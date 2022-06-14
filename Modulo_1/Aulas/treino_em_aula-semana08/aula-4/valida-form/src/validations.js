
class Validations {
    validaNome(atributo) {
        if(!atributo){
            return 'O campo nome é obrigatório!'
        }

    }
    validaValor(atributo) {
        if(atributo <= 0){
            return 'O campo valor tem que ser maior que zero!'
        }
    }
}
export default new Validations