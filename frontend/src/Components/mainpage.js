import React, { useState } from "react";
import '../assets/grid.css';
import pic from '../files/heunet.png';
import { Filters } from "./filter";
import { Settings } from "./settings";
import Button from '@mui/material/Button';


function MainPage() {
    const [throughputTime,setThroughputTime] = useState("")
    return (

        <div class="grid-container">
            <header class="header">
                <div>O P M - D A S H B O A R D </div>
                <div style={{ display: 'flex', justifyContent: 'flex-end', marginRight: '5rem', marginTop: '-2.5rem' }}>
                    <Settings />
                </div>
            </header>
            <main class="main">
                    <div class="overviewcard">
                        <div>Average Throughput-Time: {throughputTime} sec</div>
                </div>
                <div class="main-cards">
                    <div class="card">
                        <img src={pic} />
                        <p></p>
                        <Button variant="contained" onClick={() => {
                            fetch("/api/update").then(res => res.json()).then(data => {
                                setThroughputTime(data.response)
                                console.log(data.response)
                            })
                        }}>REFRESH
                        </Button>
                        
                    </div>
                    
                    <div class="card">
                        Filter-Area
                            <Filters />
                    </div>
                </div>
            </main>

            <footer class="footer">
                <div class="footer__copyright">&copy; Chris Schroeder &amp; Daniel Fischer</div>
            </footer>
        </div>


    )
}
export default MainPage;