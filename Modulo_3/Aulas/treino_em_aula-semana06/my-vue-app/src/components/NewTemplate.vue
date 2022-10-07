<template>
    <v-form v-model="valid">
    <v-container>
        <v-row>
        <v-col
            cols="12"
            md="4"
        >
            <v-text-field
            v-model="name"
            :rules="nameRules"
            :counter="10"
            label="First name"
            required
            ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="4"
        >
            <v-text-field
            v-model="idade"
            :rules="nameRules"
            :counter="10"
            label="Last name"
            required
            ></v-text-field>
        </v-col>

        <v-col
            cols="12"
            md="4"
        >
            <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            ></v-text-field>
        </v-col>
        </v-row>
        <div class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height">
            <v-btn
            variant="outlined"
            @click="createUser()"
            >
                click
            </v-btn>
        </div>
    </v-container>
    </v-form>
</template>

<script>
import axios from 'axios'
export default {
    data: () => ({
    valid: false,
    name: '',
    idade: '',
    nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
    ],
    }),
    methods: {
        getUser() {  // realiza a busca do cep e preenche alguns campos no formulário
        axios.get(`https://sample-devhouse-1ded3-default-rtdb.firebaseio.com/users.json`)
        .then((response) => {
            console.log(response)
            // this.name = response.data.localidade;
            // this.idade = response.data.localidade;
        }) .catch ((error) => {
            console.log(error.message)
        })
    },
        createUser() {  // realiza a busca do cep e preenche alguns campos no formulário
        axios.post(`https://sample-devhouse-1ded3-default-rtdb.firebaseio.com/users.json`, {"name": this.name, "idade": this.idade})
        .then((response) => {
            console.log(response)
            // this.name = response.data.localidade;
            // this.idade = response.data.localidade;
        }) .catch ((error) => {
            console.log(error.message)
        })
    }
    }
}
</script>