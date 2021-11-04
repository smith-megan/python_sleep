import React,{useState, useEffect, ReactDOM} from 'react'

function Note(props) {
  const [note, setNote]=useState([])
  const [tip, setTip]=useState([])
  // let notes='hello'

  function saveNote(event) {
    event.preventDefault()
    // let note={note: event.target.note.value, email: props.email}
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({note: event.target.note.value, email: props.email})
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
  fetch(`/notes/${props.email}`, requestOptions).then(
    res=>res.json()
  ).then(data => {
    setNote([data.notes])
  })
}

function deleteNote(noteId) {
  // event.preventDefault()
  const requestOptions={
    method: 'DELETE',
    headers:{'Content-Type': 'application/json'}
  };

  fetch(`/notes/${props.email}/${noteId}`, requestOptions).then(
    res=>res.json()
  ).then(data => {
    getNote()
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
    setTip(data.tips)
  })
}

function deleteTip(tipId) {
  const requestOptions={
    method: 'DELETE',
    headers:{'Content-Type': 'application/json'}
  };

  fetch(`/tips/${props.email}/${tipId}`, requestOptions).then(
    res=>res.json()
  ).then(data => {
    getTips()
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
              <div>
                <p className="notes-item" key={element+index} onClick={()=>{
                  deleteNote(element[1])
                  }}>{element[0]}</p>
              </div>
            )
          })}
          </div>
        </div>
        <div className="add-note-div">
          <form className="add-note-form"onSubmit={saveNote}>
          <label>
          <p>Add a note</p>
            <input type="text" name="note"></input>
           </label>
           <input className="add-note-btn" type="submit"></input>
          </form>
        </div>
        <div className="dash-tips-div">
          <h2>Tips</h2>
          <div className="dash-tips-grid">
          {tip.map((element, index, array)=>{
            return(
              <div className="dash-tips" key={element+index}>
                <button className="dash-tip-star"onClick={()=>{
                  deleteTip(element[2])
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