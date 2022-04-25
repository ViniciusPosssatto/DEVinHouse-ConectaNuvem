class ValidacaoV {
    validarCampos(atributo) {
        if(!atributo) {
           // console.log(atributo)
            return `Este campo é obrigatório!`
        }
        return true
    }
    validarValor(valor) {
        if(valor <= 0) {
            return `O valor deve ser maior que zero!`
        }
    }
}
export default new ValidacaoV()