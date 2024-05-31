// src/components/App.js
import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from "./NavBar";
import BookList from "./BookList";
import BookDetail from "./BookDetail";
import UserProfile from "./UserProfile";
import Login from "./Login";
import SignUpForm from "./SignupForm";

function App() {
  return (
    <div className="App">
      <Router>
        <NavBar />
        <Switch>
          <Route exact path="/books" component={BookList} />
          <Route path="/bookdetails/:id" component={BookDetail} />
          <Route path="/profile" component={UserProfile} />
          <Route path="/login" component={Login} />
          <Route path="/signup" component={SignUpForm} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
