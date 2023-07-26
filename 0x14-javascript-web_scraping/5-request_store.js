#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    if (r.statusCode === 200) {
      fs.writeFile(file, body, 'utf8', (err, data) => {
        if (err) {
          console.error(err);
        }
      });
    }
  }
});
