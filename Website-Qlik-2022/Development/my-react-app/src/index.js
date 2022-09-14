// import React from 'react';
import ReactDOM from 'react-dom/client';

// class is initialized
class Car {
  constructor( name ) {
    // class property is set
    this.brand = name;
  }
  present() {
    return 'I have a ' + this.brand;
  }
}

class Model extends Car {
  constructor( name, mod ) {
    super( name );
    this.model = mod;
  }
  show() {
    return this.present() + ', it is a ' + this.model + '.'
  }
}
const myCarMakeModel = new Model( "Ford", "Mustang" );
myCarMakeModel.show();

// class instance is initialized
// const myCar = new Car( "Ford" );

// const myFirstElement = <h1>Hello React!</h1>

const root = ReactDOM.createRoot( document.getElementById( 'root' ) )
// class property is rendered in the DOM
root.render( myCarMakeModel.show() );
