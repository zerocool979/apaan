import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

// Dapatkan __filename dan __dirname dalam modul ES
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const port = process.env.PORT || 3000; // Port untuk menjalankan server

// Sajikan file statis dari direktori saat ini (tempat index.html, script.js, style.css, dan folder asset berada)
app.use(express.static(path.join(__dirname)));

// Rute dasar untuk menyajikan index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Mulai server
app.listen(port, () => {
  console.log(`Server Chika berjalan di http://localhost:${port}`);
});
