import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("https://book-review-project-backend.onrender.com/books")
      .then((response) => response.json())
      .then((data) => setBooks(data));
  }, []);

  return (
    <div>
      <h2>Book List</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            {/* Link to the BookDetailPage for each book */}
            <Link to={`/book/${book.id}`}>
              <h3>{book.title}</h3>
              <p>Author: {book.author}</p>
              {/* Add additional book details as needed */}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;
