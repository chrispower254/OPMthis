import React, { useState } from "react";
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';


const style = {
  width: 250,
};

export const Filters = () => {

  const [filters, setFilters] = useState(['placeholder'])
  const [values, setValues] = useState({})
  const [isLoading, setLoading] = useState(true);
  const [defaultValues, setDefaultValues] = useState({})
  const [throughputTime, setThroughputTime] = useState("")

  // Calls API to retrieve all fields that we can filter on
  React.useEffect(() => {
    fetch("/api/config/filters/eventAttribute/get").then(res1 => res1.json()).then(data1 => {
      setFilters(data1.response)
      fetch("/api/config/filters/get").then(res2 => res2.json()).then(data2 => {
        setValues(data2.response)
        var jsonObj = {}
        for (var key in data1.response) {
          jsonObj[data1.response[key]] = data2.response[data1.response[key]] ? data2.response[data1.response[key]].join(";") : ""
        }
        setDefaultValues(jsonObj)
        setLoading(false)
      })
    })
  }, [])

  const handler = (filtername, eventValue) => {
    setDefaultValues({ ...values, [filtername]: eventValue })
    setValues({ ...values, [filtername]: eventValue.split(";") })
  }

  console.log(values)

  const render = () => {
    if (isLoading) return "\n Loading...";
    else {
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
                  value={defaultValues[filter]}
                />
              </div>
            }</div>)}
            <Box sx={style}>
              <Button variant="contained"
                onClick={() => {
                  fetch("/api/config/filters/post", {
                    'method': 'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(values)
                  })
                }}>
                SUBMIT FILTERS
              </Button>
              <Button variant="contained"
                sx={{ mx: 1 }}
                onClick={() => {
                  fetch("/api/config/filters/get").then(res2 => res2.json()).then(data2 => {
                    setValues(data2.response)
                    var jsonObj = {}
                    for (var key in filters) {
                      jsonObj[filters[key]] = data2.response[filters[key]] ? data2.response[filters[key]].join(";") : ""
                    }
                    setDefaultValues(jsonObj)
                    setLoading(false)
                  })
                }}>
                RESET
              </Button>
            </Box>
          </Box>
        </div>
      )
    }
  }
  return render()
}

