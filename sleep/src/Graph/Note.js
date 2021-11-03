import React,{useState, useEffect, ReactDOM} from 'react'

function Note(props) {
  const [note, setNote]=useState([])
  const [tip, setTip]=useState([])
  // let notes='hello'

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
    ).then(data => {
      getNote()
    })
  }
function getNote() {
  const requestOptions={
    method: 'GET',
    headers:{'Content-Type': 'application/json'}
  };
  fetch("/notes", requestOptions).then(
    res=>res.json()
  ).then(data => {
    setNote(data.notes)
  })
}

function getTips(){
  const requestOptions={
    method: 'GET',
    headers:{'Content-Type': 'application/json'}
  };

  fetch(`/dashboardtip/${props.email}`, requestOptions).then(
    res=>res.json()
  ).then(data => {
    console.log(data.tips)
    setTip(data.tips)
  })
}

useEffect(()=>{
  getNote()
  getTips()
}, [])

  return (<div className="notes">
        <div>
          <h2>Notes</h2>
          <div id="noteshere"> 
          {note.map((element, index, array)=>{
            return(
            <p key={element+index}>{element[0]}</p>
            )
          })}
          </div>
        </div>
        <div className="add-note-div">
          <form onSubmit={saveNote}>
          <label>
          <p>Add a note</p>
            <input type="text" name="note"></input>
           </label>
           <input className="add-time-btn" type="submit"></input>
          </form>
        </div>
        <div className="dash-tips-div">
          <h2>Tips</h2>
          <div className="dash-tips-grid">
          {tip.map((element, index, array)=>{
            return(
              <div className="dash-tips" key={element+index}>
                <button className="dash-tip-star"onClick={()=>{
                  // unfavorited(element[3])
                }}></button>
                <p><a className="dash-tips-link" href={element[1]}>{element[0].split(":")[0]}</a></p>
            </div>
            )
          })}
          </div>
        </div>
      </div>
  )}

export default Note