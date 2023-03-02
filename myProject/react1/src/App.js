import './App.css';

const Subject =(props)=>{
  return(
    <header>
        <h1>{props.title}</h1>
        <h3>{props.dec}</h3>
    </header>
  );
}

const Toc = (props) => {
  return(
    <nav>
        <ol>
          <li><a href='1.html'>{props.title}</a></li>
          
        </ol>
    </nav>
  );
}

const Content = (props) => {
  return(
    <article>
        <h1>{props.title}</h1>
        <h4>{props.dec}</h4>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Velit ab dignissimos accusantium accusamus earum voluptatum veniam, ratione harum quos commodi? Eligendi aliquid sint ad eaque. Tenetur omnis praesentium asperiores maiores.</p>
      </article>
  );
}

function App() {
  const content = [
    {id:1, title:"HTML", desc:"Html is for information"},
    {id:2, title:"Css", desc:"JavaScript is for design"},
    {id:3, title:"JavaScript", desc:"JavaScript is for interaction"},
  ];
  return (
    <div className="App">
      <Subject title="React Practice" dec="World Wide Web"></Subject>
      
      <Toc title = {content.title} desc = {content.desc}/>
      <Content title="Welcome" dec="Hello Web"/>
      
    </div>
  );
}

export default App;
