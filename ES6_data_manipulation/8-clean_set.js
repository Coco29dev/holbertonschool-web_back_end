export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string' || startString === '') {
    return '';
  }

  const result = [];

  for (const value of set) {
    if (typeof value === 'string' && value && value.startsWith(startString)) {
      const suffix = value.slice(startString.length);
      if (suffix) {
        result.push(suffix);
      }
    }
  }

  return result.join('-');
}
