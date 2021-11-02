import React,{useState, useEffect} from 'react'
import './tips.css';
import {AiOutlineStar} from 'react-icons/ai';


function Tips() {
  const [tip, setTip]=useState([])
  useEffect(()=>{
    fetch("/tips").then(
      res=>res.json()
    ).then(data => {
      console.log(data.tips)
      setTip(data.tips)
      console.log(tip)
    })
  }, [])
  
  return (
    <div className="tips">
      <h1>Tips</h1>
      <div className="tips-card">
      {tip.map((element, index, array)=>{
            return(
            <div key={element+index} className="tip-div">
              <div className="tip-header-div">
                <button className="tip-star"></button>
                <h2 className="tip-header">{element[0].split(":")[0]}</h2>
              </div>
              <div className="tip-info">
                <p>{element[0].split(":")[1]}</p>
                <p><a href={element[2]}>Source</a>- {element[1]}</p>
              </div>
            </div>
            )
          })}
      </div>
    </div>
  )
}

export default Tips