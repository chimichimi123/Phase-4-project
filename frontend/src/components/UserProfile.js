import React, { useEffect, useState } from "react";

function UserProfile() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from backend API
    fetch("/users")
      .then((response) => response.json())
      .then((data) => setUser(data));
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>User Profile</h1>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
      <h2>Favorite Books</h2>
      <ul>
        {user.favoriteBooks.map((book) => (
          <li key={book.id}>
            <p>{book.title}</p>
            <p>Author: {book.author}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserProfile;
