import './App.css';
import pic from './files/heunet.png'
import React, {useState, useEffect} from "react";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={pic}/>
          <button onClick={() => {
              fetch("/api/update")
          }}>
              OPM THIS SHIEEET
          </button>
      </header>
    </div>
  );
}

export default App;
