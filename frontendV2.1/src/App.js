import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Productos from "./pages/Productos";
import Inicio from "./pages/Inicio";
import LoginInner from "./pages/LoginInner";
import { LoginContextLayout } from "./contexts/LoginContext";

function App() {
  return (
    <Router>
      <Routes>
        <Route element = {<LoginContextLayout/>}>
          <Route path="/login" element={<Login />} />
          <Route path="/loginInner" element={<LoginInner />} />
        </Route>
        <Route path="/productos" element={<Productos />} />
        <Route path="/inicio" element={<Inicio />} />
      </Routes>
    </Router>
  );
}

export default App;
