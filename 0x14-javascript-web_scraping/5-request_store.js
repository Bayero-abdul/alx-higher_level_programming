#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const PATH = process.argv[3];


request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = new Uint8Array(Buffer.from(body));
    fs.writeFile(PATH, data, {encoding: 'utf8'}, (err) => {
      if (err) {
        console.log(err);
       }
    });
  }
});
