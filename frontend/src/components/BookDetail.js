import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import ReviewForm from "./ReviewForm";

function BookDetail() {
  const { id } = useParams();
  const [book, setBook] = useState(null);
  const [error, setError] = useState(null);
  const [isFavorite, setIsFavorite] = useState(false);
  const userId = 1;

  useEffect(() => {
    fetch(`/books/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((basicBookData) => {
        setBook({
          id: basicBookData.id,
          title: basicBookData.title,
          author: basicBookData.author,
          summary: basicBookData.summary,
          cover_image_url: basicBookData.cover_image_url,
        });

        fetch(`/bookdetails/${id}`)
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
          .then((detailsData) => {
            setBook((prevBook) => ({
              ...prevBook,
              genre: detailsData.genre,
              year: detailsData.year,
              pages: detailsData.pages,
              publisher: detailsData.publisher,
              description: detailsData.description,
            }));
          })
          .catch((err) => setError(err.message));
      })
      .catch((err) => setError(err.message));
  }, [id]);

  const handleFavoriteClick = () => {
    fetch(`/users/favorite`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userId, bookId: id }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(() => {
        setIsFavorite(true);
      })
      .catch((err) => setError(err.message));
  };

  if (error) return <div>Error: {error}</div>;
  if (!book) return <div>Loading...</div>;

  return (
    <div>
      <h1>{book.title}</h1>
      <p>Written by Author: {book.author}</p>
      <img src={book.cover_image_url} alt={book.title} />

      <h2>Book Details</h2>
      <p>Genre: {book.genre || "Unavailable"}</p>
      <p>Year: {book.year || "Unavailable"}</p>
      <p>Pages: {book.pages || "Unavailable"}</p>
      <p>Publisher: {book.publisher || "Unavailable"}</p>
      <p>Description: {book.description || "Unavailable"}</p>

      <button onClick={handleFavoriteClick} disabled={isFavorite}>
        {isFavorite ? "Added to Favorites" : "Add to Favorites"}
      </button>

      <h2>Reviews</h2>
      <ul>
        {book.reviews && book.reviews.length > 0 ? (
          book.reviews.map((review) => (
            <li key={review.id}>
              <p>Rating: {review.rating}</p>
              <p>{review.comment}</p>
              <p>By: {review.user.username}</p>
            </li>
          ))
        ) : (
          <li>No reviews available.</li>
        )}
      </ul>

      <ReviewForm bookId={book.id} />
    </div>
  );
}

export default BookDetail;
