import React, {Component} from 'react';
import PropTypes from 'prop-types';


class MyComponents extends Component {
    render(){
    const {name, favoriteNumber, children} = this.props;
    return(
        <div>
        <h1>My name is {name}<br />
            children value is {children}<br />
            My favorite Number is {favoriteNumber}
        </h1>
    </div>
    );
    }
}

// const MyComponents =({name, favoriteNumber, children})=> {
    
//     return(
//     <div>
//         <h1>My name is {name}<br />
//             children value is {children}<br />
//             My favorite Number is {favoriteNumber}
//         </h1>
//     </div>
//     );
// };

MyComponents.defaultProps = {
    name: "Vue?"
}

MyComponents.propTypes = {
    name:PropTypes.string,
    favoriteNumber: PropTypes.number.isRequired
}
export default MyComponents;
