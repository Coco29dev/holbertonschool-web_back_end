const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  it('should return status code 200', (done) => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct welcome message', (done) => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should not return an error', (done) => {
    request.get('http://localhost:7865/', (error, response, body) => {
      expect(error).to.be.null;
      done();
    });
  });
});

describe('Cart page', () => {
  it('should return status code 200 when :id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message when :id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('should return status code 404 when :id is NOT a number', (done) => {
    request.get('http://localhost:7865/cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments', () => {
  it('should return status code 200', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct object (deep equality)', (done) => {
    request.get('http://localhost:7865/available_payments', (error, response, body) => {
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('Login', () => {
  it('should return status code 200', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      json: true,
      body: { userName: 'Betty' },
    };

    request.post(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the welcome message with the username', (done) => {
    const options = {
      url: 'http://localhost:7865/login',
      json: true,
      body: { userName: 'Betty' },
    };

    request.post(options, (error, response, body) => {
      expect(body).to.equal('Welcome Betty');
      done();
    });
  });
});
