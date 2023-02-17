import React from "react";
import { Link } from "react-router-dom";
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

const Recoverpw = () => {
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
                    <Link to="/auth-lock-screen" className="logo logo-admin">
                      <img src={logo} height="24" alt="logo" />
                    </Link>
                  </div>
                </div>

                <CardBody className="p-4">
                  <div className="p-3">
                    <div className="alert alert-success mt-5" role="alert">
                      Ingrese su usuario para acceder al sistema!
                    </div>

                    <Form className="mt-4" action="auth-lock-screen">
                      <div className="mb-3">
                        <Label htmlFor="user">Usuario</Label>
                        <Input
                          type="text"
                          className="form-control"
                          id="user"
                          placeholder="Ingrese su usuario"
                        />
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

export default Recoverpw;
