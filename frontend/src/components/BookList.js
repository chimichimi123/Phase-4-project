import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("https://book-review-project-backend-db1.onrender.com/books")
      .then((response) => response.json())
      .then((data) => setBooks(data));
  }, []);

  return (
    <div>
      <h2>Book List</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            {/* bookdetails page link */}
            <Link to={`/book/${book.id}`}>
              <h3>{book.title}</h3>
              <p>Author: {book.author}</p>
              {/* additional book details */}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;
