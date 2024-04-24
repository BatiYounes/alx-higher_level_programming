#!/usr/bin/node
// Script to fetch and print all character names from a given Star Wars movie using the Star Wars API

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.log('Please provide a valid movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

(async () => {
  try {
    const filmData = await fetchFilmData(apiUrl);
    const charactersUrls = filmData.characters;

    for (const url of charactersUrls) {
      const characterData = await fetchCharacterData(url);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
})();

function fetchFilmData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || body);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}

function fetchCharacterData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || body);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
