#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  let res = {};
  const tasks = JSON.parse(response.body);
  for (let i = 0; i < tasks.length; i++) {
    if (!res[tasks[i].userId]){
      res[tasks[i].userId] = 0;
    }
    if (tasks[i].completed) {
      res[tasks[i].userId] = res[tasks[i].userId] + 1 || 1;
    }
  }
  console.log(res);
});
