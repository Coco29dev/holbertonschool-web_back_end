import fs from 'fs/promises';

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const header = lines[0].split(',');
    const fieldIndex = header.indexOf('field');
    const firstNameIndex = header.indexOf('firstname');

    if (fieldIndex === -1 || firstNameIndex === -1) {
      throw new Error('Malformed CSV file');
    }

    const studentsByField = {};

    for (let i = 1; i < lines.length; i++) {
      const line = lines[i].trim();
      if (!line) continue;

      const parts = line.split(',');
      if (parts.length <= fieldIndex || parts.length <= firstNameIndex) continue;

      const field = parts[fieldIndex];
      const firstName = parts[firstNameIndex];

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }

      studentsByField[field].push(firstName);
    }

    return studentsByField;
  } catch (err) {
    return Promise.reject(err);
  }
}

export default readDatabase;
