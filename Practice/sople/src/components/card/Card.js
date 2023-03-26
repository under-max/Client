import React from 'react';
import './Card.css';

const Card = ({children}) => {
    return (
        <div className='Card__'>
            {children}
        </div>
    );
};

export default Card;