<template>
    <div class="preview">
        <Preview :initialValue="value"/>
    </div>
</template>

<script>
    import Preview from '../../../src/preview';
    import doc from './doc';
    export default {
        name: "preview",
        components:{Preview},
        data() {
            return {
                value:doc
            }
        },
        mounted() {

        },
        methods: {}
    }
</script>
