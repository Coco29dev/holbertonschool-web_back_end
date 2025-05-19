const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const line = readline.createInterface({ input, output });

console.log('Welcome to Holberton School, what is your name?');

line.on('line', (input) => {
  console.log(`Your name is: ${input}`);
  line.close();

  if (process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
