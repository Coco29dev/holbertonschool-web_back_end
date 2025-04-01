export default function uploadPhoto(fileName) {
  const FirstPromise = Promise.reject(new Error(`${fileName} cannot be processed`));
  return FirstPromise;
}
