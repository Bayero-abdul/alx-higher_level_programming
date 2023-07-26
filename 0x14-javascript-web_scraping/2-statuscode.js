#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    console.log('code:', r.statusCode);
  }
});
