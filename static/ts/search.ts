import { createApp } from 'vue';
import axios from "axios";
console.log("test");
    const app = createApp({
        data() {
            return {
                value: [],
                result:null,
                flag: false,
                msg:"メインのキャラを選んでください。"
            }
        },
        compilerOptions: {
            delimiters: ['[[', ']]'],
        },
        methods: {
            getData() {
                console.log(document.getElementById("#selection")?.getAttribute("value"));
                axios.post("{% url 'search' %}", 
                {choice: document.getElementById("selection")?.getAttribute("value")})
                    .then(response => {
                        this.result = response.data;
                        this.value=JSON.parse(this.result);
                        console.log(this.value);
                        this.flag = true;
                    })
                    .catch(error => {
                        console.error(error);
                    });
                    
            }
        },
    });
    app.mount('#app');