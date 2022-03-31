const nome = document.getElementById('nome');
const msg = document.getElementById('msg');
const botao = document.getElementById('botao')


const mensagemOla = () => {
    if(nome.value){
        msg.innerHTML = `Olá, ${nome.value}! Que bom te ver por aqui.`;
    }else{
        msg.innerHTML = `Digite seu nome acima.`
    }
};

botao.addEventListener('click', mensagemOla);