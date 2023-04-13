 #!/usr/bin/node
// hannds on javascript objs

exports.converter = function (base) {
  return (res) => res.toString(base);
};
