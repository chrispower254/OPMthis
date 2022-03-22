import './App.css';
import React from "react";
import ProcessView from "./View/ProcessView.js";
import Filters from "./View/Filters";
import MainPage from './Components/mainpage';
import Main from './Components/mainpage';


function App() {
    return (
        <>
            <div className="wrapper">
                <div className='main'>
                    <MainPage />
                </div>
            </div>
        </>
    );
}

export default App;
