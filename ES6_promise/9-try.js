export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const resultat = mathFunction();
    queue.push(resultat);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  }

  queue.push('Guardrail was processed');

  return queue;
}
