#!/usr/bin/node
// Script to fetch and print all character names from a given Star Wars movie using the Star Wars API

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.log('Please provide a valid movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', body);
    return;
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  charactersUrls.forEach(url => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Error:', body);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
