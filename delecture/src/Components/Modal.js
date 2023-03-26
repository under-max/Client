import React from 'react';
import './Modal.css'

const Modal = (props) => {
    return (
        
        <div className='modal'>
            <h4>제목: {props.value[props.changeTitle]}</h4>
            <p>날짜: </p>
            <p>상세내용: </p>
            <button onClick={()=>{
                let copy = [...props.value]
                copy[0] = '여자 코트 추천'
                props.titleState(copy)
            }
            }>글 수정</button>
        </div>
        
    );
};

export default Modal;