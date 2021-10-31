import React,{useState, useEffect} from 'react'
import './graph.css';
import {Line} from 'react-chartjs-2';
import {BiLeftArrow, BiRightArrow} from 'react-icons/bi';

function Graph(props) {

  const[note, setNote]=useState([{}])
  const[skip, setSkip]=useState(0)
  // setSkip(0)

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

    let valuestart=event.target.wake.value
    let valuestop=event.target.sleep.value
    // console.log(valuestart,valuestop,"yikes")

    var timeStart = new Date("01/01/2007 " + valuestart);
    var timeEnd = new Date("01/01/2007 " + valuestop);

    var difference = timeEnd - timeStart;    
    // console.log(difference+"maybe")        
    var diff_result = new Date(difference);    

    var hourDiff = diff_result.getHours();
    // console.log(hourDiff +"hello")

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
      return data
      })

    setChartData({
      type: "line",
      labels:[time.dates[0].slice(0,-13), time.dates[1].slice(0,-13), time.dates[2].slice(0,-13), time.dates[3].slice(0,-13), time.dates[4].slice(0,-13), time.dates[5].slice(0,-13), time.dates[6].slice(0,-13)],
      datasets: [
        {
          label: 'Hours Slept',
          data: [time.slept_hours[0],time.slept_hours[1],time.slept_hours[2],time.slept_hours[3],time.slept_hours[4],time.slept_hours[5],time.slept_hours[6]],
          backgroundColor: [
            '#3C3D48'
          ],
          borderColor:[
            '#FFFFFF'
          ],
          borderWidth: 2,
        },
        {
          label: 'Low Baseline',
          data: [time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0]],
          backgroundColor: [
            '#EEC492'
          ],
          borderWidth: 2,
          fill: '+1'
        },
        {
          label: 'High Baseline',
          data: [time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1]],
          backgroundColor: [
            '#B58852'
          ],
          borderWidth: 2,
        }
      ]
    })
  }
  useEffect(()=>{
    chart()
  }, [])

  async function graphBack(skipped){
    let data={email: "telfor@gmalil",
      count: skipped
    }
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({data})
    };
    
    let time=await fetch("/backhistory", requestOptions).then(
      res=>res.json()
      ).then(data => {
      return(data)
    })
console.log(skip, time.dates)
    setChartData({
      type: "line",
      labels:[time.dates[0].slice(0,-13), time.dates[1].slice(0,-13), time.dates[2].slice(0,-13), time.dates[3].slice(0,-13), time.dates[4].slice(0,-13), time.dates[5].slice(0,-13), time.dates[6].slice(0,-13)],
      datasets: [
        {
          label: 'Hours Slept',
          data: [time.slept_hours[0],time.slept_hours[1],time.slept_hours[2],time.slept_hours[3],time.slept_hours[4],time.slept_hours[5],time.slept_hours[6]],
          backgroundColor: [
            '#3C3D48'
          ],          
          borderColor:[
            '#FFFFFF'
          ],
          borderWidth: 2
        },
        {
          label: 'Low Baseline',
          data: [time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0],time.hours[0]],
          backgroundColor: [
            '#EEC492'
          ],
          borderWidth: 2,
          fill: '+1'
        },
        {
          label: 'High Baseline',
          data: [time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1],time.hours[1]],
          backgroundColor: [
            '#B58852'
          ],
          borderWidth: 2,
        }
      ]
    })
    // chart()
  }
  return (
    <div>
      <div className="graph">
        <div className="left-arrow-div">
          <button className="left-arrow" 
          onClick={()=>{
            let skipped=(skip+7)
            setSkip(skipped)
            graphBack(skipped)
            }}><div className="magic-left">Older<BiLeftArrow/></div></button>
        </div>
        <div className="graph-image">
          <Line data={chartData} 
          options={{
            responsive: true,
            scales: {
              y: {
                  beginAtZero: true,
                  color: "white"
                  },
                },
                plugins: {
                  scaleBackgroundColor: {
                    color: 'white'
                  },
                  legend: {
                      display: true,
                      labels: {
                          color: '#EBEFDE'
                      }
                  }
              }
            }}
            />
        </div>
        <div className="right-arrow-div">
        <button className="right-arrow"
        onClick={()=>{
            let skipped=(skip-7)
            setSkip(skipped)
            graphBack(skipped)
                  }}><div className="magic-right">Recent<BiRightArrow/></div></button>
        </div>
      </div>
      <div className="data">
        {/* <div className="graph-updates"> */}
          <div>
            <h2>Add a time</h2>
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
        {/* </div> */}
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