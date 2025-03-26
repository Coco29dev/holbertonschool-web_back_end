export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }

    this._sqft = sqft;

    if (this.constructor !== Building) {
      const hasMethod = Object.prototype.hasOwnProperty.call(
        Object.getPrototypeOf(this),
        'evacuationWarningMessage',
      )
        || this.evacuationWarningMessage !== Building.prototype.evacuationWarningMessage;

      if (!hasMethod) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    this._checkMethodIsCalled = true;
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
