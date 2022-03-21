import React from "react";
// react plugin used to create switch buttons
import Switch from "react-bootstrap-switch";
// plugin that creates slider
import Slider from "nouislider";

// reactstrap components
import {
  Button,
  Label,
  FormGroup,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Container,
  Row,
  Col,
} from "reactstrap";
import { MainView } from "../Components/filter";



function BasicElements() {

  return (
    <>
     <MainView />
    </>
  );
}

export default BasicElements;


/*
function Filters() {
  return (
    <div className="section section-basic" id="basic-elements">
      <Container>
        <h3 className="title">Basic Elements</h3>
        <div className="space-70"></div>
        <div id="inputs">
          <h4>Inputs</h4>
          <p className="category">Form Controls</p>
          <Row>
            <Col lg="3" sm="6">
              <FormGroup>
                <Input
                  defaultValue=""
                  placeholder="Regular"
                  type="text"
                ></Input>
              </FormGroup>
            </Col>
            <Col lg="3" sm="6">
              <FormGroup className="has-success">
                <Input
                  className="form-control-success"
                  defaultValue="Success"
                  type="text"
                ></Input>
              </FormGroup>
            </Col>
            <Col lg="3" sm="6">
              <FormGroup className="has-danger">
                <Input
                  className="form-control-danger"
                  defaultValue="Error Input"
                  type="email"
                ></Input>
              </FormGroup>
            </Col>
            <Col lg="3" sm="6">
              <InputGroup >
                <InputGroupAddon addonType="prepend">
                  <InputGroupText>
                    <i className="fa fa-user-circle"></i>
                  </InputGroupText>
                </InputGroupAddon>
                <Input
                  placeholder="Left Font Awesome Icon"
                  type="text"
                ></Input>
              </InputGroup>
            </Col>
            <Col lg="3" sm="6">
              <InputGroup>
                <Input
                  placeholder="Right Nucleo Icon"
                  type="text"
                ></Input>
                <InputGroupAddon addonType="append">
                  <InputGroupText>
                    <i className="now-ui-icons users_single-02"></i>
                  </InputGroupText>
                </InputGroupAddon>
              </InputGroup>
            </Col>
          </Row>
        </div>
      </Container>
    </div>
  );
}

export default Filters;
*/