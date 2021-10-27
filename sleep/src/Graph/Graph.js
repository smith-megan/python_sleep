import React,{useState, useEffect} from 'react'
import './graph.css';
import {Line} from 'react-chartjs-2';

function Graph(props) {

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

  function sendData(event) {
    event.preventDefault()
    let data={sleep: event.target.sleep.value,
    wake: event.target.wake.value,
    date: event.target.date.value
  }
  console.log(event.target.date.value)
    console.log(data)
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({data})
    };

    fetch("/data", requestOptions).then(
      res=>res.json()
    ).then(data => {
      // setNote(note)
      console.log(data)
    })
  }

  const [chartData, setChartData]=useState({})

  async function chart(){
    let email="telfor@gmalil"
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({email})
    };
    
    const time=await fetch("/graph", requestOptions).then(
      res=>res.json()
    ).then(data => {
      // console.log(data)
      return data
      })
      
      console.log(time.hours[0])
    setChartData({
      type: "line",
      labels:['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
      datasets: [
        {
          label: 'Low Healthy Baseline',
          data: [time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0]],
          backgroundColor: [
            'rgb(167,25,22,.7)'
          ],
          borderWidth: 2,
          fill: '+1'
        },
        {
          label: 'High Healthy Baseline',
          data: [time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1]],
          backgroundColor: [
            'rgb(167,25,22,100)'
          ],
          borderWidth: 2,
        },
        {
          label: 'Your hours slept',
          // data: [data1,data2,data3,data4,data5,data6,data7],
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
      <p>hello{props.age}</p>
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
            <form onSubmit={sendData}>
              <label> date
              <input type="date" name="date"></input>
              </label>
              <label> wake-up
              <input type="time" name="wake"></input>
              </label>
              <label> sleep
              <input type="time" name="sleep"></input>
              </label>
              <input type="submit"></input>
            </form>
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