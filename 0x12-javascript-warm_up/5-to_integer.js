#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const [,, arg] = process.argv;

const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
