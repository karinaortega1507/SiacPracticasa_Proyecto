import React from "react";
// Formik Validation
import * as Yup from "yup";
import { useFormik } from "formik";

import { useNavigate, Link } from "react-router-dom";
import {
  Card,
  CardBody,
  Col,
  Container,
  Form,
  Input,
  Label,
  Row,
} from "reactstrap";

// import images
import logo from "../../assets/images/logo-sm.png";

const Login = () => {
  const url = 'http://localhost:7000/grupos/1';
  const navigate = useNavigate();
  const validation = useFormik({
    // enableReinitialize : use this flag when initial values needs to be changed
    enableReinitialize: true,

    initialValues: {
      email: '',
    },
    validationSchema: Yup.object({
      email: Yup.string().required("Ingrese su usuario"),
    }),
    onSubmit:  (values) => {
      console.log(values);
      sendEmail(values)
      navigate('/auth-lock-screen')
      //enviar los datos a la api
    }
  });
  const opciones = {
    method: 'GET',
    headers: new Headers({
      'Content-Type': 'application/json'
    }),
    //body: JSON.stringify(email)
  };
  const sendEmail=  () =>{
    fetch(url, opciones)
    .then(response => {
      if (response.ok) {
        console.log('Datos enviados exitosamente', response);
      } else {
        throw new Error('Error al enviar datos');
      }
    })
    .catch(error => console.error(error));
  }
  document.title = "Ingreso de usuario | Practicasa";
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
                          type="email"
                          className="form-control"
                          id="email"
                          onChange={validation.handleChange}
                          onBlur={validation.handleBlur}
                          value={validation.values.email || ""}
                          invalid={
                            validation.touched.email && validation.errors.email ? true : false
                          }
                        />
                        {validation.touched.email && validation.errors.email ? (
                          <FormFeedback type="invalid">{validation.errors.email}</FormFeedback>
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
