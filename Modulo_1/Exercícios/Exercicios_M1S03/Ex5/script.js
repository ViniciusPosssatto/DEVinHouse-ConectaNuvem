//define um intervalo de 1 seg
setInterval(() => {
  var timestamp = document.getElementById("timestamp")
  var data = new Date(); //pega a data completa
  var hora = data.getHours(); //seleciona só a hora
  var min = data.getMinutes(); //seleciona só os minutos
  var time = hora + 'h' + ":" + min + 'min'; 
  horacerta.innerText = time; //imprime na tela pelo id = time
}, 1000);
