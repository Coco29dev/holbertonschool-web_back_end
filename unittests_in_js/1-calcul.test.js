const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  it('DIVIDE', function () {
    assert.strictEqual(calculateNumber('DIVIDE', 10, 2), 5);
    assert.strictEqual(calculateNumber('DIVIDE', 10, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 10.7, 2.3), 5.5);
    assert.strictEqual(calculateNumber('DIVIDE', -10, -2), 5);
    assert.strictEqual(calculateNumber('DIVIDE', -10, 2), -5);
    assert.strictEqual(calculateNumber('DIVIDE', 10, -2), -5);
    assert.strictEqual(calculateNumber('DIVIDE', -10.7, -2.3), 5.5);
    assert.strictEqual(calculateNumber('DIVIDE', -10.7, 2.3), -5.5);
    assert.strictEqual(calculateNumber('DIVIDE', 10.7, -2.3), -5.5);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });

  it('SUM', function () {
    assert.strictEqual(calculateNumber('SUM', 10, 2), 12);
    assert.strictEqual(calculateNumber('SUM', 10.7, 2.3), 13);
    assert.strictEqual(calculateNumber('SUM', -10, -2), -12);
    assert.strictEqual(calculateNumber('SUM', -10, 2), -8);
    assert.strictEqual(calculateNumber('SUM', 10, -2), 8);
    assert.strictEqual(calculateNumber('SUM', -10.7, -2.3), -13);
    assert.strictEqual(calculateNumber('SUM', -10.7, 2.3), -9);
    assert.strictEqual(calculateNumber('SUM', 10.7, -2.3), 9);
  });

  it('SUBTRACT', function () {
    assert.strictEqual(calculateNumber('SUBTRACT', 10, 2), 8);
    assert.strictEqual(calculateNumber('SUBTRACT', 10.7, 2.3), 9);
    assert.strictEqual(calculateNumber('SUBTRACT', -10, -2), -8);
    assert.strictEqual(calculateNumber('SUBTRACT', -10, 2), -12);
    assert.strictEqual(calculateNumber('SUBTRACT', 10, -2), 12);
    assert.strictEqual(calculateNumber('SUBTRACT', -10.7, -2.3), -9);
    assert.strictEqual(calculateNumber('SUBTRACT', -10.7, 2.3), -13);
    assert.strictEqual(calculateNumber('SUBTRACT', 10.7, -2.3), 13);
  });
});
