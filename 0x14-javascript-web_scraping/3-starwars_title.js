#!/usr/bin/node
// script that prints the title of a Star Wars movie

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (error, response, body) =>
  error ? console.error(error) : console.log(JSON.parse(body).title)
);
