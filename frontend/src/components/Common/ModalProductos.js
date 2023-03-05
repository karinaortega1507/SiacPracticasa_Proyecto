import React, { useState } from "react";

import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Modal,
  Container,
  ModalBody,
  ModalHeader,
  ModalFooter,
  Button,
} from "reactstrap";


const ModalProductos = () => {
    const [modal_standard, setmodal_standard] = useState(false);

    const removeBodyCss = () => {
        document.body.classList.add("no_padding");
      };

    const tog_standard = () => {
        setmodal_standard(!modal_standard);
        removeBodyCss();
      };
    const guardar_producto = () => {
        //llamada a la api para agregar producto a la proforma.
    }
    
    return(
        <React.Fragment>
            <div className="page-content">
                <Container fluid={true}>
                    <Row>   
                        <Col sm={6} md={4} xl={3}>
                            <div className="my-4 text-center">
                            <p className="text-muted">Standard modal</p>
                            <Button color="primary" onClick={tog_standard}> Standard modal </Button>
                            <Modal isOpen={modal_standard} toggle={tog_standard}>
                                <ModalHeader toggle={tog_standard}>Nombre del producto</ModalHeader>
                                <ModalBody>
                                <h5>Descripción del producto</h5>
                                <p>
                                    Cras mattis consectetur purus sit amet fermentum.
                                    Cras justo odio, dapibus ac facilisis in, egestas
                                    eget quam. Morbi leo risus, porta ac consectetur
                                    ac, vestibulum at eros.
                                </p>
                                <p>
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Vivamus sagittis lacus vel
                                    augue laoreet rutrum faucibus dolor auctor.
                                </p>
                                <p>
                                    Aenean lacinia bibendum nulla sed consectetur.
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Donec sed odio dui. Donec
                                    ullamcorper nulla non metus auctor fringilla.
                                </p>
                                <p>
                                    Cras mattis consectetur purus sit amet fermentum.
                                    Cras justo odio, dapibus ac facilisis in, egestas
                                    eget quam. Morbi leo risus, porta ac consectetur
                                    ac, vestibulum at eros.
                                </p>
                                <p>
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Vivamus sagittis lacus vel
                                    augue laoreet rutrum faucibus dolor auctor.
                                </p>
                                <p>
                                    Aenean lacinia bibendum nulla sed consectetur.
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Donec sed odio dui. Donec
                                    ullamcorper nulla non metus auctor fringilla.
                                </p>
                                <p>
                                    Cras mattis consectetur purus sit amet fermentum.
                                    Cras justo odio, dapibus ac facilisis in, egestas
                                    eget quam. Morbi leo risus, porta ac consectetur
                                    ac, vestibulum at eros.
                                </p>
                                <p>
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Vivamus sagittis lacus vel
                                    augue laoreet rutrum faucibus dolor auctor.
                                </p>
                                <p>
                                    Aenean lacinia bibendum nulla sed consectetur.
                                    Praesent commodo cursus magna, vel scelerisque
                                    nisl consectetur et. Donec sed odio dui. Donec
                                    ullamcorper nulla non metus auctor fringilla.
                                </p>
                                </ModalBody>
                                <ModalFooter>
                                <Button color="secondary" onClick={tog_standard}>
                                    Close
                                </Button>{' '}
                                <Button color="primary" onClick={guardar_producto}>
                                    Save changes
                                </Button>
                                </ModalFooter>
                            </Modal>
                            </div>
                        </Col>
                    </Row>
                </Container>
          </div>
        </React.Fragment>

       
    );
}

export default ModalProductos;