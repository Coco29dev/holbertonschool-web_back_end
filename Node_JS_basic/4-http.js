const app = require('http');

const server = app.createServer((req, res) => {
  res.write('Hello Holberton School!');
  res.end();
});

const PORT = 1245;

server.listen(PORT, () => {
  console.log("...");
});

module.exports = app;
