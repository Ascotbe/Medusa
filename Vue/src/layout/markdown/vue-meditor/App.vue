<template>
    <div>
        <Markdown
            v-model="val"
            @on-ready="onReady"
            @on-copy="onCopy"
            @on-upload-image="onUpladImage"
            @on-save="onSave"
            :height="500"
        />
    </div>
</template>

<script>
    // import Markdown from './dist/simple';
    // import Markdown from 'vue-meditor';
    import Markdown from './src/pro';
    // import Markdown from './src/simple';

    export default {
        components: {
            Markdown
        },
        data: function () {
            return {
                val: ''
            }
        },
        methods: {
            onReady(data) {
                console.log(data)
            },
            onCopy(text) {
                console.log(text);
            },
            onUpladImage(file) {
                console.log(file)
            },
            onSave(data) {
                console.log(data);
            }
        }
    }
</script>

<style lang="less">

</style>
