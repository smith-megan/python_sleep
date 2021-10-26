import React,{useState, useEffect} from 'react'
import './graph.css';
import {Line} from 'react-chartjs-2';

function Graph() {

  const[note, setNote]=useState([{}])

  function saveNote(event) {
    event.preventDefault()
    let note=event.target.note.value
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({note})
    };

    fetch("/notes", requestOptions).then(
      res=>res.json()
    ).then(note => {
      setNote(note)
      console.log(note)
    })
  }

  const [chartData, setChartData]=useState({})

  const chart=()=>{
    setChartData({
      type: "line",
      labels:['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
      datasets: [
        {
          label: 'Low Healthy Baseline',
          data: [6,6,6,6,6,6,6],
          backgroundColor: [
            'rgb(167,25,22,.7)'
          ],
          borderWidth: 2,
          fill: '+1'
        },
        {
          label: 'High Healthy Baseline',
          data: [9,9,9,9,9,9,9],
          backgroundColor: [
            'rgb(167,25,22,100)'
          ],
          borderWidth: 2,
        },
        {
          label: 'Your hours slept',
          data: [5,4,3,2,12,15,0],
          backgroundColor: [
            '#000000'
          ]
        }
      ]
    })
  }

  useEffect(()=>{
    chart()
  }, [])
  return (
    <div>
      <div className="graph">
        <div className="left-arrow"></div>
        <div className="graph-image">
          <Line data={chartData} 
          options={{
            responsive: true,
            scales: {
              y: {
                  beginAtZero: true
                  },
                }
            }}
            />
        </div>
        <div className="right-arrow"></div>
      </div>
      <div className="data">
        <div className="graph-updates">
          <div>
            <p>Wake up</p>
            <p>Sleep</p>
          </div>
          <div>
            <p>"dateofweek"</p>
            <p>"dayofweek"</p>
            <input></input>
            <input></input>
            <button>^</button>
          </div>
        </div>
      </div>
      <div className="note">
        <h2>Notes:</h2>
        <form onSubmit={saveNote}>
          <label>
          <input type="text" name="note"></input>
          </label>
          <input type="submit"></input>
        </form>
      </div>
    </div>
  )
}

export default Graph