const fs = require('fs').promises;

function readDatabase(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const header = lines[0].split(',');
      const filedIndex = header.indexOf('filed');
      const firstNameIndex = header.indexOf('firstname');

      if (fieldIndex === -1 || firstNameIndex === -1) {
        throw new Error('Malformed CSV file');
      }

      const studentsByField = {};

      for (let i = 1; i < lines.length; i++) {
        const line = lines[i].trim();
        if (!line) continue;

        const parts = line.split(',');
        if (parts.length <= filedIndex || parts.length <= firstNameIndex) continue;

        const field = parts[filedIndex];
        const firstName = parts[firstNameIndex];

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }

        studentsByField[field].push(firstName);
      }

      return studentsByField;
    })
    .catch((err) => {
      return Promise.reject(err);
    });
}

module.exports = readDatabase;
