// src/components/App.js
import React from "react";
import { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from "./NavBar";
import BookList from "./BookList";
import BookDetail from "./BookDetail";
import UserProfile from "./UserProfile";
import Login from "./Login";
import Signup from "./Signup";

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/check_session")
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("User not authenticated");
        }
      })
      .then((user) => {
        setUser(user);
      })
      .catch((error) => {
        console.error("Session check failed:", error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleLogout() {
    setUser(null);
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <Router>
        <NavBar user={user} onLogout={handleLogout} />
        <Switch>
          <Route exact path="/books" component={BookList} />
          <Route path="/bookdetails/:id" component={BookDetail} />
          <Route
            path="/profile"
            render={(props) => <UserProfile {...props} user={user} />}
          />
          <Route
            path="/login"
            render={(props) => <Login {...props} onLogin={handleLogin} />}
          />
          <Route path="/signup" component={Signup} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
