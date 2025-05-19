const readline = require('node:readline');
const { stdin: input, stdout: output } = require('node:process');

const line = readline.createInterface({ input, output });

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

line.question('Welcome to Holberton School, what is your name?\n', (réponse) => {
  console.log(`Your name is: ${réponse}`);
  line.close();

  if (process.stdin.isTTY) {
    console.log('This important software ');
  }
});
