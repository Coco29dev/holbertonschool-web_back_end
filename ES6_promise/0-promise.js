export default function getResponseFromAPI() {
  const FirstPromise = new Promise((resolve, reject) => {
    const ExecutionGood = true;

    if (ExecutionGood) {
      resolve('Approuvé');
    } else {
      reject(new Error('Rejeté'));
    }
  });
  return FirstPromise;
}
