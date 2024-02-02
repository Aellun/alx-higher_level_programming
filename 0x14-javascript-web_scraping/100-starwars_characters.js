#!/usr/bin/node
//  script that prints all characters of a Star Wars movie
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, (error, res, body) => {
      if (error) {
        console.log(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

