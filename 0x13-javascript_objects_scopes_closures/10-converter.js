#!/usr/bin/node
// hands on javascript objs

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
