#!/usr/bin/node
const request = require('request');

// The first argument is the API URL
const apiUrl = process.argv[2];
request(apiUrl, (err, res, body) => {
  const userTasks = {};
  if (err) {
    console.error(err);
    return;
  }
  try {
    const todos = JSON.parse(body);
    todos.forEach(todo => {
      if (todo.completed) {
        if (!userTasks[todo.userId]) {
          userTasks[todo.userId] = 0;
        }
        userTasks[todo.userId]++;
      }
    });
    console.log(userTasks);
  } catch (parseErr) {
    console.error('Error parsing JSON:', parseErr);
  }
});

