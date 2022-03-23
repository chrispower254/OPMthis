import React, { useState } from "react";
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { valueToPercent } from "@mui/base";
import { Typography } from "@mui/material";


export const Filters = () => {

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
    <div>
      <Box
        component="form"
        sx={{
          '& .MuiTextField-root': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
        style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}
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
          <Button variant="contained"
            onClick={() => {
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
      </Box>
    </div>
  )
}

