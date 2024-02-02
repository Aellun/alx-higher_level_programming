#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

// Request to get film details
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) return;
  // Request to get character details
  request(characters[index], (error, response, body) => {
    if (!error) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
}
