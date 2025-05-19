process.stdout.write("Welcome to Holberton School, what is your name?\n");

process.stdin.setEncoding("utf-8");

process.stdin.on("data", (input) => {
  const name = input.trim();
  console.log(`Your name is: ${name}`);

  if (!process.stdin.isTTY) {
    console.log("This important software is now closing");
  }

  process.exit();
});
