import React, {useState} from "react";
import axios from "axios";
// Formik Validation
import * as Yup from "yup";
import { useFormik } from "formik";

import { useNavigate, Link } from "react-router-dom";
import {
  Alert,
  Card,
  CardBody,
  Col,
  Container,
  Form,
  FormFeedback,
  Input,
  Label,
  Row,
} from "reactstrap";

// import images
import logo from "../../assets/images/logo-sm.png";

const BASE_URL = process.env.REACT_APP_API;
//http://127.0.0.1:5000/loguin/usuario_existe 
const Login = () => {
  const API_URL = BASE_URL + 'login/usuario_existe';
  const navigate = useNavigate();
  document.title = "Ingreso de usuario | Practicasa";
  const validation = useFormik({
    // enableReinitialize : use this flag when initial values needs to be changed
    enableReinitialize: true,
    initialValues: {
      text: '',
    },
    validationSchema: Yup.object({
      text: Yup.string().required("Ingrese su usuario"),
    }),
   
    onSubmit: function(values) {
      console.log(JSON.stringify(values.text));
      localStorage.setItem("usuario", values.text);
      fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify({
          user: values.text
          //user: "\u00adv}xg@Practi"
        }),
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      })
      .then(function(response) {
        console.log(response.json)
        return response.json();
      })
      .then(function(data) {
        console.log(data);
        if (data.status === "ok"){
          console.log(data.status);
          navigate('/auth-lock-screen')
        }
      })
      .catch(function(error) {
        console.error(error);
      });
    }

  });
  


  return (
    <React.Fragment>
      <div className="account-pages my-5 pt-5">
        <Container>
          <Row className="justify-content-center">
            <Col md={8} lg={6} xl={4}>
              <Card className="overflow-hidden">
                <div className="bg-primary">
                  <div className="text-primary text-center p-4">
                    <h5 className="text-white font-size-20 p-2">
                      Ingrese su usuario
                    </h5>
                    <Link to="" className="logo logo-admin">
                      <img src={logo} height="24" alt="logo" />
                    </Link>
                  </div>
                </div>

                <CardBody className="p-4">
                  <div className="p-3">
                    <div className="alert alert-success mt-5" role="alert">
                      Ingrese su usuario para acceder al sistema!
                    </div>

                    <Form className="mt-4"
                     onSubmit={(e) => {
                      e.preventDefault();
                      validation.handleSubmit();
                      return false;
                    }}>
                      <div className="mb-3">
                        <Label htmlFor="email">Usuario</Label>
                        <Input
                          type="text"
                          className="form-control"
                          id="text"
                          placeholder="Ingrese su correo"
                          onChange={validation.handleChange}
                          onBlur={validation.handleBlur}
                          value={validation.values.text}
                          invalid={
                            validation.touched.text && validation.errors.text ? true : false
                          }
                        />
                        {validation.touched.text && validation.errors.text ? (
                          <FormFeedback type="invalid">{validation.errors.text}</FormFeedback>
                        ) : null}
                      </div>
                      <div className="row mb-0">
                        <Col xs={12} className="text-end">
                          <button
                            className="btn btn-primary w-md waves-effect waves-light"
                            type="submit"
                          >
                            Ingresar
                          </button>
                        </Col>
                      </div>
                    </Form>
                  </div>
                </CardBody>
              </Card>

              <div className="mt-5 text-center">
                <p>
                  ¿No recuerda el usuario?{" "}
                  <Link
                    to=""
                    className="fw-medium text-primary"
                  >
                    {" "}
                    Contáctese con el administrador{" "}
                  </Link>{" "}
                </p>
                <p className="mb-0">
                  © {new Date().getFullYear()} Practicasa. Creado con {" "}
                  <i className="mdi mdi-heart text-danger"></i> por Digotec
                </p>
              </div>
            </Col>
          </Row>
        </Container>
      </div> </React.Fragment>
  );
};

export default Login;
