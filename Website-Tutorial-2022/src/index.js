import React from 'react';
// Need to inject component functions Greetings into the index.html root need to use//
import ReactDOM from 'react-dom';
//import './App.css';
// ReactDom uses a renderMethod ... used at end of file
//import './App.css';
// We can create functions however we like function() or arrow function => *//
// Stateless functional component
// JSX Rules
// div / Section / article or Fragment
// use camelCase for html attribute
// className instead of class
// Closs every element
// formatting


// function Greeting() {
//   return (
//     <div onClick>
//       <h1>Passing JSX into the root UI.</h1>
//       <ul>
//         <li href='#'>formatting</li>
//         <li href='#'>use camelCase for html attribute</li>
//         <li href='#'>div / Section / article or Fragment</li>
//         <li href='#'>className instead of class</li>
//       </ul>
//       <img src='' alt='' />
//       <input type='text' name='' id='' />
//     </div>
//   )
// }

// const Greeting_Complex = () => {
//   return React.createElement(
//     'div',
//     {},
//     React.createElement( 'h3', {}, 'Passing JSX into the Root UI the hard way' )
//   );
// };

//Pass the Greeting <JSX/> into the render method

// Nested Components, React Tools

// function Greeting() {
//   return (
//     <div>
//       <Person />
//       <Message />
//     </div>
//   )
// }

// const Person = () => <h1>Steven Barkley is a person</h1>
// const Message = () => <p>This is a message in JSX</p>

// ReactDOM.render( <Greeting />, document.getElementById( 'root' ) )

// //Pass JSX as <i></i> or <i/>

//CSS
// ./ mean same folder reference

//Setup vars
const firstBook = {
  img: 'https://images-na.ssl-images-amazon.com/images/I/71-zUutYfBL._UX300__PJku-sticker-v7,TopRight,0,-50_AC_UL127_SR127,127_.jpg',
  title: 'The Locked Door: A gripping psychological thriller with a jaw-dropping twist',
  author: 'Frieda McFadden'
}


function BookList() {
  return (
    <section >
      <Book
        img={ firstBook.img }
        title={ firstBook.title }
        author={ firstBook.author }
      />
      <Book title='developers guide' job="programmer" />
      <Book title='random title' number={ 22 } />
      <Book job='stripper' title='the space between' number={ 69 } />
    </section>
  );
}
const Book = ( props ) => {
  console.log( props )
  return (
    <article>
      <img src={ props.img } alt='' />
      <h1>{ props.title }</h1>
      <p>{ props.job }</p>
      <h4>{ props.author }</h4>

    </article>
  )
}

ReactDOM.render( <BookList />, document.getElementById( 'root' ) )

// //Pass JSX as <i></i> or <i/>