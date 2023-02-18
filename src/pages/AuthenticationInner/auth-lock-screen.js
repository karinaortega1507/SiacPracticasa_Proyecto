import React, { useState } from "react";

// Formik Validation
import * as Yup from "yup";
import { useFormik } from "formik";

import { useNavigate, Link } from "react-router-dom";

import { Container, 
  Row, 
  Col, 
  CardBody, 
  Card, 
  Form, 
  FormFeedback, 
  Input, 
  Dropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem, } from "reactstrap";


// import images
import logo from "../../assets/images/logo-sm.png";
import avatar from "../../assets/images/users/user-1.jpg";

const LockScreen = () => {
  const navigate = useNavigate();
  const [more_Menu, setmore_Menu] = useState(false)
  const [selectedOption, setSelectedOption] = useState("");
  const toggle = () => setDropdownOpen((prevState) => !prevState);
  const validation = useFormik({
    // enableReinitialize : use this flag when initial values needs to be changed
    enableReinitialize: true,

    initialValues: {
      password: '',
    },
    validationSchema: Yup.object({
      password: Yup.string().required("Ingrese su contraseña"),
    }),
    onSubmit: (values) => {
      console.log(values);
      navigate('/tables-datatable')
      //enviar los datos a la api
    }
  });
  document.title = "Ingreso de usuario | Contraseña";
  //opción seleccionada en el dropdown de empresa
  const handleOptionClick = (option) => {
    setSelectedOption(option);
  };
  return (
    <React.Fragment>
      <div className="account-pages my-5 pt-sm-5">
        <Container>
          <Row className="justify-content-center">
            <Col md="8" lg="6" xl="4">
              <Card className="overflow-hidden">
                <div className="bg-primary">
                  <div className="text-primary text-center p-4">
                    <h5 className="text-white font-size-20">Contraseña</h5>
                    <p className="text-white-50">
                      Bienvenido jgomez, ingresa tu contraseña!
                    </p>
                    <Link to="" className="logo logo-admin">
                      <img src={logo} height="24" alt="logo" />
                    </Link>
                  </div>
                </div>
                <CardBody className="p-4">
                  <div className="p-3">
                    <Form className="mt-4"
                      onSubmit={(e) => {
                        e.preventDefault();
                        validation.handleSubmit();
                        return false;
                      }}>

                      <div className="pt-3 text-center">
                        
                        <h6 className="font-size-16 mt-3">Jorge Gómez</h6>
                      </div>

                      <div className="mb-3">
                        <label className="form-label" htmlFor="userpassword">Contraseña</label>
                        <Input
                          name="password"
                          className="form-control"
                          placeholder="Enter password"
                          type="password"
                          id="password"
                          onChange={validation.handleChange}
                          onBlur={validation.handleBlur}
                          value={validation.values.password || ""}
                          invalid={
                            validation.touched.password && validation.errors.password ? true : false
                          }
                        />
                        {validation.touched.password && validation.errors.password ? (
                          <FormFeedback type="invalid">{validation.errors.password}</FormFeedback>
                        ) : null}
                         
                      </div> 
                      <div className="mb-3">
                        <Dropdown
                          isOpen={more_Menu}
                          toggle={() => {
                            setmore_Menu(!more_Menu)
                          }}
                          className="btn-group me-2 mb-2 mb-sm-0"
                        >
                          <DropdownToggle
                            className="btn btn-primary waves-light waves-effect dropdown-toggle"
                            tag="div"
                          >
                            {selectedOption ? selectedOption : "Seleccione una empresa"} 
                            <i className="mdi mdi-chevron-down ms-1"></i>
                          </DropdownToggle>
                          <DropdownMenu>
                            <DropdownItem onClick={() => handleOptionClick("Practicasa")}>Practica</DropdownItem>
                            <DropdownItem onClick={() => handleOptionClick("Mercatti")}>Mercatti</DropdownItem>
                          </DropdownMenu>
                        </Dropdown>                  
                      </div>
                      <div className="row mb-0">
                        <div className="col-12 text-end">
                          <button className="btn btn-primary w-md waves-effect waves-light" type="submit">Ingresar</button>
                        </div>
                      </div>

                    </Form>

                  </div>
                </CardBody>
              </Card>
              <div className="mt-5 text-center">
                <p>
                  ¿No eres tú? {" "}
                  <Link
                    to="/page-recoverpw"
                    className="fw-medium text-primary"
                  >
                    {" "}
                    Inicia sesión{" "}
                  </Link>{" "}
                </p>
                <p>
                  © 2023 Practicasa. Creado con {" "}
                  <i className="mdi mdi-heart text-danger" /> por Digotec
                </p>
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    </React.Fragment>
  );
};
export default LockScreen;
