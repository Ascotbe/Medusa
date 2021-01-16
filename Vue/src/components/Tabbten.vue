<template>
<div class="tabten">
    <div class="tabtenL" @click="handelSetActiveL" ref="tabtenL"></div>
    <div class="tabtenR" @click="handelSetActiveR" ref="tabtenR"></div>
</div>
</template>

<script>
export default {
    name: "tabbten",
    data() {
        return {
            activeL: true,
            activeR: false,
        };
    },
    mounted() {
        this.handelSetActiveL();
    },
    methods: {
        handelSetActiveL() {
            this.$emit("handelSetActiveL");
            this.$refs.tabtenL.style.setProperty("--widthL", "50%");
            this.$refs.tabtenR.style.setProperty("--widthR", "25%");
        },
        handelSetActiveR() {
            this.$emit("handelSetActiveR");
            this.$refs.tabtenR.style.setProperty("--widthR", "50%");
            this.$refs.tabtenL.style.setProperty("--widthL", "25%");
        },
    },
};
</script>

<style lang="scss" scoped>
.tabten {
    height: 25px;
    width: 100%;
    font-size: 16px;
    display: flex;
    flex-wrap: nowrap;
    justify-content: space-between;

    // .activeR {
    //     border-top: 25px solid rgb(122, 255, 128);
    //     width: 50%;
    // }

    // .activeL {
    //     border-bottom: 25px solid rgb(0, 225, 255);
    //     width: 50%;
    // }

    .tabtenL,
    .tabtenR {
        height: 25px;
        width: 25%;
        min-width: 125px;
        cursor: pointer;
    }

    .tabtenL {
        left: 0%;
        --widthL: 25%;
    }

    .tabtenR {
        left: 75%;
        --widthR: 25%;
    }

    .tabtenL:before,
    .tabtenR:before {
        content: "";
        height: 0;
        position: absolute;
        min-width: 125px;
        transition: all 1s;
        -moz-transition: all 1s;
        /* Firefox 4 */
        -webkit-transition: all 1s;
        /* Safari 和 Chrome */
        -o-transition: all 1s;
        /* Opera */
    }

    .tabtenL:before {
        content: "";
        width: var(--widthL);
        left: 0;
        border-top: 25px solid rgb(32, 218, 47);
        border-right: 35px solid transparent;
    }

    .tabtenR:before {
        content: "";
        width: var(--widthR);
        right: 0;
        border-bottom: 25px solid rgba(0, 174, 255, 1);
        border-left: 35px solid transparent;
        animation: WidthLength 2s linear;
        -moz-animation: WidthLength 2s linear;
        /* Firefox */
        -webkit-animation: WidthLength 2s linear;
        /* Safari 和 Chrome */
        -o-animation: WidthLength 2s linear;
        /* Opera */
    }

    @keyframes WidthLength {
        0% {
            width: 25%;
        }

        50% {
            width: 45%;
        }

        100% {
            width: 25%;
        }
    }

    .tabtenL:after,
    .tabtenR:after {
        color: #fff;
        height: 25px;
        position: absolute;
        width: 25%;
        min-width: 125px;
        line-height: 25px;
    }

    .tabtenL:after {
        content: "切换公共模板";
        text-align: left;
        left: 0;
    }

    .tabtenR:after {
        content: "切换个人模板";
        text-align: right;
        color: #fff;
        animation: textAnimation 2s linear;
        -moz-animation: textAnimation 2s linear;
        /* Firefox */
        -webkit-animation: textAnimation 2s linear;
        /* Safari 和 Chrome */
        -o-animation: textAnimation 2s linear;
        /* Opera */
    }

    @keyframes textAnimation {
        0% {
            content: "切换个人模板";
            text-align: right;
            color: #fff;
        }

        50% {
            content: "点我切换";
            text-align: right;
            color: #fff;
        }

        100% {
            text-align: right;
            color: #fff;
            content: "切换个人模板";
        }
    }

    .tabtenL:hover:before {
        border-top: 25px solid rgb(122, 255, 128);
        width: 50%;
        transition: all 1s;
        -moz-transition: all 1s;
        /* Firefox 4 */
        -webkit-transition: all 1s;
        /* Safari 和 Chrome */
        -o-transition: all 1s;
        /* Opera */
    }

    .tabtenR:hover:before {
        border-bottom: 25px solid rgb(0, 225, 255);
        width: 50%;
        transition: all 1s;
        -moz-transition: all 1s;
        /* Firefox 4 */
        -webkit-transition: all 1s;
        /* Safari 和 Chrome */
        -o-transition: all 1s;
        /* Opera */
    }
}
</style>
