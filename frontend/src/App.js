import './App.css';
import React from "react";
import ProcessView from "./View/ProcessView.js";
import Filters from "./View/Filters";


function App() {
    return (
        <>
            <div className="wrapper">
                <div className='main'>
                    <Filters />
                    <ProcessView />
                </div>
            </div>
        </>
    );
}

export default App;
