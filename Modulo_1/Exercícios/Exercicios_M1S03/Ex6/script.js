function calcularIdade() {
    dateString = document.getElementById('dataNasc').valueAsDate;
    if(dateString==null || dateString=='') {  
        document.getElementById("mensagem").innerHTML = "Escolha uma data!";    
        return false;   
      } else {  
        dateString = document.getElementById('dataNasc').valueAsDate;
        
        niver = new Date(dateString);
        
        idade = Math.floor((Date.now() - niver) / (31557600000));
        
        if (idade < 1){ //para o caso e ser menor que 1 ano de idade
            resposta = `Você ainda não tem 1 ano de idade completo!`;
        } else {
            if (idade == 1){ //para o caso de ser 1 ano e não ficar no plural (anos)
                resposta = `Você tem ${idade} ano de idade!`;
            } else {
                resposta = `Você tem ${idade} anos!`;
            }
        document.getElementById("idade").innerHTML = resposta    
        }
        console.log(idade);
    };
};