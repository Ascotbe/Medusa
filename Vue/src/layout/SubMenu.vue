<template>
<a-sub-menu :key="menuInfo.key" v-bind="$props" v-on="$listeners">
    <span slot="title">
        <myicon :type="menuInfo.iconType" />
        <span>{{ menuInfo.msg }}</span>
    </span>
    <template v-for="item in menuInfo.children">
        <a-menu-item v-if="!item.children" :key="item.key" @click="handleGoChange">
            <span>{{ item.msg }}</span>
        </a-menu-item>
    </template>
</a-sub-menu>
</template>

<script>
import {
    Icon
} from "ant-design-vue";
const MyIcon = Icon.createFromIconfontCN({
    scriptUrl: "//at.alicdn.com/t/font_1734998_261bksb0z5p.js",
});
import {
    Menu
} from "ant-design-vue";
export default {
    components: {
        myicon: MyIcon,
    },
    name: "SubMenu",
    // must add isSubMenu: true
    isSubMenu: true,
    props: {
        ...Menu.SubMenu.props,
        // Cannot overlap with properties within Menu.SubMenu.props
        menuInfo: {
            type: Object,
            default: () => ({}),
        },
        handleGoChange: {
            default: (e) => {
                console.log(e);
            },
            type: [Function],
        },
    },
    methods: {},
};
</script>

<style>
</style>
