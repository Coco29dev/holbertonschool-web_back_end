export default function signUpUser(firstName, lastName) {
  const obj = { firstName, lastName };
  const FirstPromise = Promise.resolve(obj);
  return FirstPromise;
}
