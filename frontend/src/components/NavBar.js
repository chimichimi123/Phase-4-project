// src/components/NavBar.js
import React from "react";
import { Link } from "react-router-dom";

function NavBar({ user, handleLogout }) {
  return (
    <nav>
      <ul>
        {user ? (
          <>
            <p>Welcome, {user.username}!</p>
            <button onClick={handleLogout}>Logout</button>
          </>
        ) : (
          <li>
            <Link to="/login">Click Here to Login</Link>
          </li>
        )}
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/profile">Profile</Link>
        </li>
        <li>
          <Link to="/books">Book List</Link>
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
