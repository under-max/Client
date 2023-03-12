import React, {useState} from "react";

const CounterFunction =()=>{
    const [number, setCount] = useState(100)
    const onIncrease = () =>{
        setCount(number + 1)
    }
    const onDecreases = () =>{
        setCount(number - 1);
    }
    return(
        <div>
            <h1>{number}</h1>
            <button onClick={onIncrease}>+1</button>
            <button onClick={onDecreases}>-1</button>
        </div>
    );
}

export default CounterFunction;