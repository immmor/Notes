import store from '@/store/index';

export function hasPermission(allowRoleList){
    
    if (allowRoleList.indexOf(store.state.role) !== -1) {
        return true;
    }
}