#!/usr/bin/node
// send a request to star wars api

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body);

    let sum = 0;
    let film;
    let char;
    for (film in films.results) {
      for (char in films.results[film].characters) {
        if (films.results[film].characters[char].includes('18')) {
          sum++;
        }
      }
    }
    console.log(sum);
  }
});
