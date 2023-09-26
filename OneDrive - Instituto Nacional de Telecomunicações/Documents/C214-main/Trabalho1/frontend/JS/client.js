function reset(){
  let title = document.getElementById('title');
  let description = document.getElementById('description');
  let status = document.getElementById('status');
  title.value = '';
  description.value = '';
  status.value = '';
}
// Função para exibir as tarefas na tabela
function displayTasks(tasks) {
  const tableBody = document.querySelector('#taskTable tbody');
  tableBody.innerHTML = ''; // Limpa o conteúdo atual da tabela

  tasks.forEach((task) => {
    const row = tableBody.insertRow(); // Cria uma nova linha na tabela
    const titleCell = row.insertCell(0); // Cria uma célula para o título
    const descriptionCell = row.insertCell(1); // Cria uma célula para a descrição
    const statusCell = row.insertCell(2); // Cria uma célula para o status

    // Preenche as células com os valores das tarefas
    titleCell.textContent = task.title;
    descriptionCell.textContent = task.description;
    statusCell.textContent = task.status;

    // Aplica as classes de status com base no status da tarefa
    statusCell.classList.add('tableStatus'); // Adiciona a classe comum a todas as células de status

    if (task.status === 'Completed') {
      statusCell.classList.add('Completed');
    } else if (task.status === 'InProgress') {
      statusCell.classList.add('InProgress');
    } else if (task.status === 'ToDo') {
      statusCell.classList.add('ToDo');
    }
  });
}
async function createTask(){
  let title = document.getElementById('title').value;
  let description = document.getElementById('description').value;
  let status = document.getElementById('status').value;
  if(title == '' || description == '' || status == ''){
    alert('Preencha todos os campos');
    reset();
  }else{
    if(status == 'InProgress' || status == 'Completed' || status == 'ToDo'){
    const myRequest1 = {
      method: 'GET',
      headers: new Headers({
          'Content-Type': 'application/json',
      }),
  };
    fetch('http://localhost:3000/tasks', myRequest1, {})
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Erro na solicitação: ${response.status}`);
      }  
      return response.json(); 
    })
    .then((data) => {
      let flag = 0;
      for(var i=0; i<data.length; i++){
          if((title == data[i].title)){
              flag=1;
              break;
          }else{
              flag = 0;
          }
      }
      if(flag == 0){
        const myRequest = {
          method: 'POST',
          headers: new Headers({
            'Content-Type': 'application/json',
          }),
          body: JSON.stringify({
              "title": title,
              "description": description,
              "status": status   
          }),
      };
      fetch('http://localhost:3000/tasks', myRequest, {})
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Erro na solicitação: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          console.log('Resposta do servidor:', data);
          alert('Foi criado uma Task!');
          reset();
          location.reload(); 
        })
        .catch((error) => {
          console.error('Erro na solicitação:', error.message);
          reset();
        });
      }else{
        alert('Task ja foi criada com esse nome, insira outro!');
        reset();
      }  
    })
}else{
  alert('Entre com um valor de status como: (InProgress), (Completed) ou (Todo)');
}
}
}
async function searchTask() {
  const myRequest = {
      method: 'GET',
      headers: new Headers({
          'Content-Type': 'application/json',
      }),
  };
  fetch('http://localhost:3000/tasks', myRequest)
      .then((response) => {
          if (!response.ok) {
              throw new Error(`Erro na solicitação: ${response.status}`);
          }
          return response.json();
      })
      .then((data) => {
          console.log('Resposta do servidor:', data);
          displayTasks(data); // Chama a função para exibir as tarefas
          reset();
      })
      .catch((error) => {
          console.error('Erro na solicitação:', error.message);
          reset();
      });
}
async function updateTask(){
  const title = document.getElementById('title').value;
  const description = document.getElementById('description').value;
  const status = document.getElementById('status').value;
  if(status == 'InProgress' || status == 'Completed' || status == 'Todo'){
  const myRequest1 = {
    method: 'GET',
    headers: new Headers({
        'Content-Type': 'application/json',
    }),
};
fetch('http://localhost:3000/tasks', myRequest1, {})
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Erro na solicitação: ${response.status}`);
    }  
    return response.json(); 
  })
  .then((data) => {
    let flag = 0;
    let id = '';
    for(var i=0; i<data.length; i++){
        if((title == data[i].title)){
            flag=1;
            id = data[i]._id;
            break;
        }else{
            flag = 0;
        }
    }
    if(flag == 0){
        alert('Task não encontrada!');
        reset();
      }else{
        const myRequest2 = {
          method: 'PUT',
          headers: new Headers({
          'Content-Type': 'application/json',
          }),
          body:JSON.stringify({
            status: status,
            description: description
          })
        };
        fetch(`http://localhost:3000/tasks/${id}`,(myRequest2))
        .then(response => {
          if (response.ok) {
            alert(`Task atualizada com id: ${id}`);
            console.log(`Task atualizada com id: ${id}`);
            reset();
          } else {
            alert('Erro na requisição:', response.status);
            console.error('Erro na requisição:', response.status);
            reset();
          }
        })
        .catch(error => {
          alert('Erro na requisição:', error);
          console.error('Erro na requisição:', error);
          reset();
        });
    }})
}
else{
  alert('Entre com um valor de status como: (InProgress), (Completed) ou (Todo)');
}
}
async function deleteTask(){
    const title = document.getElementById('title').value;

    const myRequest = {
        method: 'GET',
        headers: new Headers({
            'Content-Type': 'application/json',
        }),
    };
    fetch('http://localhost:3000/tasks', myRequest, {})
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Erro na solicitação: ${response.status}`);
        }
        return response.json(); 
      })
      .then((data) => {
        let flag = 0;
        let id = '';
        for(var i=0; i<data.length; i++){
            if((title == data[i].title)){
                flag=1;
                id = data[i]._id;
                break;
            }else{
                flag = 0;
            }
        }
        if(flag == 0){
            alert('Task não encontrada!');
            reset();
        }else{
            const myRequestdelete = {
                method: 'DELETE',
                headers: new Headers({
                    'Content-Type': 'application/json',
                }),
            };
            try{
            fetch(`http://localhost:3000/tasks/${id}`, myRequestdelete, {})
              .then((response) => {
                if (!response.ok) {
                  throw new Error(`Erro na solicitação: ${response.status}`);
                  reset();
                }
                else{
                    alert(`Task removida com id ${id}`);
                    reset();
                    return response;
                
            }
            })
            }
            catch(error){
                console.log('Erro ao deletar: ', error);
                reset();
            }
        }
      })
}

