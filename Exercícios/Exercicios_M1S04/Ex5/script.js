class Endereço{
  constructor(logradouro, numero, cidade, estado, pais, cep){
    this.logradouro = logradouro;
    this.numero = numero;
    this.cidade = cidade;
    this.estado = estado;
    this.pais = pais;
    this.cep = cep;
  }
  local(){
    return `Meu endereço completo é ${this.logradouro}, número ${this.numero}, em ${this.cidade}/${this.estado}/${this.pais} no cep ${this.cep}.`
  }
}

const casa = new Endereço('Rua das palmeiras', 397, 'Florianópolis', 'SC', 'BR', 86522000);
console.log(casa.local());
