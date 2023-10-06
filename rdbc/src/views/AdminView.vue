<template>
    <div class="pg-header"></div>
    <div class="pg-body">
        <div class="left-menu">
            <router-link v-for="item in routerList" :to="{name: 'basic'}">{{item.title}}</router-link>
        </div>
        <div class="right-content" style="flex-grow:1">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup>
import {computed} from "vue";
import {useRouter} from "vue-router";

const router = useRouter();
const routerList = computed(() => {
    // let role = store.state.role;
    // let routerData = router.getRoutes().filter(item => {
    //     if (item.meta.title && item.meta.role.indexOf(role) !== -1) {
    //         return item;
    //     }
    // })
    console.log(router);
    return [];
})
</script>

<style scoped>
.pg-header {
    height: 48px;
    background-color: brown;
}

.pg-body {
    display: flex;
    flex-direction: row;
}

.pg-body .left-menu {
    width: 290px;
    background-color: aliceblue;
    height: calc(100vh - 48px);
}

.pg-body .left-menu a {
    display: block;
    padding: 8px 10px;
    border-bottom: 1px solid #dddddd;
}

.pg-body .right-content {
    background-color: antiquewhite;
    height: calc(100vh - 48px)
}
</style>
  