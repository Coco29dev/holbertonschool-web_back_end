import handleProfileSignup from './6-final-user';

const test = async () => {
  const results = await handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg");
  console.log(results);
};

test();