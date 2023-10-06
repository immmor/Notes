<template>
    <div class="box">
        <p>
            <input type="text" placeholder="用户名" v-model="state.user">
        </p>
        <p>
            <input type="text" placeholder="密码" v-model="state.pwd">
        </p>
        <p>
            <select v-model="state.role">
                <option :value="ele.value" v-for="ele in state.roleList" :key="ele.value">{{ele.text}}</option>
            </select>
        </p>
        <p>
            <input type="button" value="登录" @click="doLogin">
        </p>
    </div>
</template>

<script setup>
import {reactive} from "vue";
import {useStore} from "vuex";
import {useRouter} from "vue-router";

const router = useRouter();
const store = useStore();
const state = reactive({
    user: "immmor",
    pwd: "12321",
    role: "user",
    roleList: [
        {text: "管理员", value: "admin"},
        {text: "经理", value: "manager"},
        {text: "用户", value: "user"},
    ]
})

function doLogin(){
    const context = {
        token: "412e6632-435a-4b4c-baf5-aedfd496e204",
        role: state.role,
    }
    store.commit('login', context);
    router.replace({name: "basic"});
}
</script>

<style scoped>
.box {
    border: 1px solid #ddd;
    width: 300px;
    margin-top: 200px;
    margin-left: auto;
    margin-right: auto;
    padding: 30px;
}
</style>
  