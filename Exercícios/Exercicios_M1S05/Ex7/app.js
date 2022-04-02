
async function aguarda3Segundos(){
    await new Promise(
        resolve => setTimeout(resolve, 3000)
    );
    console.log('Função diz: terminei!');
}

async function euNãoEspero(){
    aguarda3Segundos();
    console.log('Eu não espero.')
}
euNãoEspero();

async function euEspero(){
    await aguarda3Segundos();
    console.log('Eu espero agora')
}
euEspero();