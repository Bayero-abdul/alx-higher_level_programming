#!/usr/bin/node

const request = require('request');
const API = process.argv[2];

request(API, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log('Invalid Status Code Returned:', response.statusCode);
  } else {
    const taskDone = {};
    const jsonTodos = JSON.parse(body);
    for (const user of jsonTodos) {
      if (user.completed) {
        const idx = user.userId.toString();

        if (!(idx in taskDone)) {
          taskDone[idx] = 1;
        } else {
          taskDone[idx] += 1;
        }
      }
    }
    console.log(taskDone);
  }
});
