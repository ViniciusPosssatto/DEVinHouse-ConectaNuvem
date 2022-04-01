
function produto(...num){
    return num.reduce((acc, numero) => acc + numero, 0)    
}

export default produto;
