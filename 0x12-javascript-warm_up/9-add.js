#!/usr/bin/node
// This script prints the addition of 2 integers
function add (a, j) {
  console.log(a + j);
}

let firstArg = process.argv[2];
let secondArg = process.argv[3];

firstArg = parseInt(firstArg);
secondArg = parseInt(secondArg);

add(firstArg, secondArg);
