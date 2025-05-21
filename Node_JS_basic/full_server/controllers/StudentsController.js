import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2];

    try {
      const studentsByField = await readDatabase(database);
      const sortMethod = (a, b) => a.toLowerCase().localeCompare(b.toLowerCase());
      const fields = Object.keys(studentsByField).sort(sortMethod);

      let response = 'This is the list of our students\n';

      for (const field of fields) {
        const list = studentsByField[field];
        response += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      res.status(200).type('text/plain').send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const database = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const studentsByField = await readDatabase(database);
      const list = studentsByField[major] || [];
      return res.status(200).send(`List: ${list.join(', ')}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
