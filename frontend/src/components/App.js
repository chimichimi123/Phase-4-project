// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from "./components/NavBar";
import BookList from "./components/BookList";
import BookDetail from "./components/BookDetail";
import UserProfile from "./components/UserProfile";

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route exact path="/" component={BookList} />
        <Route path="/book/:id" component={BookDetail} />
        <Route path="/profile" component={UserProfile} />
      </Switch>
    </Router>
  );
}

export default App;
