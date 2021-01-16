<template>
<div class="scroll" ref="scroll">
    <div class="head">
        <div class="top" :style="{ width: towWidth }"></div>
        <div class="top_right" :style="{ left: top_right_Left }"></div>
        <div class="top_right_bottom" :style="{ left: top_right_bottom_Left }"></div>
        <div class="top_right_bottom_hr_top" :style="{ left: top_right_bottom_hr_top_Left }"></div>
        <div class="top_right_bottom_hr_bottom" :style="{ left: top_right_bottom_hr_bottom_Left }"></div>
        <div class="nav_top" :style="{ width: nav_top_Width }"></div>
    </div>
    <div class="main">
        <div class="nav" :style="{ width: nav_top_Width }">
            <div class="title">
                <slot name="title"></slot>
            </div>
            <div class="main">
                <slot name="main"></slot>
            </div>
        </div>
    </div>
    <div class="tail">
        <div class="nav_bottom" :style="{ width: nav_top_Width }"></div>
        <div class="bottom" :style="{ width: towWidth }"></div>
        <div class="bottom_left"></div>
        <div class="bottom_left_top" :style="{ width: bottom_left_top_Width }"></div>
        <div class="bottom_right" :style="{ left: bottom_right_Left }"></div>
        <div class="bottom_right_top" :style="{ left: bottom_right_top_Left }"></div>
    </div>
</div>
</template>

<script>
export default {
    name: "test",
    data() {
        return {
            towWidth: "",
            top_right_Left: "",
            top_right_bottom_Left: "",
            top_right_bottom_hr_top_Left: "",
            top_right_bottom_hr_bottom_Left: "",
            nav_top_Width: "",
            bottom_left_top_Width: "",
            bottom_right_Left: "",
            bottom_right_top_Left: "",
        };
    },
    mounted() {
        this.setOption();
        window.addEventListener("resize", () => {
            this.$nextTick(() => {
                this.setOption();
            });
        });
    },

    methods: {
        setOption() {
            let width = this.$refs.scroll.clientWidth;
            if (width > 300) {
                this.towWidth = width - 150 + 1 + "px";
                this.top_right_Left = width - 100 + "px";
                this.top_right_bottom_Left = width - 50 + "px";
                this.top_right_bottom_hr_top_Left = width - 100 + "px";
                this.top_right_bottom_hr_bottom_Left = width - 100 + "px";
                this.nav_top_Width = width - 200 + 1 + "px";
                this.bottom_left_top_Width = width - 175 + 1 + "px";
                this.bottom_right_Left = width - 200 + 1 + "px";
                this.bottom_right_top_Left = width - 200 + 1 + "px";
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.scroll {
    // padding: 10px;
    width: 100%;
    height: 500px;
    box-sizing: border-box;
    margin: 0 auto;

    .head {
        height: 75px;
        position: relative;

        .top {
            background: rgba(242, 235, 217, 1);
            left: 100px;
            position: absolute;
            height: 50px;
            width: 400px;
            border-top: 1px solid #000;
            border-left: 1px solid #000;
            border-top-left-radius: 50px;
        }

        .top_right {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            left: 449px;
            height: 50px;
            width: 100px;
            border-top: 1px solid #000;
            border-left: 1px solid #000;
            border-right: 1px solid #000;
            border-top-left-radius: 50px;
            border-top-right-radius: 50px;
        }

        .top_right_bottom {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            left: 499px;
            top: 50px;
            height: 25px;
            width: 50px;
            border-bottom: 1px solid #000;
            border-left: 1px solid #000;
            border-right: 1px solid #000;
            border-bottom-right-radius: 25px;
            border-bottom-left-radius: 25px;
        }

        .top_right_bottom_hr_top {
            position: absolute;
            left: 450px;
            top: 50px;
            height: 25px;
            width: 50px;
            border-top: 1px solid rgba(0, 0, 0, 0.2);
        }

        .top_right_bottom_hr_bottom {
            position: absolute;
            left: 450px;
            top: 50px;
            height: 25px;
            width: 75px;
            border-top-right-radius: 50px;
            border-bottom: 1px solid rgba(0, 0, 0, 0.2);
        }

        .nav_top {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            left: 100px;
            top: 50px;
            width: 350px;
            height: 25px;
            border-right: 1px solid #000;
            border-left: 1px solid #000;
            text-align: center;
        }
    }

    .main {
        position: relative;
        min-width: 100px;
        min-height: 25px;

        .nav {
            background: rgba(242, 235, 217, 1);
            margin-left: 100px;
            width: 350px;
            min-height: 25px;
            border-right: 1px solid #000;
            border-left: 1px solid #000;

            .title {
                text-align: center;
                font-size: 25px;
            }

            .main {
                font-size: 16px;
            }
        }
    }

    .tail {
        position: relative;
        height: 75px;

        .nav_bottom {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            left: 100px;
            width: 350px;
            height: 25px;
            border-right: 1px solid #000;
            // border-left: 1px solid #000;
        }

        .bottom {
            position: absolute;
            top: 25px;
            left: 50px;
            height: 50px;
            width: 400px;
            border-bottom: 1px solid #000;
            border-right: 1px solid #000;
            border-bottom-right-radius: 50px;
        }

        .bottom_left {
            position: absolute;
            top: 25px;
            left: 1px;
            height: 50px;
            width: 100px;
            // border-top:1px solid #000;
            border-bottom: 1px solid #000;
            border-left: 1px solid #000;
            // border-right: 1px solid #000;
            border-bottom-left-radius: 50px;
            // border-bottom-right-radius: 50px;
        }

        .bottom_left_top {
            background: rgba(255, 255, 255, 1);
            position: absolute;
            left: 1px;
            height: 25px;
            width: 375px;
            border-top: 1px solid #000;
            border-left: 1px solid #000;
            border-top-left-radius: 25px;
        }

        .bottom_right {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            top: 25px;
            left: 350px;
            height: 50px;
            width: 100px;
            border-bottom: 1px solid #000;
            border-left: 1px solid #000;
            border-right: 1px solid #000;
            border-bottom-left-radius: 50px;
            border-bottom-right-radius: 50px;
        }

        .bottom_right_top {
            background: rgba(242, 235, 217, 1);
            position: absolute;
            left: 350px;
            height: 25px;
            width: 26px;
            border-top: 1px solid #000;
            border-left: 1px solid #000;
            border-top-left-radius: 25px;
        }
    }
}
</style>
