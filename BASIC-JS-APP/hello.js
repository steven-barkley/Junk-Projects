'user strict';

// Focuses variables in Javascript

var name, age, height, location, eyecolor, haircolor; 

name = "Steven Barkley";
age = 35;
height = 6.45;
location_state = "Alaska";
eyecolor = "brown";
haircolor = "darkbrown";
person = true;
/*
break, case, catch, continue, debugger, default, delete, 
do, else, false, finally, for, function, if, in, instanceof, 
new, null, return, switch, this, throw, true, try, typeof, var, 
void, while, with */ 

var myText = "My name is "+name+" I am " + age + " years old and is " + height + 
    " feet tall, he lives in " + location_state + ". He has " + eyecolor + " eyes " +
    " and " + haircolor +  " hair.";

function changeContent( button, content) {
    button.text(content)
};

$(document).ready( function()
{ 
    $('.myDiv').text(myText);
    
    $('button').text("this is a button");

    $('#thisButton').click(function()
    {
        changeContent( $(this) , " Javascript Yeahhh!");
    }    
);
});
