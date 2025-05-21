const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const { url } = req;

  if (url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    const database = process.argv[2];

    res.writeHead(200, { 'Content-Type': 'text/plain' });

    countStudents(database)
      .then((result) => {
        const responseText = `This is the list of our students\n${result}`;
        res.end(responseText);
      })
      .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found');
  }
});

const PORT = 1245;
app.listen(PORT);

module.exports = app;
