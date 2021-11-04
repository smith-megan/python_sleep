import React,{useState, useEffect} from 'react'
// import Registration from './Registration';
import "./login.css"
import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

function Login(props) {
  // const[email, setEmail]=useState()
  // const[age, setAge]=useState(0)
  function logins(event){
    event.preventDefault()

    let email=event.target.email.value
    let password=event.target.password.value
    let login = {"email": email, "password": password}

    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({login})
    };

    fetch("/login", requestOptions).then(
      res=>res.json()
    ).then(data => {
      if (data.authenticate===true) {
        props.setEmail(email)
        props.setAge(data.age)
        props.setCity(data.city)
      }
      else {
        // message failure?
      }
      
    })
  }

  return (
    <div className="login">
      <div className="login-bg-div">
        <form className="login-form" onSubmit={logins}>
          <h2>Login</h2>
            <label>
              Email:
              <input type="text" name="email"></input>
            </label>
            <label>
              Password:
              <input type="password" name="password"></input>
            </label>
          <input className="login-button" type="submit"></input>
        </form>
        <Link to="/registration" className="register-link">or Register Here</Link>
      </div>
    </div>
  )
}

export default Login