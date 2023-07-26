#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;
let count = 0;
request.get(apiUrl, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    if (r.statusCode === 200) {
      const films = JSON.parse(body).results;
      for (const film of films) {
        for (const characterUrl of film.characters) {
          let match = characterUrl.match(/\/(\d+)\/$/);
          match = match ? match[1] : null;
          if (characterId === parseInt(match)) { count++; }
        }
      }
      console.log(count);
    }
  }
});
