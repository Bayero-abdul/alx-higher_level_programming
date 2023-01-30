#!/usr/bin/node

exports.esrever = function (list) {
  const output = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    output.push(list.pop());
  }
  return (output);
};
