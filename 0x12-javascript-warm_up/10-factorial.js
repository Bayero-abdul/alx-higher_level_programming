#!/usr/bin/node

const n = Number(process.argv[2]);

console.log(factorial(n));

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
