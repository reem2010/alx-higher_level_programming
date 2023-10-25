#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const res = {};
  const tasks = JSON.parse(response.body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      if (!res[tasks[i].userId]) {
        res[tasks[i].userId] = 1;
      } else { res[tasks[i].userId] = res[tasks[i].userId] + 1; }
    }
  }
  console.log(res);
});
