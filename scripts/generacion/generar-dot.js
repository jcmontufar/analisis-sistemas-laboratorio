const fs = require('node:fs');
const path = require('node:path');
const { instance } = require('@viz-js/viz');

const [entrada, salida] = process.argv.slice(2);
if (!entrada || !salida) {
  console.error('Uso: node generar-dot.js <entrada.dot> <salida.svg>');
  process.exit(2);
}

(async () => {
  try {
    const viz = await instance();
    const dot = fs.readFileSync(entrada, 'utf8');
    const svg = viz.renderString(dot, { format: 'svg', engine: 'dot' });
    fs.mkdirSync(path.dirname(salida), { recursive: true });
    fs.writeFileSync(salida, svg, 'utf8');
    console.log(`Generado: ${salida}`);
  } catch (error) {
    console.error(`No se pudo renderizar DOT: ${error.message}`);
    process.exit(1);
  }
})();
