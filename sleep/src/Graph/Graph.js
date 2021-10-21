import React,{useState, useEffect} from 'react'

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
  

  return (
    <div>
      <div className="graph">
        <div className="left-arrow"></div>
        <div className="graph-image"></div>
        <div className="right-arrow"></div>
      </div>
      <div className="data">
        <div className="Date">
          <p>"dayofweek"</p>
          <p>"dateofweek"</p>
        </div>
        <div>
          <p>Wake up</p>
          <p>Sleep</p>
        </div>
        <div>
          <input></input>
          <input></input>
          <button>^</button>
        </div>
      </div>
      <div className="note">
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