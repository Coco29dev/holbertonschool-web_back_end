const express = require('express');

const app = express();
const PORT = 1245;

app.get('/', (req, res) => {
  res.send('Hello holberton School!');
});

app.listen(PORT);

module.exports = app;
