#!/usr/bin/node
// This script computes and prints a factorial
function factorial (x) {
  if (isNaN(x) | x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}

console.log(factorial(process.argv[2]));
