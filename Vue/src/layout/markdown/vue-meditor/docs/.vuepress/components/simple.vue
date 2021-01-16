<template>
    <div class="simple">
        <Markdown :height="400" theme="oneDark" v-model="value"/>
    </div>
</template>

<script>
    import Markdown from '../../../src/components/simple';
    import doc from './doc';

    export default {
        name: "simple",
        components:{
            Markdown
        },
        data(){
            return {
                value:doc
            }
        }
    }
</script>
