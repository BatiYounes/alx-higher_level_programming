#!/usr/bin/node

const req = require('request');
const episode = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/';

req(api + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
