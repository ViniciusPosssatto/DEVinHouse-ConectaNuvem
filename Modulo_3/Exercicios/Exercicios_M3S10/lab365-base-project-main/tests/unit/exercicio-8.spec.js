import { shallowMount } from "@vue/test-utils";
import Exercicio8 from "@/exercicios/exercicio-8.vue";

// const wrapper = shallowMount(Exercicio8, {
//   data() {
//     return {
//       numeroPaginaAtual: 5,
//     };
//   },
// });

describe("teste component", () => {
  it("Testa o botão de aumentar contagem", async () => {
    const wrapper = shallowMount(Exercicio8, {
      data() {
        return {
          numeroPaginaAtual: 5,
        };
      },
    });
    await wrapper.find("#btn2").trigger("click");
    expect(wrapper.find("h1").text()).toBe("Página atual: 6");
  });
  it("Testa o botão de diminuir contagem", async () => {
    const wrapper = shallowMount(Exercicio8, {
      data() {
        return {
          numeroPaginaAtual: 5,
        };
      },
    });
    await wrapper.find("#btn1").trigger("click");
    expect(wrapper.find("h1").text()).toBe("Página atual: 4");
  });
  it("Testa o botão de diminuir contagem, não zera ou fica negativo", async () => {
    const wrapper = shallowMount(Exercicio8, {
      data() {
        return {
          numeroPaginaAtual: 1,
        };
      },
    });
    await wrapper.find("#btn1").trigger("click");
    expect(wrapper.find("h1").text()).toBe("Página atual: 1");
  });
});
