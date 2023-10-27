<template>
    <h1>Basic</h1>
    <ul>
        <li v-if="hasPermission(['admin', 'manager'])">查看</li>
        <li>新增</li>
        <li v-permission="['admin', 'manager']">修改</li>
        <li>删除</li>
    </ul>
</template>
<script setup>
// import { useStore } from 'vuex';
import { onMounted } from 'vue';
import { hasPermission } from '@/store/permission';
// const store = useStore();



onMounted(()=>{
    initPage();
})

function initPage(){
    // if (allowRoleList.indexOf(store.state.role) !== -1) {
    //     return true;
    // }
    if (!hasPermission(['admin', 'manager'])) {
        return true;
    }
}
</script>

<style scoped>

</style>
  