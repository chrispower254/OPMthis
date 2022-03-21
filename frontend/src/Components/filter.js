import React, { useState } from "react";
import TextField from '@mui/material/TextField';
import { valueToPercent } from "@mui/base";
import { Typography } from "@mui/material";


export const MainView = () => {

  const [filters, setFilters] = useState([])
  const [value, setValue] = useState({})
  const filtersRequest = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: value
  };

  React.useEffect(() => {
    // fetch ölogik zum config holen
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
      Moinsen
      {filters.map(filter => <div>{
        <div key={filter}>
          <TextField
            label={filter}
            onChange={evt => handler(filter, evt.currentTarget.value)}
            variant="standard"
            focused
          />
        </div>
      }</div>)}
      <button onClick={() => {
        fetch("/api/config/filters/post", {
          'method': 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(value)
        })
      }}>
        Submit Filters
      </button>

    </div>
  )
}