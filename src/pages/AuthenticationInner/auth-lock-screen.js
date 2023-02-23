import React, { useState, useEffect } from "react";
import {axios} from "axios";

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
  //endpoint que retorna los datos de las empresas a las que pertenece el usuario
  const API_URL = "http://127.0.0.1:5000/loguin/companias_del_usuario";
  const navigate = useNavigate();
  const [more_Menu, setmore_Menu] = useState(false)
  const [more_locate, setmore_locate] = useState(false)
  const [selectedOption, setSelectedOption] = useState(null);
  const [selectedOptionLocate, setSelectedOptionLocate] = useState(null);
  const [optionsBusiness, setOptionsBusiness] = useState([]);
  const [optionsLocate, setOptionsLocate] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  /* const data = {
    cliciausu: localStorage.getItem("cliciausu"),
    cliciagrupo: localStorage.getItem("cliciagrupo")
  } */
  //Debe venir el nombre del cliente y el usuario
  const name = "Jorge López";
  const user = "jlopez";
  const data ={
    cliciausu: "­v}xg",
    cliciagrupo:"Practi"
  }
  const localidades = [
      {
        sucursal:"gye", 
        localidad:"01"
      },
      {
        sucursal:"uio",
        localidad:"02"
      }]
  
  // Se realiza la petición a la API para obtener las empresas y llenar con las opciones el Dropdown
  useEffect(() => {
      fetch(API_URL, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        }
      })
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        console.log(data);
        if (data.status === "ok"){
          console.log(data.status);
          setOptionsBusiness(data.data); 
          console.log(optionsBusiness);
        }
      })
      .catch(function(error) {
        console.error(error);
      });
      setOptionsLocate(localidades)
  },[])
 
  //Obtener las localidades
  /* useEffect(() => {
    axios
      .post(API_URL,data)
      .then(response => {
          setOptionsLocate(response.data.map(option => ({
            loccodigo: option.loccodigo,
            name: option.name,
          })));
        })
        .finally(() => {
          // Cambiar el estado de carga
          setIsLoading(false);
        });
    
  },[]);  */

  const validation = useFormik({
    // enableReinitialize : use this flag when initial values needs to be changed
    enableReinitialize: true,
    initialValues: {
      password: ''    
    },
    validationSchema: Yup.object({
      password: Yup.string().required("Ingrese su contraseña"),
      /* business: Yup.mixed().oneOf(optionsBusiness).required('Debe seleccionar una opción.'),
      locate: Yup.mixed().oneOf(optionsLocate).required('Debe seleccionar una opción.'), */
    }),
    onSubmit: (values) => {
      console.log(values.password);
      console.log(selectedOption);
      console.log(selectedOptionLocate);
      const business = optionsBusiness.find((business) => business.cliciacianombre === selectedOption);
      const locate = optionsBusiness.find((locate) => locate.localidad === selectedOptionLocate);
      console.log("Empresa seleccionada",business);
      console.log("Localidad seleccionada",locate);
      navigate('/tables-datatable')
      //enviar los datos a la api
    }
  });
  document.title = "Ingreso de usuario | Contraseña";
  //opción seleccionada en el dropdown de empresa
  const handleOptionClick = (option) => {
    setSelectedOption(option);
  };
  const handleOptionClickLocate = (option) => {
    setSelectedOptionLocate(option);
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
                      Bienvenido {user}, ingresa tu contraseña!
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
                        
                        <h6 className="font-size-16 mt-3">{name}</h6>
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
                              { optionsBusiness.map(option => (
                                <DropdownItem 
                                key={option.cliciaciacodigo} 
                                onClick={() => handleOptionClick(`${option.cliciacianombre}`)} required>{option.cliciacianombre}</DropdownItem>
                              )) }
                               
                            {/* <DropdownItem onClick={() => handleOptionClick("Practicasa")}>Practica</DropdownItem>
                            <DropdownItem onClick={() => handleOptionClick("Mercatti")}>Mercatti</DropdownItem> */}
                          </DropdownMenu>
                        </Dropdown>                  
                      </div>
                      <div className="mb-3">
                        <Dropdown
                          isOpen={more_locate}
                          toggle={() => {
                            setmore_locate(!more_locate)
                          }}
                          className="btn-group me-2 mb-2 mb-sm-0"
                        >
                          <DropdownToggle
                            className="btn btn-primary waves-light waves-effect dropdown-toggle"
                            tag="div"
                          >
                            {selectedOptionLocate ? selectedOptionLocate : "Seleccione una localidad"} 
                            <i className="mdi mdi-chevron-down ms-1"></i>
                          </DropdownToggle>
                          <DropdownMenu>
                          { optionsLocate.map(option => (
                                <DropdownItem 
                                key={option.sucursal} 
                                onClick={() => handleOptionClickLocate(`${option.localidad}`)} required>{option.localidad}</DropdownItem>
                              )) }
                           {/*  <DropdownItem onClick={() => handleOptionClickLocate("01")} required>01</DropdownItem>
                            <DropdownItem onClick={() => handleOptionClickLocate("02")} required>02</DropdownItem> */}
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
