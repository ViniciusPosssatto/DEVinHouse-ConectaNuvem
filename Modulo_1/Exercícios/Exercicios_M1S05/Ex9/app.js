const campoCEP = document.getElementById('campo-cep');
const botaoBuscar = document.getElementById('botao-buscar');
const pResultado = document.getElementById('resultado');

async function buscaCEP() {
    try {
      const cep = campoCEP.value;
      const url = `https://viacep.com.br/ws/${cep}/json`;
  
      const resposta = await fetch(url);
      //console.log(resposta);
      const conteudo = await resposta.json();
      //console.log(conteudo);
  
      pResultado.innerText = conteudo.localidade;
    } catch (erro) {
      console.error(erro);
    }
  }
  
  botaoBuscar.addEventListener('click', buscaCEP);
  