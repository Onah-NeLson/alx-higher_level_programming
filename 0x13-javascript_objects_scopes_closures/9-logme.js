#!/usr/bin/node
// hands on javascript objs

let narg = 0;

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
