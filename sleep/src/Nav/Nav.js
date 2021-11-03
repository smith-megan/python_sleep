import React,{useState, useEffect} from 'react'
import "./nav.css"
import Graph from '../Graph/Graph.js'
import Home from '../Home.js'
import Login from '../Login/Login.js'
import Registration from '../Login/Registration'
import Tips from "../Tips/Tips"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function Nav() {
  const[age, setAge]=useState(21)
  const[city, setCity]=useState('Salt Lake City')
  const[email, setEmail]=useState('')

  return (
    <div className="nav">
      <Router>
      <div className="logo-div">
        <div className="logo"></div>
        <p className="logo-title">Sleep Central</p>
        <div></div>
        <div className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/tips">Tips</Link>
          <Link to="/graph">Graph</Link>
          {email?<Link onClick={()=>{setEmail('')}} to="/login">Logout</Link>:<Link to="/login">Login</Link>}
        </div>
      </div>
        <Switch>
          <Route exact path="/">
            <Home/>
          </Route>
          <Route path="/graph">
            <Graph age={age} setAge={setAge} city={city} setCity={setCity} email={email} setEmail={setEmail}/>
          </Route>
          <Route path="/login">
            <Login age={age} setAge={setAge} city={city} setCity={setCity} email={email} setEmail={setEmail}/>
          </Route>
          <Route path="/registration">
            <Registration/>
          </Route>
          <Route path="/tips">
            <Tips email={email}/>
          </Route>

        </Switch>
      </Router>

    </div>
  )
}

export default Nav