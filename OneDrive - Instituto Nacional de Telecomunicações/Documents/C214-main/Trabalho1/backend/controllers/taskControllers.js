import Task from "../models/task.js";

async function getTasks (req, res){
    const tasks = await Task.find();
    return res.status(200).send(tasks);
}
async function createTask( req, res ){
    const task = req.body;
    const newTask = await Task.create(task);
    return res.status(201).send(newTask);
}
async function deleteTask( req, res ){
    const id = req.params.id;
    await Task.findByIdAndDelete(id);
    return res.status(200).send('Task excluida com sucesso!');
}
async function updateTask( req, res ){
    const id = req.params.id
    const status = req.body.status;
    const description = req.body.description;
    const task = await Task.findByIdAndUpdate({"_id": id}, {"status": status, "description": description});
    return res.status(200).send('Task atualizada com sucesso!');
}

export { getTasks, createTask, deleteTask, updateTask};