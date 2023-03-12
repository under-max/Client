import React,{ useState } from "react";


const Counter =(props)=>{
    const [number, setNumber] = useState(0); //0은 시작값
    
    const increase=()=>{
        setNumber(prevNumber => prevNumber + 1);
    }
    const decrease=()=>{
        setNumber(prevNumber => prevNumber - 1);
    }
    return(
        <div>
            <h1>{number}</h1>
            <button onClick={increase}>+1</button>
            <button onClick={decrease}>-1</button>
        </div>
    );
}

export default Counter;