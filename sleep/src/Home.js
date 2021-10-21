import React,{useState, useEffect} from 'react'

function Home() {
  const[data, setData]=useState([{}])

  return (
    <div className="home">
  {/* nav? */}
      <h1>Sleep Guide Central</h1>
      <button className="home-btn">login</button>

    </div>
  )
}

export default Home