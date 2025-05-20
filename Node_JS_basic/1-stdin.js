process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const prénom = process.stdin.read();
  if (prénom) {
    process.stdout.write(`Your name is: ${prénom}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
