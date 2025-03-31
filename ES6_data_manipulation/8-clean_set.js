export default function cleanSet(set, startString) {
  if (startString === '' || !startString) {
    return '';
  }

  const result = [];

  for (const string of set) {
    if (string.startsWith(startString)) {
      const suffix = string.slice(startString.length);
      result.push(suffix);
    }
  }

  return result.join('-');
}
