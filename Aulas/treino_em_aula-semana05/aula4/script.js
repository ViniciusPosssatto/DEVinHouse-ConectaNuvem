// ///exercicio de concatenar com export e import

// import concat from './util.js'

// const a = [1, 2, 3, 4];
// const b = [5, 6, 7, 8];

// const concatenado = concat(v, b);
// console.log(concatenado);


// export default function concatena(veta, vetb)






// ///////////////////////////

// const listaCEPs = {
//   '88034001': {
//     logradouro: 'Rua do SENAI SC'
//   }
// }

// function buscaCEPpromise(cep) {


//   return new Promise((resolve, reject) => {
//     const resultado = listaCEPs[cep];
    
//     const erro = resultado ? null : 'CEP inválido!';

//     if (erro) {
//       reject(erro);
//     } else {
//       resolve(resultado);
//     }
//   });
// }

// buscaCEPpromise('88034001')
//   .then(resultado => {
//     //console.log(resultado);
//   })
//   .catch(erro => {
//     console.log('ERRRRRRROOOOU');
//     //console.log(erro);
//   });

// console.log('Após')


// EXEMPLO DE FETCH

// sempre usar o path para colocar um arquivo do PC ou do seu servidor
//'/modulo-1/semana-5/aula-4/teste.txt'

// const display = document.getElementById('display');
// const campoCEP = document.getElementById('campo-cep');
// const btnCEP = document.getElementById('btn-cep');

// function buscaCEP() {
//   const cep = campoCEP.value;

//   if (!cep) {
//     display.innerHTML = 'Informe um CEP!';
//     return;
//   }

// puxa as informações JSON do site selecionado
// fetch(`https://viacep.com.br/ws/${cep}/json`)
//   .then(resposta => {
//     resposta.json()  //--- aqui o JSON retorna uma promise, então deve ser utilizado o .then dentro dele(como abaixo)
//       .then(conteudo => {  //----imprime todo o conteudo o JSON
//         console.log(conteudo);
//         p.innerHTML = conteudo.logradouro;  /// --- seleciona o logradouro dentro do JSON e imprime no html
//       })
//   })
//   .catch(erro => {   // caso o then não funcione, ele aciona o catch e aparece o erro no console
//     console.log(erro)
//   });

//   btnCEP.addEventListener('click', buscaCEP);


  // EXEMPLOS ASYNC AWAIT

// promise com atraso
// function delay(ms) {
//   return new Promise(resolve => {
//       setTimeout(() => resolve('blah'), ms);
//     }
//   );
// }

// uma arrow function assíncrona
// async function buscaCEP() {
//   // comando de espera
//   const resposta = await delay(1000);
//   // executa após conclusão de delay
//   console.log('Terminei de esperar! ' + resposta);
// }

// roda o exemplo
// buscaCEP();
// imprime primeiro no console
// console.log('Executei o console log');

// async await com fetch

// async function buscaCEPawait() {
//   const cep = campoCEP.value;

//   if (!cep) {
//     display.innerHTML = 'Informe um CEP!';
//     return;
//   }

//   const url = `https://viacep.com.br/ws/${cep}/json`;
//   const resposta = await fetch(url);
//   const conteudo = await resposta.json()

//   console.log(conteudo);
//   display.innerHTML = conteudo.localidade;

  // .catch(erro => {
  //   console.log(erro);
  // });
// }

//btnCEP.addEventListener('click', buscaCEPawait);

// EXEMPLO COM TRY CATCH

// async function buscaCEPtry() {
//   try {
//     const cep = campoCEP.value;

//     if (!cep) {
//       throw new Error('CEP não informado!');
//     }
    
//     const url = `https://viacep.com.br/ws/${cep}/json`;
//     const resposta = await fetch(url);
//     const conteudo = await resposta.json()

//     console.log(conteudo);
//     display.innerHTML = conteudo.localidade;

//   } catch (erro) {
//     display.innerHTML = erro;
//     console.log('DENTRO DO CATCH!');
//     console.log({ erro });
//   } finally {
//     console.log('FINALLY!');
//   }
// }

// btnCEP.addEventListener('click', buscaCEPtry);


// /// teste de CEP com validador de CEP para 8 dígitos
// function validaCEP(cep) {
//   return cep.length === 8;
// }

// // EXEMPLO COM TRY CATCH

// async function buscaCEPtry() {
//   try {
//     const cep = campoCEP.value;

//     if (!validaCEP(cep)) {
//       throw new Error('CEP não informado!');
//     }
    
//     const url = `https://viacep.com.br/ws/${cep}/json`;
//     const resposta = await fetch(url);
//     const conteudo = await resposta.json()

//     console.log(conteudo);
//     display.innerHTML = conteudo.localidade;

//   } catch (erro) {
//     display.innerHTML = erro;
//     console.log('DENTRO DO CATCH!');
//     console.log({ erro });
//   } finally {
//     console.log('FINALLY!');
//   }
// }

//btnCEP.addEventListener('click', buscaCEPtry);

// EXEMPLO THE CAT API

const btnCat = document.getElementById('btn-cat');
const imgCat = document.getElementById('img-cat');

async function fetchCat() {
  try {

    const url = 'https://api.thecatapi.com/v1/images/search';
    const resposta = await fetch(url);
    const conteudo = await resposta.json()

    console.log({ conteudo });
    imgCat.src = conteudo[0].url;

  } catch (erro) {
    console.error(erro);
  }
}

btnCat.addEventListener('click', fetchCat);