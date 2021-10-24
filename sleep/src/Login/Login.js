import React,{useState, useEffect} from 'react'
import "./login.css"
import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

function Login() {
  function logins(event){
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

  function regist(event){
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
        <form className="login-form" onSubmit={logins}>
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
        {/* <Link to="/registration">Register Here</Link> */}
        </form>
        <form className="login-registration" onSubmit={regist}>
          <h2>Registration</h2>
          <label>
            name:
            <input type="text"></input>
          </label>
          <label>
            email:
            <input type="text"></input>
          </label>
          <label>
            password:
            <input type="password"></input>
          </label>
          <input className="login-button" type="submit"></input>
        </form>
    </div>
  )
}

export default Login