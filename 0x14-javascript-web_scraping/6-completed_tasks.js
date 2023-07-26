#!/usr/bin/node

const request = require('request');

const todoApiUrl = process.argv[2];

request.get(todoApiUrl, function (e, r, body) {
  if (e) {
    console.error(e);
  } else {
    if (r.statusCode === 200) {
      const todosList = JSON.parse(body);
      const completed = {};

      for (const t of todosList) {
        if (t.completed) {
          completed[t.userId] = (completed[t.userId] || 0) + 1;
        }
      }
      
      if (numberOfUsers <= 8) {
        console.log(completed);
      } else {
      	for (const userId in completed) {
          console.log(`${userId}: ${completed[userId]}`);
        }
     }
  }
});
