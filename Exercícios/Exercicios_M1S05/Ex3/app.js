
const nome = document.getElementById('nome');
const msg = document.getElementById('msg');
const botao = document.getElementById('botao')
const total = document.getElementById('total');

const produtos = [
    { nome: 'arroz', preco: 9 },
    { nome: 'feijao', preco: 12 },
    { nome: 'batata', preco: 8 },
    { nome: 'macarrao', preco: 5 }
    ];

const filtra = (() => {
    let item = procurar(nome.value, produtos)
    if(item){
        msg.innerHTML = `Produto encontrado! O preço de ${item.nome} é: R$${item.preco},00.`;
    }else{
        msg.innerHTML = `Este produto não está disponível.`;
    }
});

function procurar(nome, lista){
    var item = lista.find(name => name.nome === nome)
    return item
}

botao.addEventListener('click', filtra);


const vetObjTotal = produtos.reduce((acc, item) => {
    return acc + item.preco;
}, 0);

total.innerHTML = `O valor total dos produtos é R$${vetObjTotal},00.`