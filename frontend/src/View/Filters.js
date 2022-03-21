
function Filters(){
  return(
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
                <InputGroup className={leftFocus ? "input-group-focus" : ""}>
                  <InputGroupAddon addonType="prepend">
                    <InputGroupText>
                      <i className="fa fa-user-circle"></i>
                    </InputGroupText>
                  </InputGroupAddon>
                  <Input
                    placeholder="Left Font Awesome Icon"
                    type="text"
                    onFocus={() => setLeftFocus(true)}
                    onBlur={() => setLeftFocus(false)}
                  ></Input>
                </InputGroup>
              </Col>
              <Col lg="3" sm="6">
                <InputGroup className={rightFocus ? "input-group-focus" : ""}>
                  <Input
                    placeholder="Right Nucleo Icon"
                    type="text"
                    onFocus={() => setRightFocus(true)}
                    onBlur={() => setRightFocus(false)}
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
  );
}
