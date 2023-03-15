import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,Routes,Route} from "react-router-dom";
import Login from './pages/Login'
import Productos from './pages/Productos'
import Inicio from './pages/Inicio'

function App() {
  return (
    <Router>
       <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/productos" element={<Productos />} />
        <Route path="/inicio" element={<Inicio />} />
      </Routes>
    </Router>
  );
}

export default App;
