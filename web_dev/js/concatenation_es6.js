// You can also concatenate different arrays of objects together using a ... notation.
// This script was inspired by the freeCodeCamp Javascript workshop: www.youtube.com/watch?v=5MPHo5jGXwQ

// Author: Alex Nakagawa

let names =         ['Alex', 'Bob', 'Carl'];
let moreNames =     ['Danielle', 'Edna'];
let evenMoreNames = ['Forrest'];

let allNames = [...names, 
				...moreNames,
				...evenMoreNames
];

console.log(allNames)