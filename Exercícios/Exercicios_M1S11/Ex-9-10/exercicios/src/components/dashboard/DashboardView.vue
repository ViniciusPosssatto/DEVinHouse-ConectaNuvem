<template>
  <div class="container mt-4">
        <div class="row">
            <div class="col-8">
                <h1>Área do User</h1>
                <h4>Seja bem vindo</h4>
            </div>
            <div class="col-4">
                <p>Caso deseje sair clique em logout.</p>
            </div>
        </div>
        <div class="container">
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni aliquam cupiditate nulla incidunt voluptatum error nemo placeat quaerat fugit, neque, quia molestiae est aspernatur mollitia exercitationem repellat, optio alias quibusdam?</p>
        </div>
        <div class="row">
            <div class="col-6">
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Fugit inventore repellendus nam unde tempore nesciunt quam beatae assumenda. Eaque officiis soluta amet eveniet assumenda labore, inventore nesciunt corrupti exercitationem doloribus.</p>
            </div>
            <div class="col-6">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis consectetur placeat autem iusto hic sint perferendis, quo quia adipisci quam dolorem deserunt architecto possimus. Tempore ut placeat officiis voluptas repudiandae.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <p>Lorem ipsum dolor Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta, libero vitae! Dolore possimus exercitationem itaque dolorem! Deleniti, odit ab ipsa voluptatibus harum quas! Adipisci, rem incidunt nostrum reprehenderit consequatur voluptates? sit amet consectetur, adipisicing elit. Fugit inventore repellendus nam unde tempore nesciunt quam beatae assumenda. Eaque officiis soluta amet eveniet assumenda labore, inventore nesciunt corrupti exercitationem doloribus.</p>
            </div>
            <div class="col-6">
                <p>Lorem  Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias ipsa quidem eius ab quos consectetur accusantium officia architecto doloremque expedita assumenda id ducimus, aspernatur rerum delectus fugit, necessitatibus quia consequuntur. ipsum dolor sit amet, consectetur adipisicing elit. Officiis consectetur placeat autem iusto hic sint perferendis, quo quia adipisci quam dolorem deserunt architecto possimus. Tempore ut placeat officiis voluptas repudiandae.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-6">
                <h5>AHAHAHA</h5>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Fugit inventore repellendus nam unde tempore nesciunt quam beatae assumenda. Eaque officiis soluta amet eveniet assumenda labore, inventore nesciunt corrupti exercitationem doloribus.</p>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Fugit inventore repellendus nam unde tempore nesciunt quam beatae assumenda. Eaque officiis soluta amet eveniet assumenda labore, inventore nesciunt corrupti exercitationem doloribus.</p>
            </div>
            <div class="col-6">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officiis consectetur placeat autem iusto hic sint perferendis, quo quia adipisci quam dolorem deserunt architecto possimus. Tempore ut placeat officiis voluptas repudiandae.</p>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    methods: {
        logout(){
            this.$state.dispatch('logout')
        }
    },
    computed: {
        autenticado(){
            return this.$store.state.autenticacaoModule.autenticado; 
        }
    },
    mounted() {
        //this.$store.state.autenticacaoModule.autenticado = localStorage.getItem('autenticado');
    }
}
</script>

<style>

</style>