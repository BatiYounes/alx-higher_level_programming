#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], function (error, response, body) {
    if (error) {
      console.error(error);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);
    printCharactersInOrder(characters, index + 1);
  });
}
