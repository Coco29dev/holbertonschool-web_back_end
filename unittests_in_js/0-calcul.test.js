import assert from "assert";
import calculateNumber from './0-calcul.js';

describe('calculateNumber', function () {
  const tests = [
    { a: 1, b: 3, expected: 4 },
    { a: 1, b: 3.7, expected: 5 },
    { a: 1.2, b: 3.7, expected: 5 },
    { a: 1.5, b: 3.7, expected: 6 },
    { a: -1.5, b: -3.7, expected: -6 },
    { a: -1.2, b: -3.7, expected: -5 }
  ];

  tests.forEach(({ a, b, expected }) => {
    it(`should return ${expected} when a=${a} and b=${b}`, function () {
      const result = calculateNumber(a, b);
      assert.strictEqual(result, expected);
    });
  });
});
