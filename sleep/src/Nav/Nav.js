import React,{useState, useEffect} from 'react'
import "./nav.css"
import Graph from '../Graph/Graph.js'
import Home from '../Home.js'
import Login from '../Login/Login.js'
import Registration from '../Login/Registration'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function Nav() {
  const[data, setData]=useState([{}])

  return (
    <div className="nav">
      <Router>
      <div className="logo-div">
        <div className="logo"></div>
        <p className="logo-title">Sleep Central</p>
        <div></div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/">Tips</Link>
          <Link to="/graph">Graph</Link>
          <Link to="/login">Login</Link>
        </div>
      </div>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route path="/graph">
            <Graph/>
          </Route>
          <Route>
            <Login/>
          </Route>
          <Route>
            <Registration path="/registration"/>
          </Route>
          <Route>
            {/* <Registration path="/registration"/> */}
          </Route>

        </Switch>
      </Router>

    </div>
  )
}

export default Nav