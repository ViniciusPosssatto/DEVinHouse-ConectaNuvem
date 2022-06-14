
async function aguarda3Segundos(){
    await new Promise(
        resolve => setTimeout(resolve, 3000)
    );
    console.log('Função diz: terminei!');  //quando a função que for executada com essa, vai ter aviso quando for terminada a execução
}

async function euNãoEspero(){
    aguarda3Segundos();
    console.log('Eu não espero.')
}
euNãoEspero();

async function euEspero(){
    await aguarda3Segundos();  //vai aguardar 3 segundos para ser executado o console.log
    console.log('Eu espero agora')
}
euEspero();