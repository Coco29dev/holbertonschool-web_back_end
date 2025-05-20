const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
