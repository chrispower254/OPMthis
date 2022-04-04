import React, { useState } from "react";
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import Fade from '@mui/material/Fade';
import IconButton from '@mui/material/IconButton';
import SettingsIcon from '@mui/icons-material/Settings';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';



const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 600,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
};

// Defines list for OPM algorithm and process net type
// OPM algorithms require special process nets
const opmStyles = [
    {
        value: 'dfg;dfg',
        label: 'dfg;dfg',
    },
    {
        value: 'heu_min;heu_net',
        label: 'heu_min;heu_net',
    },
    {
        value: 'inductive;process_tree',
        label: 'inductive;process_tree',
    }
];

// Type of the log, that will be generated
const eventLogTypes = [
    {
        value: 'csv',
        label: 'csv',
    },
    {
        value: 'test',
        label: 'test',
    }
];


export const Settings = () => {
    const [settings, setSettings] = useState({
        'baseUrl': '',
        'eventAttributes': [''],
        'kafkaSettings': {
            'topic': '',
            'bootstrapServers': '',
        },
        'opmSettings': {
            'eventLogType': '',
            'opmAlgo': '',
            'processNetType': '',
            'heuMinConfig': {
                'dependency': 0.5
            }
        }
    })
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [throughputTime,setThroughputTime] = useState("")


    // Calls API to retrieve configurations
    React.useEffect(() => {
        fetch("api/config/get").then(res => res.json()).then(data => {
            setSettings(data.response)
        })
    }, [])


    // Passes the input of the forms into the settings constant
    const handler = (field, eventValue) => {
        console.log(field + " settings: " + eventValue)
        if (field == "bootstrapServers" || field == "topic") {
            setSettings({
                ...settings, ['kafkaSettings']: {
                    ...settings['kafkaSettings'], [field]: eventValue
                }
            })
        }
        else if (field == "eventAttributes") {
            setSettings({ ...settings, [field]: eventValue.split(";") })
        }
        else if (field == "dependency") {
            setSettings({
                ...settings, ['opmSettings']: {
                    ...settings['opmSettings'], ['heuMinConfig']: {
                        ...settings['opmSettings']['heuMinConfig'], [field]: eventValue
                    }
                }
            })
        }
        else {
            setSettings({ ...settings, [field]: eventValue })
        }
    }

    // Passes the input of the OPM style form into the settings
    const handleOpmStyle = (event: React.ChangeEvent<HTMLInputElement>) => {
        var input = event.target.value.split(";")
        setSettings({
            ...settings, ['opmSettings']: {
                ...settings['opmSettings'], ['opmAlgo']: input[0], ['processNetType']: input[1]
            }
        })
    };

    // Passes the input of the event log type form into the settings
    const handleEventLogType = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSettings({
            ...settings, ['opmSettings']: {
                ...settings['opmSettings'], ['eventLogType']: event.target.value
            }
        })
    };

    return (
        <div>
            <IconButton aria-label="delete" onClick={handleOpen}>
                <SettingsIcon sx={{ fontSize: 50 }} />
            </IconButton>
            <Modal
                aria-labelledby="transition-modal-title"
                aria-describedby="transition-modal-description"
                open={open}
                onClose={handleClose}
                closeAfterTransition
                BackdropComponent={Backdrop}
                BackdropProps={{
                    timeout: 500,
                }}
            >
                <Fade in={open}>
                    <Box sx={style}>
                        <Typography id="transition-modal-title" variant="h6" component="h2" pb={3}>
                            Edit configurations
                        </Typography>
                        <div key="baseUrlKey">
                            <TextField
                                label="Connected URL"
                                id="outlined-required"
                                onChange={evt => handler('baseUrl', evt.currentTarget.value)}
                                fullWidth
                                value={settings['baseUrl']}
                            />
                        </div>
                        <div key="eventAttributesKey">
                            <TextField
                                label="Event attributes (separate with comma)"
                                id="outlined-required"
                                onChange={evt => handler('eventAttributes', evt.currentTarget.value)}
                                fullWidth
                                value={settings['eventAttributes'].join(";")}
                            />
                        </div>
                        <div key="kafkaTopicKey">
                            <TextField
                                label="Kafka topic"
                                id="outlined-required"
                                onChange={evt => handler('topic', evt.currentTarget.value)}
                                fullWidth
                                value={settings['kafkaSettings']['topic']}
                            />
                        </div>
                        <div key="kafkaBootstrapServersKey">
                            <TextField
                                label="Kafka bootstrap server"
                                id="outlined-required"
                                onChange={evt => handler('bootstrapServers', evt.currentTarget.value)}
                                fullWidth
                                value={settings['kafkaSettings']['bootstrapServers']}
                            />
                        </div>
                        <div key="opmSettingsEventLogTypeKey">
                            <TextField
                                id="outlined-select-currency"
                                select
                                fullWidth
                                label="Event log type"
                                value={settings['opmSettings']['eventLogType']}
                                onChange={handleEventLogType}
                            >
                                {eventLogTypes.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                ))}
                            </TextField>
                        </div>
                        <div key="opmSettingsOpmStyleKey">
                            <TextField
                                id="outlined-select-currency"
                                select
                                fullWidth
                                label="OPM algo ; Net type"
                                value={settings['opmSettings']['opmAlgo'] + ";" + settings['opmSettings']['processNetType']}
                                onChange={handleOpmStyle}
                            >
                                {opmStyles.map((option) => (
                                    <MenuItem key={option.value} value={option.value}>
                                        {option.label}
                                    </MenuItem>
                                ))}
                            </TextField>
                        </div>
                        <div key="opmSettingsHeuMinConfigDependencyKey">
                            <TextField
                                label="HeuMin dependency"
                                id="outlined-required"
                                onChange={evt => handler('dependency', evt.currentTarget.value)}
                                fullWidth
                                value={settings['opmSettings']['heuMinConfig']['dependency']}
                            />
                        </div>
                        <Button variant="contained" sx={{ mx: 1, marginLeft: 'auto', marginTop: '1rem' }}
                            onClick={() => {
                                console.log(settings)
                                fetch("/api/config/post", {
                                    'method': 'POST',
                                    headers: {
                                        'Content-Type': 'application/json'
                                    },
                                    body: JSON.stringify(settings)
                                })
                            }}>
                            SUBMIT SETTINGS
                        </Button>
                        <Button
                            variant="contained"
                            sx={{ mx: 1, marginLeft: 'auto', marginTop: '1rem' }}
                            onClick={() => { fetch("api/config/get").then(res => res.json()).then(data => setSettings(data.response)) }}>
                            RESET
                        </Button>
                        <Button variant="outlined" color="error" sx={{ marginLeft: 'auto', marginTop: '1rem' }}
                            onClick={() => {
                                fetch("/api/restart")
                                console.log("?")
                            }}>RESTART APP
                        </Button>
                    </Box>
                </Fade>
            </Modal>
        </div>
    );
}