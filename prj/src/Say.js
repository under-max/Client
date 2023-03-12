import React,{useState} from "react";

const Say =(props)=>{
    const [message, setMessage] = useState('');
    const [color, setColor] = useState('black')
    const onClickEnter = () => setMessage("안녕하세요");
    const onClickLeave = () => setMessage("안녕히 가세요");
    const changeStyle = () => setColor('blue');
    const {comment} = props;

    return(
        <div>
            <h1 style={{color}}>useState Check</h1>
            <button onClick={changeStyle}>Click me</button>
            <button onClick={onClickEnter}>입장</button>
            <button onClick={onClickLeave}>퇴장</button>
            <h1 style={{color}}>{message}</h1>
            <button style={{color:"red"}} onClick={()=>setColor('red')}>빨간색</button>
            <button style={{color:"blue"}} onClick={()=>setColor('blue')}>파란색</button>
            <button style={{color:"green"}} onClick={()=>setColor('green')}>녹색</button>
            <h1>{comment}</h1>
        </div>
    );
}

export default Say;