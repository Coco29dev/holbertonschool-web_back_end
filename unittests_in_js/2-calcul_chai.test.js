const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  it('DIVIDE', function () {
    expect(calculateNumber('DIVIDE', 10, 2)).to.equal(5);
    expect(calculateNumber('DIVIDE', 10, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 10.7, 2.3)).to.equal(5.5);
    expect(calculateNumber('DIVIDE', -10, -2)).to.equal(5);
    expect(calculateNumber('DIVIDE', -10, 2)).to.equal(-5);
    expect(calculateNumber('DIVIDE', 10, -2)).to.equal(-5);
    expect(calculateNumber('DIVIDE', -10.7, -2.3)).to.equal(5.5);
    expect(calculateNumber('DIVIDE', -10.7, 2.3)).to.equal(-5.5);
    expect(calculateNumber('DIVIDE', 10.7, -2.3)).to.equal(-5.5);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });

  it('SUM', function () {
    expect(calculateNumber('SUM', 10, 2)).to.equal(12);
    expect(calculateNumber('SUM', 10.7, 2.3)).to.equal(13);
    expect(calculateNumber('SUM', -10, -2)).to.equal(-12);
    expect(calculateNumber('SUM', -10, 2)).to.equal(-8);
    expect(calculateNumber('SUM', 10, -2)).to.equal(8);
    expect(calculateNumber('SUM', -10.7, -2.3)).to.equal(-13);
    expect(calculateNumber('SUM', -10.7, 2.3)).to.equal(-9);
    expect(calculateNumber('SUM', 10.7, -2.3)).to.equal(9);
  });

  it('SUBTRACT', function () {
    expect(calculateNumber('SUBTRACT', 10, 2)).to.equal(8);
    expect(calculateNumber('SUBTRACT', 10.7, 2.3)).to.equal(9);
    expect(calculateNumber('SUBTRACT', -10, -2)).to.equal(-8);
    expect(calculateNumber('SUBTRACT', -10, 2)).to.equal(-12);
    expect(calculateNumber('SUBTRACT', 10, -2)).to.equal(12);
    expect(calculateNumber('SUBTRACT', -10.7, -2.3)).to.equal(-9);
    expect(calculateNumber('SUBTRACT', -10.7, 2.3)).to.equal(-13);
    expect(calculateNumber('SUBTRACT', 10.7, -2.3)).to.equal(13);
  });
});
