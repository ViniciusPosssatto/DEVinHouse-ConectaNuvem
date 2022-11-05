import { subtraiNumeros } from "../../src/exercicios/exercicio-6";

describe("Teste da função subtrai números", () => {
  it("Não deve subtrair quando há algum valor inválido", () => {
    expect(subtraiNumeros("letra", null)).toBe("entrada inválida");
  });
  it("Deve retornar o valor correto quando valores são válidos", () => {
    expect(subtraiNumeros(3, 5)).toBe(-2);
  });
  it("Deve realizar a soma caso o segundo valor seja negativo", () => {
    expect(subtraiNumeros(4, -5)).toBe(9);
  });
});
