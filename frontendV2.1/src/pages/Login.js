import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import {
  TextField,
  Button,
  Paper,
  Typography,
  Grid,
} from "@material-ui/core";

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
  },
}));

const Login = () => {
  const classes = useStyles();
  const [email, setEmail] = useState("");

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
        console.log(response.status);
        //navigate('/auth-lock-screen')
      }
      

    }catch(err){
      if(err instanceof Error){
        console.error(err)
      }
      console.error(err)

    }
  };

  return (
    <Grid  container justifyContent="center">
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <form className={classes.form} onSubmit={handleSubmit}>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
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
              Sign In
            </Button>
          </form>
        </div>
      </Grid>
    </Grid>
  );
};

export default Login;
