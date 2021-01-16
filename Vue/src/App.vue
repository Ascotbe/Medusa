<template>
<div id="app">
    <template>
        
            <router-view />
     
    </template>
</div>
</template>

<script>
export default {
    data() {
        return {

        };
    },
};
</script>

<style lang="scss">
/* 定义 */
@font-face {
    font-family: 'Lato';
    src: url('./commonFont/Lato-Regular.ttf');
    font-weight: normal;
    font-style: normal;

}

@font-face {
    font-family: 'NotoSans';
    src: url('./commonFont/NotoSans-Regular.ttf');
    font-weight: normal;
    font-style: normal;
}

body {
    margin: 0;
    padding: 0;

}

html,
body,
#app {

    font-family: 'Lato', 'NotoSans';
    height: 100%;
    overflow: hidden;
}

#app {
    font-family: 'Lato', 'NotoSans';
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    word-wrap: break-word;
}
</style>
