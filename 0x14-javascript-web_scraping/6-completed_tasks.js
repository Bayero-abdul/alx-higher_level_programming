#!/usr/bin/node

const request = require('request');

const todoApiUrl = process.argv[2];

request.get(todoApiUrl, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    if (r.statusCode === 200) {
      const todosList = JSON.parse(body);
      const numOfTaskById = {};

      let count = 0;
      let userId = todosList[0].userId;

      for (const task of todosList) {
        if (task.userId === userId) {
          if (task.completed === true) { count++; }
        } else {
          numOfTaskById[userId] = count;
          userId = task.userId;
          count = 0;
          if (task.completed === true) { count++; }
        }
      }
      numOfTaskById[userId] = count;
      console.log(numOfTaskById);
    }
  }
});
