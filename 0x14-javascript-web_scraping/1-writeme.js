#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

const data = new Uint8Array(Buffer.from(text));
fs.writeFile(file, data, (err) => {
  if (err) {
    console.log(err);
  }
});
