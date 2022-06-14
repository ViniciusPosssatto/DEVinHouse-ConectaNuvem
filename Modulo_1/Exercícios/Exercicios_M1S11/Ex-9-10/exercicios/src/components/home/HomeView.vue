<template>
  <div class="container mt-3">
      <div class="col-6" v-if="autenticado">
		<h1 class="text-center">Alguma coisa</h1>
		<p>
			Lorem ipsum, dolor sit amet consectetur adipisicing elit. Distinctio neque, obcaecati tempora corrupti ipsa eos dolorum eum optio pariatur mollitia ducimus eligendi. Eos maxime debitis, laboriosam dolor magni non? Quidem.
		</p>
		<p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Non molestias hic facere repellendus iusto quos, asperiores dicta architecto sequi aspernatur, quidem nobis, quibusdam sint! Culpa officia cupiditate saepe repudiandae atque?</p>
		<h3>Outra coisa</h3>
		<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit ex explicabo quam vel, quae labore delectus quod autem assumenda totam sunt itaque obcaecati doloremque! Mollitia perferendis fuga ratione quae deserunt.</p>
		<div class="row">
			<div class="col-6">
				<p>Lorem ipsum dolor Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum consequuntur tempora nulla atque, facilis sed commodi officiis labore possimus consequatur cumque nobis eum maiores dignissimos magnam. Unde voluptatibus quae dolorem. sit amet consectetur, adipisicing elit. Fugit inventore repellendus nam unde tempore nesciunt quam beatae assumenda. Eaque officiis soluta amet eveniet assumenda labore, inventore nesciunt corrupti exercitationem doloribus.</p>
			</div>
			<div class="col-6">
				<p>Lorem ipsum dolor sit amet, Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nemo modi, voluptatibus porro ab possimus voluptates, ratione distinctio officia consectetur odit minima deleniti? Accusantium aspernatur amet, cumque sapiente beatae maiores harum? onsectetur adipisicing elit. Officiis consectetur placeat autem iusto hic sint perferendis, quo quia adipisci quam dolorem deserunt architecto possimus. Tempore ut placeat officiis voluptas repudiandae.</p>
			</div>
		</div>
      </div>
      <div v-else>
		<h3>Para navegar neste local é necessário autenticação!</h3>
		<h5 style="color:red">Crie uma <router-link to="/register">conta</router-link> ter todos os benefícios  ou faça <router-link to="/login">login</router-link> e utilize.</h5>
      </div>
  </div>
</template>

<script>
export default {
    methods: {
      logout() {
        this.$store.commit('autenticaUser/logout');
        this.$router.push('/');
      }
    },
    computed: {
      autenticado(){ 
        return this.$store.state.autenticaUser.autenticado;
      },
      user(){
        return this.$store.state.userModule.user;
      }
    },
    mounted() {
      this.$store.state.autenticaUser.autenticado = localStorage.getItem('token') ? true : false;
    }
  }
</script>

<style>

</style>