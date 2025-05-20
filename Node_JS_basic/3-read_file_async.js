const fs = require('fs').promises;

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8')
      .then((data) => {
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        const students = lines.slice(1).filter((line) => line.length > 0);

        console.log(`Number of students: ${students.length}`);

        const fieldGroups = {};

        students.forEach((student) => {
          const fields = student.split(',');
          const firstName = fields[0];
          const field = fields[3];

          if (!fieldGroups[field]) {
            fieldGroups[field] = [];
          }

          fieldGroups[field].push(firstName);
        });

        for (const field in fieldGroups) {
          if (Object.prototype.hasOwnProperty.call(fieldGroups, field)) {
            const studentList = fieldGroups[field];
            console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
          }
        }

        resolve();
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
}

module.exports = countStudents;
