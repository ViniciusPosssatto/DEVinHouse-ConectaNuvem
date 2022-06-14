


function progressaoA(){
 
    var tn1 = Number(document.getElementById('txtn1').value);
    var tn2 = Number(document.getElementById('txtn2').value);
    var tn3 = Number(document.getElementById('txtn3').value);
    var pa = '';
    var resultado = window.document.getElementById('resultado');
    var botaoA = document.getElementById('botaoA');

    //peguei esse for da internet e adaptei para as minhas variáveis
    for(var count=1; count<=tn3 ; count++){
        pa += "</br>"+"Termo "+count+" = "+tn1;
          tn1 += tn2;
       }
       var tn1 = Number(document.getElementById('txtn1').value); //tive que recolocar aqui, pois estava puxando a tn1 somado ao tn2
       resultado.innerHTML = `A progressão aritmética de ${tn1} com raiz de ${tn2} por ${tn3} vezes é essa ${pa}`;
}
botaoA.addEventListener('click', progressaoA);

function progressaoG(){
 
  var tn1 = Number(document.getElementById('txtn1').value);
  var tn2 = Number(document.getElementById('txtn2').value);
  var tn3 = Number(document.getElementById('txtn3').value);
  var pa = '';
  var resultado = window.document.getElementById('resultado');
  var botaoG = document.getElementById('botaoG');
  //peguei esse for da internet e adaptei para as minhas variáveis
  for(var count=1; count<=tn3 ; count++){
      pa += "</br>"+"Termo "+count+" = "+tn1;
        tn1 *= tn2;
     }
     var tn1 = Number(document.getElementById('txtn1').value); //tive que recolocar aqui, pois estava puxando a tn1 somado ao tn2
     resultado.innerHTML = `A progressão aritmética de ${tn1} com raiz de ${tn2} por ${tn3} vezes é essa ${pa}`;
}

botaoG.addEventListener('click', progressaoG);

    