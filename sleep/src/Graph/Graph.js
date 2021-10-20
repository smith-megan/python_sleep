import React,{useState, useEffect} from 'react'

function Graph() {
  
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
    </div>
  )
}

export default Graph