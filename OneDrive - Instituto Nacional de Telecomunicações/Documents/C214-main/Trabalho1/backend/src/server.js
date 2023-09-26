import express from 'express';
import cors from 'cors';
import routes from './routes.js';
import connectionDB from '../database/db.js';
const app = express();

app.use(express.json());
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:5500'); 
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
  });
app.use(cors());
app.use(routes);
try{
  connectionDB();
}catch(error){
  console.log('Ocorreu um erro: ', error);
}
export default app;