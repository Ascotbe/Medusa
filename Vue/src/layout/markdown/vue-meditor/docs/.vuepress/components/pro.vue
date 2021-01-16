<template>
    <div class="simple">
        <Markdown :height="400" theme="dark" v-model="value" :toolbars="toolbars"/>
    </div>
</template>

<script>
    import Markdown from '../../../src/components/pro';
    import doc from './doc';

    export default {
        name: "simple",
        components:{
            Markdown
        },
        data(){
            return {
                value:doc,
                toolbars:{
                    redo:false,
                    undo:false
                }
            }
        }
    }
</script>
