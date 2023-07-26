#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);

if (args.length === 2) {
  const file = args[0];
  const content = args[1];
  fs.writeFile(file, content, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
}
