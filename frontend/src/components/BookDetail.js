// src/components/BookDetail.js
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ReviewForm from "./ReviewForm";

function BookDetail() {
  const { id } = useParams();
  const [book, setBook] = useState(null);

  useEffect(() => {
    fetch(``)
      .then((response) => response.json())
      .then((data) => setBook(data));
  }, [id]);

  if (!book) return <div>Loading...</div>;

  return (
    <div>
      <h1>{book.title}</h1>
      <p>Author: {book.author}</p>
      <p>Genre: {book.genre}</p>
      <p>Summary: {book.summary}</p>
      <img src={book.cover_image_url} alt={book.title} />

      <h2>Reviews</h2>
      <ul>
        {book.reviews.map((review) => (
          <li key={review.id}>
            <p>Rating: {review.rating}</p>
            <p>{review.comment}</p>
            <p>By: {review.user.username}</p>
          </li>
        ))}
      </ul>

      <ReviewForm bookId={book.id} />
    </div>
  );
}

export default BookDetail;
