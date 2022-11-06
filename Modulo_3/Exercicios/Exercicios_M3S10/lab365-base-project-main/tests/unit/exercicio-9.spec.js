import { shallowMount } from "@vue/test-utils";
import Exercicio9 from "@/exercicios/exercicio-9.vue";

describe("teste component", () => {
  it("Testa o botão de salvar antes de clicar", async () => {
    const wrapper = shallowMount(Exercicio9, {
      propsData: {
        loading: false,
      },
    });
    // await wrapper.find("button").trigger("click");
    expect(wrapper.find("button").text()).toBe("Salvar");
  });
  it("Testa o botão de salvar", async () => {
    const wrapper = shallowMount(Exercicio9, {
      propsData: {
        loading: true,
      },
    });
    await wrapper.find("button").trigger("click");
    expect(wrapper.find("button").text()).toBe("Carregando...");
  });
});
