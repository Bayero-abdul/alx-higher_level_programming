#!/usr/bin/node

const args = process.argv;
if (args.length < 3 || isNaN(args[2])) {
  console.log('Not a number');
} else {
  const num = Math.floor(Number(args[2]));
  console.log(`My number: ${num}`);
}
