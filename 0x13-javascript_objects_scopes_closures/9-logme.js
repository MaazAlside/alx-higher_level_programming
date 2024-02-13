#!/usr/bin/node
exports.logMe = function (item) {
  exports.logMe.count = (exports.logMe.count || 0) + 1;
  console.log(exports.logMe.count - 1 + ': ' + item);
};
