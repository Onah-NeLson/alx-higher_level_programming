#!/usr/bin/node
// adding a new function incr that increments the integer value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  myObject.value += 1;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
