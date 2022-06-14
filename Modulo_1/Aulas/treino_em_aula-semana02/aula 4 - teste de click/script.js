var a = document.getElementById("area");
a.addEventListener('click', clicar);
a.addEventListener('mouseenter', entrar);
a.addEventListener('mouseout', sair);

function clicar(){
    a.innerText = "clicou";
    a.style.background = "green";
    a.style.color = "black";
}

function entrar(){
    a.innerText = "Entrou";
    a.style.background = "black";
    a.style.color = "white";
}

function sair(){
    a.innerText = "saiu";
    a.background = "red";
    a.style.color = "green";
}

