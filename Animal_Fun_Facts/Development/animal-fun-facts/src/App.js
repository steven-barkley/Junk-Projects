import './App.css';
import { animals } from './animals';
import { navBar } from './animals';
import ReactDOM from 'react-dom';
import React from 'react';

function App() {
  return (
    <div className="App">
      <p> Does the { navBar } variable work in JSX?</p>

    </div>
  );
}

export default App;
