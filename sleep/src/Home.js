import React,{useState, useEffect} from 'react'
import "./home.css"

function Home() {
  const[data, setData]=useState([{}])

  return (
    <div className="home">
  {/* nav? */}
      <h1 className="title">Sleep Central</h1>
      <button className="home-btn">login</button>
    </div>
  )
}

export default Home