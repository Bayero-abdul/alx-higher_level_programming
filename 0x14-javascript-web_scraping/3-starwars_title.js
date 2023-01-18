#!/usr/bin/node

const request = require('request');
const API = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2];
const URL = API + ID;

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
