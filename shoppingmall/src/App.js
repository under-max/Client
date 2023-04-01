import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


import './App.css';
import { useState } from 'react';
import data from './data';
function App() {
  let [shoes] = useState(data);

  return (
    <div className="App">
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home" className='shop--header'>Shop</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#pricing">Cart</Nav.Link>
          </Nav>
        </Container>
      </Navbar>

      <div className='main-bg'></div>
      <Container>
        <Row>
          <Col sm>
            <img src="https://codingapple1.github.io/shop/shoes1.jpg" width="80%"></img>
            <h4>{shoes[0].title}</h4>
            <p>{shoes[0].content}</p>
          </Col>
          <Col sm>
          <img src="https://codingapple1.github.io/shop/shoes2.jpg" width="80%"></img>
            <h4>{shoes[1].title}</h4>
            <p>{shoes[1].content}</p>
          </Col>
          <Col sm>
            <img src="https://codingapple1.github.io/shop/shoes3.jpg" width="80%"></img>
            <h4>{shoes[2].title}</h4>
            <p>{shoes[2].content}</p>
          </Col>
        </Row>
      </Container>
    
    </div>
  );
}

export default App;
