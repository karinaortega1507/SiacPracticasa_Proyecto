import { createContext, useState } from 'react';
import {Outlet} from "react-router-dom"

const LoginContext = createContext()
const LoginContextProvider = ({children})=>{
  const [userExists, setUserExists] = useState({})
  const myContextData = { 
    userExists,
    setUserExists
  };
  return (
    <LoginContext.Provider value={myContextData}>
      {children}
    </LoginContext.Provider>
  );

}



const LoginContextLayout = () => {
    const [userExists, setUserExists] = useState({})
  const myContextData = { 
    userExists,
    setUserExists
  };

  return (
    <LoginContextProvider value={myContextData}>
      <Outlet/>
    </LoginContextProvider>
  );
};

export {LoginContextLayout,LoginContext}
