const fs = require('node:fs');
const path = require('node:path');
const { exporter, VERSION } = require('@dbml/core');

const [entrada, salida, dialecto = 'postgres'] = process.argv.slice(2);
const permitidos = new Set(['postgres', 'mysql', 'mssql', 'oracle']);

if (!entrada || !salida) {
  console.error('Uso: node convertir-dbml.js <entrada.dbml> <salida.sql> [postgres|mysql|mssql|oracle]');
  process.exit(2);
}
if (!permitidos.has(dialecto)) {
  console.error(`Dialecto no permitido: ${dialecto}`);
  process.exit(2);
}

try {
  const fuente = fs.readFileSync(entrada, 'utf8');
  const sql = exporter.export(fuente, dialecto);
  fs.mkdirSync(path.dirname(salida), { recursive: true });
  fs.writeFileSync(salida, sql, 'utf8');
  console.log(`DBML Core ${VERSION}: generado ${salida} (${dialecto}).`);
} catch (error) {
  console.error(`No se pudo convertir DBML: ${error.message}`);
  process.exit(1);
}
