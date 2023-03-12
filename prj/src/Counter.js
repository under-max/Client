import React, {Component} from "react";

class Counter extends Component {
   
        //state의 초깃값 설정 
        state = {
            number: 0,
            fixedNumber: 100
        };
    
    render(){
        const { number, fixedNumber } = this.state;
        return(
            <div>
                <h1>{number}</h1>
                <h1>{fixedNumber}</h1>
                <button onClick={() => {this.setState({number: number +1},()=>{console.log("1이더해짐");});}}>+1</button>
                <button onClick={() => {this.setState({number: number -1});}}>-1</button>                
            </div>
    );
  }
}

export default Counter;