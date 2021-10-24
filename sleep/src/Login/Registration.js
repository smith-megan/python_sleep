import React,{useState, useEffect} from 'react'
import "./login.css"

function Registration() {
  function registrations(event){
    event.preventDefault()
    let note=event.target.note.value
    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({note})
    };

    fetch("/login", requestOptions).then(
      res=>res.json()
    ).then(note => {
      // setNote(note)
      console.log(note)
    })
  }
  return (
    <div className="login">
        <form className="login-form" onSubmit={registrations}>
          <h2>Login</h2>
            <label>
              email:
              <input type="text" name="email"></input>
            </label>
            <label>
              password:
              <input type="password" name="password"></input>
            </label>
          <input className="login-button" type="submit"></input>
        </form>
    </div>
  )
}

export default Registration