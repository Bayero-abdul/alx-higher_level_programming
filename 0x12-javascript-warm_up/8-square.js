#!/usr/bin/node

const size = process.argv[2];
if (!size || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
