// This script was inspired by the freeCodeCamp Javascript workshop: www.youtube.com/watch?v=5MPHo5jGXwQ

// Author: Alex Nakagawa



// 1. Concatenation of Arrays
// You can also concatenate different arrays of objects together using a ... notation.
let names =         ['Alex', 'Bob', 'Carl'];
let moreNames =     ['Danielle', 'Edna'];
let evenMoreNames = ['Forrest'];

let allNames = [...names, 
				...moreNames,
				...evenMoreNames
];
console.log(allNames)

// 2. Embed Javascript directly inline with strings
const s = `Hi my name is ${names[0]}`
console.log(s)