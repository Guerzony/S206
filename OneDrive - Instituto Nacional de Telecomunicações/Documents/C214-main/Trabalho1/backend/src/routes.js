import Router from 'express';
import { getTasks, updateTask, deleteTask, createTask  } from '../controllers/taskControllers.js';
const routes = Router();


//Rotas para criação, leitura, busca, atualizção das tasks
routes.get('/tasks', getTasks);
routes.post('/tasks', createTask);
routes.put('/tasks/:id',updateTask);
routes.delete('/tasks/:id',deleteTask);

export default routes;


