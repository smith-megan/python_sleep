import React,{useState, useEffect} from 'react'
import "./home.css"
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function Home() {
  const[data, setData]=useState([{}])

  return (
    <div className="home">
  {/* nav? */}
      <h1 className="title">Sleep Central</h1>
      <Link to="/login"><button className="home-btn">Login</button></Link>
    </div>
  )
}

export default Home