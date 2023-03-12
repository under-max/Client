
const Hello = (props) => {
    Hello.defaultProps = {
        name: "이름없음",
    }
    return(
        <div>
            안녕하세요 {props.name}
        </div>
    );
}

export default Hello;