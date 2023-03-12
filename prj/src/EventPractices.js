import React, { useState } from "react";

const EventPracetices =()=>{

// const [username, setUsername] = useState('');
// const [message, setMessage] = useState('');

const [form, setFrom] = useState({
    username: '',
    message: ''
})

const {username, message} = form

const onChange =e=>{
    const nextForm = {
        ...form, 
        [e.target.name]: e.target.value
    };
    setFrom(nextForm)
}
// const onChangeUserName = e => setUsername(e.target.value);
// const onChangeMessage = e => setMessage(e.target.value);
const onClick = () => {
    alert(username + ": " + message);
    // setUsername('');
    // setMessage('');
    setFrom({username: '', message: ''});
}; 
const onKeyDown =(e)=>{
    if(e.key === 'Enter'){
        onClick();
    }
}
    return(
        <div>
            <h1>이벤트 연습</h1>
            <input type="text"
            name="username"
            placeholder="사용자명"
            value={username}
            onChange={onChange} />

            <input type="text"
            name="message"
            placeholder="아무거나 입력하세요"
            value={message}
            onChange={onChange}
            onKeyDown={onKeyDown} />
            
            <button onClick={onClick}>클릭</button>
        </div>
    );
}

export default EventPracetices;