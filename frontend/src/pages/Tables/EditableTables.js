import React, { useState, useEffect } from "react";
import { Row, Col, Card, CardBody, CardTitle } from "reactstrap";
// Editable
import BootstrapTable from "react-bootstrap-table-next";
import cellEditFactory from "react-bootstrap-table2-editor";

//Import Breadcrumb
import Breadcrumbs from "../../components/Common/Breadcrumb";
import "./datatables.scss";

/* const products = [
  { id: 1, age: 25, qty: 1500, cost: 1000 },
  { id: 2, age: 34, qty: 1900, cost: 1300 },
  { id: 3, age: 67, qty: 1300, cost: 1300 },
  { id: 4, age: 23, qty: 1100, cost: 6400 },
  { id: 5, age: 78, qty: 1400, cost: 4000 },
];

const columns = [
  {
    dataField: "id",
    text: "ID",
  },
  {
    dataField: "age",
    text: "Age(AutoFill)",
  },
  {
    dataField: "qty",
    text: "Qty(AutoFill and Editable)",
  },
  {
    dataField: "cost",
    text: "Cost(Editable)",
  },
]; */
const BASE_URL = process.env.REACT_APP_API
const EditableTables = () => {
  const API_URL = BASE_URL + "productos/obtener_productos"
  const [productos, setProductos] = useState([]);

  // Función para cargar los datos de los productos desde un API
  const cargarProductos =  () => {
    try {
      fetch(API_URL, {
        method: 'GET',
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
        if (data !== null){
          console.log(data);
          setProductos(data);
        }
      })
      .catch(function(error) {
        console.error(error);
      });
      
    } catch (error) {
      console.log(error);
    }
  };

  // Función para manejar los cambios en la columna "Cantidad de Etiquetas"
  const actualizarCantidadEtiquetas = (e, codigo) => {
    const nuevosProductos = [...productos];
    const indice = nuevosProductos.findIndex((p) => p.codigo === codigo);
    nuevosProductos[indice].cantidad_etiquetas = e.target.value;
    setProductos(nuevosProductos);
  };

   // Cargar los datos de los productos al montar el componente
   useEffect(() => {
    cargarProductos();
  }, []);

  // Definir las columnas personalizadas de la tabla
  const columnas = [
    {
      dataField: "codigo",
      text: "Código",
      sort: "asc",
      width: 150,
      
    },
    {
      dataField: "descripcion",
      text: "Descripción",
      sort: "asc",
      width: 270,
    },
    {
      dataField: "precio",
      text: "Precio",
      sort: "asc",
      width: 150,
    },
    {
      dataField: "medida",
      text: "Medida",
      sort: "asc",
      width: 250,
    },
    {
      dataField: "marca",
      text: "Marca",
      sort: "asc",
      width: 250,
    },
    {
      dataField: "linea",
      text: "Linea",
      sort: "asc",
      width: 250,
    },
    {
      dataField: "etiquetas",
      text: "Cantidad de etiquetas",
      sort: "asc",
      width: 100,
      //editable: true,
      // Función de devolución de llamada para manejar los cambios en la columna "Cantidad de etiquetas",
      //onCellEdit: (e, codigo) => actualizarCantidadEtiquetas(e, codigo),
    },
  ];

  document.title = "Consulta de Productos";
  return (
    <React.Fragment>
      <div className="page-content">
        <div className="container-fluid">
          <Breadcrumbs maintitle="FutureSoft" title="Practicasa" breadcrumbItem="Productos" />

          <Row>
            <Col className="col-12">
              <Card>
                <CardBody>
                  <CardTitle className="h4">Consulta de Productos </CardTitle>
                  <div className="table-responsive">
                    <BootstrapTable
                      keyField="id"
                      data={productos}
                      columns={columnas}
                      cellEdit={cellEditFactory({ mode: "click" })}
                    />
                  </div>
                </CardBody>
              </Card>
            </Col>
          </Row>
        </div>
      </div>
    </React.Fragment>
  );
};

export default EditableTables;
