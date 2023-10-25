#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let count = 0;
  const films = JSON.parse(response.body).results;
  for (let i = 0; i < films.length; i++) {
    if (films[i].characters.some(item => item.includes('/18/'))) {
      count = count + 1;
    }
  }
  console.log(count);
});
