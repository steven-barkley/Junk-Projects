import './App.css';
import { animals } from './animals';
import { navBar } from './animals';
import ReactDOM from 'react-dom';
import React from 'react';

const background = <img class="background" alt="ocean" src="/images/ocean.jpg" />;

const title = "Click an animal for a fun fact";

const animalFacts = (
  <div>
    <h1>{ title }</h1>
    { background }
  </div>
);

title === "" ? "Click an animal for a fun fact" : title

const images = [];

function App() {
  return (
    <div className="App">
      <p>Test { title }</p>
    </div>
  );
}

export default App;
