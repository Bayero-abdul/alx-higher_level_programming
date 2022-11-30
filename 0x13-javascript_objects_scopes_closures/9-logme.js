#!/usr/bin/node

let count = 0;
exports.logMe = function (Arg) {
  console.log(`${count}: ${Arg}`);
  count++;
};
