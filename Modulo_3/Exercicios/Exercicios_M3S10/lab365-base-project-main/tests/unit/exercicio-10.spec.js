import { shallowMount } from "@vue/test-utils";
import Exercicio10 from "@/exercicios/exercicio-10.vue";

describe("teste component", () => {
  it("Testa média final aprovado", async () => {
    const wrapper = shallowMount(Exercicio10, {
      data() {
        return {
          mediaFinal: null,
        };
      },
    });
    const textInput = wrapper.find('[name="input-value"');
    await textInput.setValue(8);
    expect(wrapper.find("h1").text()).toMatch("Média final: 8");
    expect(wrapper.find("h3").text()).toMatch("Parabéns! Você foi aprovado");
  });
  it("Testa média final reprovado", async () => {
    const wrapper = shallowMount(Exercicio10, {
      data() {
        return {
          mediaFinal: null,
        };
      },
    });
    const textInput = wrapper.find('[name="input-value"');
    await textInput.setValue(4);
    expect(wrapper.find("h1").text()).toMatch("Média final: 4");
    expect(wrapper.find("h3").text()).toMatch(
      "Poxa, infelizmente você reprovou"
    );
  });
  it("Testa média final em recuperação", async () => {
    const wrapper = shallowMount(Exercicio10, {
      data() {
        return {
          mediaFinal: null,
        };
      },
    });
    const textInput = wrapper.find('[name="input-value"');
    await textInput.setValue(6);
    expect(wrapper.find("h1").text()).toMatch("Média final: 6");
    expect(wrapper.find("h3").text()).toMatch(
      "Quase! Você está em exame mas ainda tem chaneces"
    );
  });
});
