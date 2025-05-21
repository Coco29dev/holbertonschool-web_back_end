const express = require('express');
const router = express.Router();
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

router.get('/', AppController);
router.get('/students', StudentsController);
router.get('/students:major', StudentsController);

module.exports = router;
