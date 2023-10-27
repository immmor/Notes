import store from '@/store';

export default{
    mounted(el, bindings) {
        let allowRoleList = bindings.value;
        let userRole = store.state.role;

        if (allowRoleList.indexOf(userRole) === -1) {
            // 没有权限
            el.parentNode && el.parentNode.removeChild(el);
        }   
    }
}