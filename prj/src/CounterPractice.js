import React, { useState } from "react";

const CounterPractice = () => {
    const [number, setCount] = useState(0);
    const numIncrease =()=> {setCount(number + 1);}
    const numDecrease =()=> {setCount(number - 1);}

    return(
        <div>
            <h1>{number}</h1>
            <button onClick={numIncrease}>클릭 +1</button>
            <button onClick={numDecrease}>클릭 -1</button>
        </div>
    );
}

export default CounterPractice;
