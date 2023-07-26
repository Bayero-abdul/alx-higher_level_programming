#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request.get(apiUrl, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    if (r.statusCode === 200) {
      const film = JSON.parse(body);
      for (const characterUrl of film.characters) {
        request.get(characterUrl, function (e, r, body) {
          if (r.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          }
        });
      }
    }
  }
});
