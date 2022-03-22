function verificar() {
    var numero = Number(window.document.getElementById('numero').value);
    var result = numero % 2 == 0 ? 'Par' : 'Impar';
    var resultado = window.document.getElementById('resultado');
    resultado.innerHTML = `O número ${numero} é ${result}.`;
    console.log(result);
}