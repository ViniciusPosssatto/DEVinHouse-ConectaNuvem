import { verificaPalavraNoTexto } from "../../src/exercicios/exercicio-7";

describe("Teste da função que verifica palavras em um texto", () => {
  it("Retorna false se não encontrar a palavra no texto", () => {
    expect(verificaPalavraNoTexto("234234", "teste")).toBe(false);
  });
  it("Retorna true se encontrar a palavra no texto", () => {
    expect(verificaPalavraNoTexto("teste da função", "teste")).toBe(true);
  });
  it("Não executa se for string vazia para o texto", () => {
    expect(verificaPalavraNoTexto("", "asdas")).toBe("informe um texto");
  });
  it("Não executa se for string vazia para a palavra", () => {
    expect(verificaPalavraNoTexto("as asdasd", "")).toBe("informe uma palavra");
  });
});
