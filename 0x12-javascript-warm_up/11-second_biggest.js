#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];
  const args = process.argv;
  for (let i = 2; i < args.length; i++) {
    numbers.push(Number(args[i]));
  }
  numbers.sort();
  console.log(numbers[numbers.length - 2]);
}
