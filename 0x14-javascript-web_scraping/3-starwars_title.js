#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(JSON.parse(response.body).title);
}
);
