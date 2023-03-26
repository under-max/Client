import React,{useState} from 'react';
import ExpenseDate from './ExpenseDate';
import './ExpenseItem.css'
import Card from '../UI/Card';

const ExpenseItem = (expense) => {
    
    const [title, setTitle] = useState(expense.title); //현재상태와 업데이트 하는 함수
    
    const clickHandler =()=> {
        setTitle('updated!');
    }


    return (
        <Card className='expense-item'>
            <ExpenseDate date={expense.date}/>
            <div className='expense-item__description'>
                <h2>{title}</h2>
                <div className='expense-item__price'>${expense.amount}</div>
            </div>
            <button onClick={clickHandler}>Change Title</button>
        </Card>
    );
};

export default ExpenseItem;