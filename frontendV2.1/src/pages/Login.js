import React, { useContext, useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  TextField,
  Button,
  Paper,
  Typography,
  Grid,
  Container
} from "@material-ui/core";
//My assests
import loginImages from "../helpers/login/getImgs"
import { LoginContext } from "../contexts/LoginContext";
import { useNavigate } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  root: {
    height: "100vh",
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
    backgroundColor:"#406AF5"
  },

  img:{ width: '50px', 
  height: '50px', 
  marginRight:"8px"
  },
}));

const Login = () => {
  const classes = useStyles();
  const navigate = useNavigate()
  const [email, setEmail] = useState("");
  const{setUserExists} = useContext(LoginContext)

  const handleSubmit = async(event) => {
    event.preventDefault();

    //validate if user exists in the db
    try{
      if(!email.match(/[^\s@]+@[^\s@]+/gi)){
        throw new Error("Ese usuario no está registrado")
      }

      const options = {
        method: 'POST',
        body: JSON.stringify({
          user: email
          //user: "\u00adv}xg@Practi"
        }),
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      }

      let response = await fetch("login/usuario_existe",options)
      response = await response.json()
      console.log(response)

      if (response.status === "ok"){
        setUserExists(response)
        console.log(response.status);
        navigate('/loginInner',{replace:true})
      }
      

    }catch(err){
      if(err instanceof Error){
        console.error(err)
      }
      console.error(err)

    }
  };

  return (

    <Container maxWidth={false} style={{ height: '100vh' }} justify="center" >
      <Grid container justifyContent="center" alignItems="center" style={{ height: '100%' }}>
        <Grid item xs={12} sm={8} md={6} lg={4}>
          <Paper elevation={3} style={{ padding: '32px' }}>
          <div className={classes.paper} >

        <Grid container justifyContent="flex-start" alignItems="center" >
          <Grid item style={{ paddingBottom: '20px' }}>
          <img src={loginImages.logoSmall} alt="Logo de la empresa" className={classes.img} />
          </Grid>         
          <Typography component="h1" variant="h5" style={{fontWeight:"bolder", fontSize:"15px"}}>
            FUTURESOFT
          </Typography>
        </Grid>

        <Typography component="h1" variant="h5" style={{fontWeight:"bolder"}}>
          Iniciar sesión
        </Typography>
        <form className={classes.form} onSubmit={handleSubmit}>
          <TextField
            variant="outlined"
            margin="normal"
            required
            fullWidth
            id="email"
            label="Usuario"
            name="email"
            autoComplete="email"
            autoFocus
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Iniciar sesión
          </Button>
        </form>
      </div>
          </Paper>
        </Grid>
      </Grid>
    </Container>
    
  );
};

export default Login;
