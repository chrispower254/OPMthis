import React, { useState } from "react";
import TextField from '@mui/material/TextField';
import { valueToPercent } from "@mui/base";
import { Typography } from "@mui/material";


export const MainView = () => {

  const [filters, setFilters] = useState([])
  const [value, setValue] = useState({})
  const [defaultValue, setDefaultValue] = useState({})

  React.useEffect(() => {
    // fetch logik zum config holen 
    fetch("/api/config/filters/get").then(res => res.json()).then(data => setFilters(data.response))
  }, [])

  /*
  async function getDefaults (filter) {
    setDefaultValue({...defaultValue,[filter]: ""})
    //await fetch("/api/config/filterValues/get?query=" + filters[filter]).then(res => res.json()).then(data => setDefaultValue({...defaultValue,[filters[filter]]: data.response}))
    const response = await fetch("/api/config/filterValues/get?query=" + filter);
    const json = await response.json();
    console.log(json.response).split(",").join(";")
    setDefaultValue({...defaultValue,[filter]: json.response})
    console.log("test2")
  }

  React.useEffect(() => {
    console.log("test0")
    for (var filter in filters) {
      getDefaults(filters[filter])
      console.log("test1")
      console.log(filters[filter])
    }
  }, [])*/
  
  const handler = (filtername, eventValue) => {
    console.log("eventValue", eventValue)
    setValue({ ...value, [filtername]: eventValue.split(";") })
    setDefaultValue({ ...value, [filtername]: eventValue })
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