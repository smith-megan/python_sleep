import React,{useState, useEffect} from 'react'
import './tips.css';
import {AiOutlineStar} from 'react-icons/ai';


function Tips(props) {
  const [tip, setTip]=useState([])
  useEffect(()=>{
    fetch("/tips").then(
      res=>res.json()
    ).then(data => {
      setTip(data.tips)
    })
  }, [])

  function favorited(idNum) {
    let data={user_email: props.email,
      tip_id: idNum
    }
      const requestOptions={
        method: 'POST',
        headers:{'Content-Type': 'application/json'},
        body: JSON.stringify({data})
      };
  
      fetch("/savedtip", requestOptions).then(
        res=>res.json()
      ).then(data => {
      })
  }
  return (
    <div className="tips">
      <h1>Tips</h1>
      <div className="tips-card">
      {tip.map((element, index, array)=>{
            return(
            <div key={element+index} className="tip-div">
              <div className="tip-header-div">
                <button className="tip-star"onClick={()=>{favorited(element[3])}}></button>
                <h2 className="tip-header">{element[0].split(":")[0]}</h2>
              </div>
              <div className="tip-info">
                <p>{element[0].split(":")[1]}</p>
                <p><a href={element[2]} className="tip-link">Source</a>- {element[1]}</p>
              </div>
            </div>
            )
          })}
      </div>
    </div>
  )
}

export default Tips