import React,{useState, useEffect} from 'react'

function Tips() {
  const[data, setData]=useState([{}])

  useEffect(()=>{
    fetch("/tips").then(
      res=>res.json()
    ).then(data => {
      setData(data)
      console.log(data)
    })
  }, [])
  
  return (
    <div>
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

export default Tips