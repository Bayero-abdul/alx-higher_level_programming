#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

// Function to fetch characters of the specified movie
function fetchMovieCharacters (movieUrl) {
  return new Promise((resolve, reject) => {
    request.get(movieUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch movie. Status code: ${response.statusCode}`));
      } else {
        const movie = JSON.parse(body);
        resolve(movie.characters);
      }
    });
  });
}

// Function to fetch character name by URL
function fetchCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character. Status code: ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

// Main function to print character names
async function printMovieCharacters () {
  try {
    const charactersUrls = await fetchMovieCharacters(apiUrl);

    // Fetch and print each character name
    for (const characterUrl of charactersUrls) {
      const characterName = await fetchCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the main function
printMovieCharacters();
