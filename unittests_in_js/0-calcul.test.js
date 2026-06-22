const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('retourne la somme de deux entiers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('arrondit b vers le haut', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('arrondit a vers le bas et b vers le haut', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('arrondit une valeur en .5 vers le haut', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('gère les nombres négatifs', function () {
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
  });

  it('arrondit un .5 négatif vers zéro', function () {
    assert.strictEqual(calculateNumber(-1.5, 3.7), 3);
  });
});
