import '../App.css';
import pic from '../files/heunet.png';
import React from "react";

function ProcessView() {
    return(
        <div className="App">
      <header className="App-header">
        <img src={pic}/>
          <button onClick={() => {
              fetch("/api/update")
          }}>
              OPM THIS SHIEEETasdasds
          </button>

        <form>
          <label>
            Name:
            <input type="text" name="name" />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </header>
    </div>
    )
}

export default ProcessView;
