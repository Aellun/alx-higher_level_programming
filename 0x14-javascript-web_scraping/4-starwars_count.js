#!/usr/bin/node
// Wedge Antilles” is present in the star war movies
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (!error) {
    const count = JSON.parse(body).results
      .filter(movie => movie.characters.some(character => character.endsWith('/18/')))
      .length;

    console.log(count);
  }
});
