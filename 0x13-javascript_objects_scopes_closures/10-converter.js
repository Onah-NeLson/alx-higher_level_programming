 #!/usr/bin/node
// hannds on javascript objs
exports.converter = function (base) {
  return function (number) {
    return (number >>> 0).toString(base);
  };
};
