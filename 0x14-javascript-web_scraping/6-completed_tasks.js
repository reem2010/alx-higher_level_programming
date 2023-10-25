#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let count = 1;
	let res = {};
  const tasks = JSON.parse(response.body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      res[`${count}`] = tasks[i].id;
      count = count + 1;
    }
  }
  console.log(res);
});
