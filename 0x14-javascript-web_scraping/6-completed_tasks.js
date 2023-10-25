#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const res = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };
  const tasks = JSON.parse(response.body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      res[tasks[i].userId] = res[tasks[i].userId] + 1;
    }
  }
  console.log(res);
});
