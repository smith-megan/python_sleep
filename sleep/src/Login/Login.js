import React,{useState, useEffect} from 'react'
import "./login.css"
import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";

function Login() {
  const[email, setEmail]=useState()
  const[age, setAge]=useState([{age:0}])

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
      console.log(data.authenticate)
      if (data.authenticate===true) {
        //set state to email
      }
      else {
        // message failure?
      }
      
    })
  }

  function regist(event){
    event.preventDefault()

    let user_details={name:event.target.name.value,
    email:event.target.email.value,
    password: event.target.password.value,
    city: event.target.city.value,
    birthday: event.target.birthday.value}

    const requestOptions={
      method: 'POST',
      headers:{'Content-Type': 'application/json'},
      body: JSON.stringify({user_details})
    };

    fetch("/register", requestOptions).then(
      res=>res.json()
    ).then(data => {
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
          <h2>Register</h2>
          <label>
            name:
            <input type="text" name="name"></input>
          </label>
          <label>
            email:
            <input type="text" name="email"></input>
          </label>
          <label>
            city:
            <input type="text" name="city"></input>
          </label>
          <label>
            birthday:
            <input type="date" name="birthday"></input>
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

export default Login