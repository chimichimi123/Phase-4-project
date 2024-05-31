#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from faker import Faker

# Local imports
from app import app
from config import db
from models import Book, BookDetails, User
from flask_bcrypt import generate_password_hash

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

books = [
    {
        'title': 'Harry Potter and the Sorcerer\'s Stone',
        'author': 'J. K. Rowling',
        'genre': 'Fiction',
        'summary': 'Harry potter goes on a wild adventure looking for the sorceres stone',
        'cover_image_url': 'https://books.google.com/books/content?id=ZiJMzwEACAAJ&printsec=frontcover&img=1&zoom=1&imgtk=AFLRE73fcP8ox6Jj2Re-qvN8NuGP95b1yV7nt0maSqibJw2LOWUJivaLENbQnZUmK5TUX3auVg-t0M4vV7i3byIXJ9ad2w6PQpJgZYVJbyYbOTY4jI87UGE_zCOm03fVVg1SsGsUkb-3',
        'details': {
            'genre': 'Fiction',
            'year': 1997,
            'pages': 333,
            'publisher': 'Scholastic Incorporated',
            'description': 'Harry Potter has never even heard of Hogwarts when the letters start dropping on the doormat at number four, Privet Drive. Addressed in green ink on yellowish parchment with a purple seal, they are swiftly confiscated by his grisly aunt and uncle. Then, on Harry\'s eleventh birthday, a great beetle-eyed giant of a man called Rubeus Hagrid bursts in with some astonishing news: Harry Potter is a wizard, and he has a place at Hogwarts School of Witchcraft and Wizardry. An incredible adventure is about to begin!',
        }
    },
    {
        'title': 'Harry Potter and the Prisoner of Azkaban',
        'author': 'J. K. Rowling',
        'genre': 'fiction',
        'summary': 'Harry potter and his run in with the prisoner of Azkaban',
        'cover_image_url': 'https://books.google.com/books/content?id=fryNzwEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api',
        'details': {
            'genre': 'fiction',
            'year': 2004,
            'pages': 435,
            'publisher': 'Scholastic Incorporated',
            'description': '"Return to Hogwarts in this stunning edition of Harry Potter and the Prisoner of Azkaban. J.K. Rowling s complete and unabridged text is accompanied by full-color illustrations on nearly every page and eight paper-engineered interactive elements: Readers will explore the Knight Bus, reveal the Grim in a teacup, spin the Time-Turner, and more."',
        }
    },
]

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

with app.app_context():
    hashed_password = generate_password_hash('password').decode('utf-8')

    user = User(
        username='username',
        password_hash=hashed_password
    )
    db.session.add(user)
    db.session.commit()

    
    for _ in range(5):
        fake_username = fake.user_name()
        fake_email = fake.email()
        fake_password_hash = hashed_password
        fake_user = User(username=fake_username, email=fake_email, password_hash=fake_password_hash)
        db.session.add(fake_user)

    for book_data in books:
        book = Book(
            title=book_data['title'],
            author=book_data['author'],
            summary=book_data['summary'],
            cover_image_url=book_data['cover_image_url']
        )
        db.session.add(book)
        db.session.flush()

        details_data = book_data.get('details', {})
        if details_data:
            details = BookDetails(
                book_id=book.id,
                genre=details_data.get('genre'),
                year=details_data.get('year'),
                pages=details_data.get('pages'),
                publisher=details_data.get('publisher'),
                description=details_data.get('description')
            )
            db.session.add(details)

    db.session.commit()
