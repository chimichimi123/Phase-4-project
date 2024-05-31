// src/components/ReviewForm.js

import React, { useState } from "react";

function ReviewForm({ bookId }) {
  const [rating, setRating] = useState("");
  const [comment, setComment] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send data to backend API for creating a review
    console.log("Submitting review:", { rating, comment, bookId });
    // Clear form fields after submission
    setRating("");
    setComment("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Review</h2>
      <label>
        Rating:
        <input
          type="number"
          value={rating}
          onChange={(e) => setRating(e.target.value)}
        />
      </label>
      <label>
        Comment:
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
        />
      </label>
      <button type="submit">Submit Review</button>
    </form>
  );
}

export default ReviewForm;
