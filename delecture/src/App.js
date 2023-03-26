// /*eslint-disable*/ waring 삭제
import { useState } from 'react';
import './App.css';
import Modal from './Components/Modal';
function App() {

  
  const [글제목, 글제목변경] = useState(['남자 코트 추천', '강남 우동 맛집', '파이썬 독학']);
  const [따봉, 따봉변경] = useState([0,0,0]);
  
  const [modal, setModal] = useState(false);
  const [title, setTitle] = useState(0);
  

  

  return (
    <div className="App">
      <div className='black-nav'>
        <h4>Blog</h4>
      </div>

      {/* <button onClick={()=>{
        let copy = [...글제목];
        copy[0] = '여자 코트 추천'
        글제목변경(copy);
      }}>제목 바꾸기</button> */}
      {/* <button onClick={()=>{
        글제목.sort();
        const copy = [...글제목];
        글제목변경(copy);
      }}>가나다순 정렬!</button> */}
      {/* <div className='list'>
        <h4 onClick={()=>
          modal === false ? setModal(true) : setModal(false)}>{글제목[0]} <span onClick={함수}>👍</span> {따봉} </h4>
        <p>2월 17일 발행</p>
      </div>
      <div className='list'>
        <h4>{글제목[1]}</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className='list'>
        <h4>{글제목[2]}</h4>
        <p>2월 17일 발행</p>
      </div> */}
      
      {
        글제목.map((a,i)=>{
          
          return (<div className='list' key={i}>
          <h4 onClick={()=>{
            modal === false ? setModal(true) : setModal(false);
            setTitle(i)
            console.log(i);
            console.log(글제목[i])
          }}>{a} </h4>
          <h4><span onClick={()=>{
            let copy = [...따봉]
            copy[i] = 따봉[i] + 1;
            따봉변경(copy);
          }}>👍</span>{따봉[i]}</h4>
          <p>2월 17일 발행</p>
        </div>)
        })
      }

      {
        modal === true ? <Modal value={글제목} titleState={글제목변경} changeTitle={title}/> : null
      }

    </div>
  );
}

export default App;
