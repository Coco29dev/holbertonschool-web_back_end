const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2];

    try {
      const studentsByField = await readDatabase(database);
      const fields = Object.keys(studentsByField).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      let réponse = 'This is the list of our students\n';

      for (const field of fields) {
        const list = studentsByField[field];
        réponse += `Nimber od students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      res.status(200).type('text/plain').send(réponse.trim());

    } catch (error) {

      res.status(500).send('Cannot load the database');

    }
  }

  static async getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {

      return res.status(500).send('Major paramter must be CS or SWE');

    }

    try {
      const studentsByField = await readDatabase(database);
      const list = studentsByField[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
