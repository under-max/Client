import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './App.css';
import SignUp from './views/SignUp/SignUp';

function App() {
const [connection, setConnection] = useState<String>('');

const connectionTest = () =>{//spring에서 get으로 받고있음
  axios.get('http://localhost:4000/').then((response) => {
    setConnection(response.data);
  }).catch((error)=>{
    setConnection(error.message);
  })
}

useEffect(()=>{
  connectionTest();
},[]); //맨처음 한번만 실행


  return (
    <div className="App">
      <p>{connection}</p>
      <SignUp />
    </div>
  );
}

export default App;
