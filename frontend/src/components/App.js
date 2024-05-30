// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from "./NavBar";
import BookList from "./BookList";
import BookDetail from "./BookDetail.js";
import UserProfile from "./UserProfile";

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
