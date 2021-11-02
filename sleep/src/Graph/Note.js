import React,{useState, useEffect, ReactDOM} from 'react'

function Note() {
  const [note, setNote]=useState([])
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
  useEffect(()=>{
    getNote()
  }, [])

  return (<div className="notes">
    <h2>Notes:</h2>
        <div>
          <div id="noteshere"> 
          {note.map((element, index, array)=>{
            return(
            <p key={element+index}>{element}</p>
            )
          })}
          </div>
          <p>add a note</p>
          <form onSubmit={saveNote}>
          <label>
            <input type="text" name="note"></input>
           </label>
           <input type="submit"></input>
          </form>
        </div>
      </div>
  )}
  // const element=(<div>
  //   <p>note</p>
  // </div>)
  // ReactDOM.render(element, document.getElementById('note'));

export default Note