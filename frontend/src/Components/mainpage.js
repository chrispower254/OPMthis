import React, { useState } from "react";
import './grid.css';
import pic from '../files/heunet.png';
import { Filters } from "./filter";
import { Settings } from "./settings";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';


function MainPage() {
    const [filters, setFilters] = useState([])
    const [value, setValue] = useState({})
    const filtersRequest = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: value
    };

    React.useEffect(() => {
        // fetch logik zum config holen
        fetch("/api/config/filters/get").then(res => res.json()).then(data => setFilters(data.response))
    }, [])

    const handler = (filtername, eventValue) => {
        // console.log("filter",filtername)
        // console.log("value",value)
        console.log("eventValue", eventValue)
        setValue({ ...value, [filtername]: eventValue.split(";") })
    }

    console.log(value)

    // alle input werte hiolen => 5 string
    // alle strings druchen => 

    return (

        <div class="grid-container">
            <header class="header">
                <div class>O P M - D A S H B O A R D</div>
                <div style={{display: 'flex', justifyContent:'flex-end', marginRight: '5rem',marginTop: '-2.5rem'  }}>
                    <Settings/>
                </div>
            </header>
            <main class="main">
                <div class="main-cards">
                    <div class="card">
                        <img src={pic} />
                        <p></p>
                        <Button variant="contained" onClick={() => {
                            fetch("/api/update")
                        }}>REFRESH
                        </Button>
                    </div>
                    <div class="card">
                        Filter-Area
                        <>
                            <Box
                                component="form"
                                sx={{
                                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                                }}
                                noValidate
                                autoComplete="off"
                            >
                                {filters.map(filter => <div>{
                                    <div key={filter}>
                                        <TextField
                                            label={filter}
                                            id="outlined-required"
                                            onChange={evt => handler(filter, evt.currentTarget.value)}
                                        />
                                    </div>
                                }</div>)}
                            </Box>
                                <Button variant="contained" onClick={() => {
                                    fetch("/api/config/filters/post", {
                                        'method': 'POST',
                                        headers: {
                                            'Content-Type': 'application/json'
                                        },
                                        body: JSON.stringify(value)
                                    })
                                }}>
                                    SUBMIT FILTERS
                                </Button>
                        </>
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
