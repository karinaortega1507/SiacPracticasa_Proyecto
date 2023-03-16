import React, { useContext, useEffect, useRef, useState } from "react";
import {
  Container,
  Grid,
  TextField,
  MenuItem,
  Select,
  Paper,
  Button,
  Typography,
  InputLabel,
} from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

import loginImages from "../helpers/login/getImgs";
import { LoginContext } from "../contexts/LoginContext";
import { useNavigate } from "react-router-dom";

const options = [
  { value: "option1", label: "Opción 1" },
  { value: "option2", label: "Opción 2" },
  { value: "option3", label: "Opción 3" },
];
const useStyles = makeStyles((theme) => ({
  paper: {
    margin: theme.spacing(8, 4),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1 ),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
    backgroundColor: "#406AF5",
  },

  img: { width: "50px", height: "50px", marginRight: "8px" },

  combobox: {
    marginBottom: "30px",
    display: "flex",
    alignItems: "center",
  },
}));
const LoginInner = () => {
  const classes = useStyles();
  const navigate = useNavigate()
  const [selectedValue1, setSelectedValue1] = useState("");
  const [selectedValue2, setSelectedValue2] = useState("");
  const {userExists} = useContext(LoginContext)
  //userExists.usuario

  const [companies, setCompanies] = useState([])
  const [locations,setLocations] = useState([
    {locdescri:"Locación 1",
    loccodigo:"1"
    },
    {locdescri:"Locación 2",
    loccodigo:"2"
    },
    {locdescri:"Locación 3",
    loccodigo:"3"
    }
  ])

  useEffect(() => {
    const getCompanies= async()=>{
      const options = {
        method: 'POST',
        body: JSON.stringify(userExists.usuario),
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      }

      try{
        let response = await fetch("login/companias_del_usuario",options)

        response = await response.json()
        setCompanies(response.data)
        console.log(response.data)

      }catch(e){
        throw new Error("No se encontro nada")
      }
    }

    const getLocations= async()=>{
      const options = {
        method: 'POST',
        body: JSON.stringify(userExists.usuario),
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      }

      try{
        fetch("login/get_localidad",options)

      }catch(e){
        throw new Error("No se encontro nada")
      }
    }



    getCompanies()

    
  
  }, [])
  

  const handleChange1 = (event) => {
    console.log(event.target.value);
    setSelectedValue1(event.target.value);
  };

  const handleChange2 = (event) => {
    console.log(event.target.value);
    setSelectedValue2(event.target.value);
  };

  const handleSubmit = async(event) => {
    event.preventDefault();

    // implentation of jwt
    navigate("/productos",{replace:true})

  }

  return (
    <Container maxWidth={false} style={{ height: "100vh" }} justify="center">
      <Grid
        container
        justifyContent="center"
        alignItems="center"
        style={{ height: "100%" }}
      >
        <Grid item xs={12} sm={8} md={6} lg={4}>
          <Paper elevation={3} style={{ padding: "32px" }}>
            <div className={classes.paper}>
              <Grid container justifyContent="flex-start" alignItems="center">
                <Grid item style={{ paddingBottom: "20px" }}>
                  <img
                    src={loginImages.logoSmall}
                    alt="Logo de la empresa"
                    className={classes.img}
                  />
                </Grid>
                <Typography
                  component="h1"
                  variant="h5"
                  style={{ fontWeight: "bolder", fontSize: "15px" }}
                >
                  FUTURESOFT
                </Typography>
              </Grid>

              <form className={classes.form} onSubmit = {handleSubmit}>
                <TextField
                  variant="outlined"
                  margin="normal"
                  required
                  fullWidth
                  id="email"
                  label="Usuario"
                  name="email"
                  value={"fixed"}
                  disabled
                />
                <TextField
                  variant="outlined"
                  label="Contraseña"
                  type="password"
                  margin="normal"
                  required
                  fullWidth
                />
                <Grid item justifyContent="center">
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "column",
                      alignItems: "center",
                      marginTop: "30px",
                    }}
                  >
                    <InputLabel id="compania">Compañia</InputLabel>
                    <Select
                      value={selectedValue1}
                      onChange={handleChange1}
                      className={classes.combobox}
                      labelId="compania"
                      style={{
                        width: "100%",
                        paddingTop: "10px",
                        textAlign: "center",
                      }}
                    >
                      <MenuItem value="">-- Seleccione una opción --</MenuItem>
                      {companies.map((company) => (
              <MenuItem key={company.loccodigo} value={company.cliciacianombre}>
                {company.cliciacianombre}
              </MenuItem>
            ))}
                    </Select>
                  </div>
                </Grid>

                <Grid item>
                  <div
                    style={{
                      display: "flex",
                      flexDirection: "column",
                      alignItems: "center",
                    }}
                  >
                    <InputLabel id="localidad">Localidad</InputLabel>
                    <Select
                      value={selectedValue2}
                      onChange={handleChange2}
                      className={classes.combobox}
                      labelId="localidad"
                      style={{
                        width: "100%",
                        paddingTop: "10px",
                        textAlign: "center",
                      }}
                    >
                      <MenuItem value="">-- Seleccione una opción --</MenuItem>
                      {locations.map((location) => (
              <MenuItem key={location.cliciaciacodigo} value={location.locdescri}>
                {location.locdescri}
              </MenuItem>
            ))}
                    </Select>
                  </div>
                </Grid>
                {/* <Grid item>
          <Select value={selectedValue} onChange={handleChange}>
            {options.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </Select>
        </Grid> */}
                <Button
                  type="submit"
                  fullWidth
                  variant="contained"
                  color="primary"
                  className={classes.submit}
                >
                  Ver dashboard
                </Button>
              </form>
            </div>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default LoginInner;
