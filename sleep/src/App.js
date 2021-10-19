import React,{useState, useEffect} from 'react'
import Graph from './Graph.js'
import Tips from './Tips.js'

function App() {
  const[data, setData]=useState([{}])

  useEffect(()=>{
    fetch("/members").then(
      res=>res.json()
    ).then(data => {
      setData(data)
      console.log(data)
    })
  }, [])
  
  return (
    <div>
      <Graph />
      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i)=>(
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  )
}

export default App