<template>
<div class="personalCard" :class="[setFlip ? 'flip' : '']" ref="card" @click="handleFlip">
    <div class="front" v-if="show">
        <!--实际上是背面-->
        <div class="pad">
            <div class="personalCard_title">
                <slot name="title"></slot>
            </div>
            <div class="dividing_line">
                {{ LV }}
            </div>
            <div class="personalCard_main">
                <slot name="main"></slot>
            </div>
        </div>
    </div>
    <div class="front cardBack" v-if="!show" ref="cardBack">
        <div class="cardBackBG" ref="cardBackBG"></div>
    </div>
    <div class="back">
        <!--实际上是正面-->
        <div class="pad">
            <div class="personalCard_title_back">
                <slot name="title_back"> </slot>
            </div>
            <div class="dividing_line">
                {{ LV }}
            </div>
            <div class="personalCard_main_back">
                <slot name="main_back"></slot>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: "personalCard",
    props: {
        LV: {
            type: String,
            default: "SSR",
        },
    },
    data() {
        return {
            setFlip: false,
            show: false,
            conter: 0,
        };
    },
    mounted() {
        this.neWClassTransform();
    },
    methods: {
        handleFlip() {
            if (this.setFlip) {
                this.setFlip = false;

                // this.show = true;
                if (this.conter == 0) {
                    this.show = true;
                    this.conter++;
                }
            } else {
                this.setFlip = true;
                // this.show = false;
            }
            console.log(this.setFlip);
        },
        neWClassTransform() {
            let _this = this;
            class Transform {
                constructor(ref1, ref2, ref3) {
                    console.log(ref1);
                    this.ref1 = ref1.ref1;
                    this.ref2 = ref1.ref2;
                    this.ref3 = ref1.ref3;
                    this.size = [
                        (this.W = this.ref1.clientWidth),
                        (this.H = this.ref1.clientHeight),
                    ];
                    this.handleMouseMove = this.handleMouseMove.bind(this);
                    this.setProperty = this.setProperty.bind(this);
                    this.handleMouseLeave = this.handleMouseLeave.bind(this);
                    this.init = this.init.bind(this);
                    console.log(this.X, this.Y);
                    this.setPropertyBG("--W", this.W + "px");
                    this.setPropertyBG("--H", this.H + "px");
                    this.init();
                }
                handleMouseMove(event) {
                    const {
                        offsetX,
                        offsetY
                    } = event;
                    let X;
                    let Y;
                    X = (offsetX - this.W / 2) / 3 / 3;
                    Y = -(offsetY - this.H / 2) / 3 / 3;
                    this.setProperty("--RY", X.toFixed(2));
                    this.setProperty("--RX", Y.toFixed(2));
                    this.setPropertyBG("--BY", 50 - (X / 4).toFixed(2) + "%");
                    this.setPropertyBG("--BX", 50 - (Y / 4).toFixed(2) + "%");
                }
                handleMouseLeave() {
                    this.setProperty("--RY", 0);
                    this.setProperty("--RX", 0);
                    this.setPropertyBG("--BY", "50%");
                    this.setPropertyBG("--BX", "50%");
                }
                setProperty(e, v) {
                    return this.ref2.style.setProperty(e, v);
                }
                setPropertyBG(e, v) {
                    return this.ref3.style.setProperty(e, v);
                }
                init() {
                    this.ref1.addEventListener("mousemove", this.handleMouseMove);
                    this.ref1.addEventListener("mouseleave", this.handleMouseLeave);
                }
            }
            const card = new Transform({
                ref1: _this.$refs.card,
                ref2: _this.$refs.cardBack,
                ref3: _this.$refs.cardBackBG,
            });
        },
    },
};
</script>

<style lang="scss" scoped>
$br: #574b4f;
$bg: #b7a28f;
$br2: #7f574b;

.personalCard {
    min-width: 320px;
    width: 100%;

    height: 100%;
    // padding: 10px;
    transform-style: preserve-3d;
    position: relative;
    transform: perspective(1000rem);
    border-radius: 25px;
    border: 1px solid rgba(255, 255, 255, 0);
    cursor: pointer;
    transition: transform 1s;
    -webkit-transition: transform 1s;

    .front {
        z-index: 2;
    }

    .cardBack {
        width: 100%;
        height: 100%;
        --RX: 0;
        --RY: 0;

        transform: rotateX(calc(var(--RX)*1deg)) rotateY(calc(var(--RY)*1deg));
        -webkit-transform: rotateX(calc(var(--RX)*1deg)) rotateY(calc(var(--RY)*1deg));
        -moz-transform: rotateX(calc(var(--RX)*1deg)) rotateY(calc(var(--RY)*1deg));
        -o-box-transform: rotateX(calc(var(--RX)*1deg)) rotateY(calc(var(--RY)*1deg));

        transition: transform 0.3s;
        -webkit-transition: transform 0.3s;

        .cardBackBG {
            --BX: 50%;
            --BY: 50%;
            --W: 0px;
            --H: 0px;
            padding: 10px;

            border: 1px solid #574b4f;
            border-radius: 25px;
            width: 100%;
            height: 100%;
            position: absolute;
            background: linear-gradient(hsla(0, 0%, 100%, 0.1),
                    hsla(0, 0%, 100%, 0.1)),
                url("../assets/CradBack2.png") no-repeat;
            background-position: var(--BX) var(--BY);
            background-size: var(--H) auto;
        }

        .cardBackBG::before,
        .cardBackBG::after {
            content: "";

            width: 50px;
            height: 50px;

            position: absolute;
            z-index: 2;

            opacity: 1;
            transition: 0.3s;
            border: 5px solid rgb(255, 255, 255);
            border-image: -webkit-linear-gradient(#ec5f67,
                    #f99057c9,
                    #fac863c9,
                    #99c794c9,
                    #5fb3b3c9,
                    #6699ccc9,
                    #c594c5c9) 20 20;
        }

        .cardBackBG::before {
            top: 25px;
            right: 25px;

            border-bottom-width: 0;
            border-left-width: 0;
        }

        .cardBackBG::after {
            bottom: 25px;
            left: 25px;

            border-top-width: 0;
            border-right-width: 0;
        }
    }

    .cardBack:after {
        content: "";
        display: inline-block;
        position: absolute;
        left: -10px;
        top: -10px;
        width: calc(100% + (20px));
        height: calc(100% + (20px));
        z-index: -20;
        filter: blur(50px);
        opacity: 1;
        border: 0 solid #113546;
        border-radius: 25px;
    }

    .back {
        transform: rotateY(180deg);
    }

    .front,
    .back {
        border: 1px solid #888888;
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        border-radius: 25px;
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
        -moz-backface-visibility: hidden;
        -o-backface-visibility: hidden;
        background-image: url("../assets/CradBack3.png");

        background-position: center top;
        background-size: cover;

        .pad {
            margin: 20px;
            width: calc(100% - 40px);
            height: calc(100% - 40px);
            overflow: hidden;

            .personalCard_title,
            .personalCard_title_back {
                font-size: 20px;
                // border-bottom: 1px solid #ccc;
            }

            .personalCard_main,
            .personalCard_main_back {
                font-size: 16px;
            }

            .dividing_line {
                display: flex;
                font-size: 16px;
                font-weight: 800;
                width: 100%;
                text-align: center;
                align-items: center;
                background: -webkit-linear-gradient(#ec5f67,
                        #f99157,
                        #fac863 20%,
                        #99c794 40%,
                        #5fb3b3 60%,
                        #6699cc 80%,
                        #c594c5);
                color: transparent;
                -webkit-background-clip: text;
            }

            .dividing_line::before,
            .dividing_line::after {
                content: "";
                flex: 1;
                height: 1px;
                background: #ccc;
            }

            .dividing_line::before {
                margin-right: 10px;
            }

            .dividing_line::after {
                margin-left: 10px;
            }
        }

        .pad::before {
            content: "";
            width: calc(100% - 40px);
            height: calc(100% - 40px);

            position: absolute;
            top: 20px;
            left: 20px;
            right: 0;
            bottom: 0;
            z-index: -1;
            background-image: url("../assets/CradBack3.png");
            background-position: center top;
            background-size: cover;

            -webkit-filter: blur(5px);
            -moz-filter: blur(5px);
            -ms-filter: blur(5px);
            -o-filter: blur(5px);
            filter: blur(5px);
        }
    }
}

.personalCard:hover .cardBackBG::before,
.personalCard:hover .cardBackBG::after {
    width: calc(100% - 50px);
    height: calc(100% - 50px);
}

.personalCard:hover .cardBack::after {
    background: -webkit-linear-gradient(45deg,
            #ec5f67,
            #f99157,
            #fac863,
            #99c794,
            #5fb3b3,
            #6699cc,
            #c594c5);
    background: linear-gradient(45deg,
            #ec5f67,
            #f99157,
            #fac863,
            #99c794,
            #5fb3b3,
            #6699cc,
            #c594c5);
    box-sizing: inherit;
}

.personalCard:hover .cardBackBG {
    box-shadow: 0px 10px 5px #888888;
    /*设置阴影,可以自定义参数*/
    -webkit-box-shadow: 0px 10px 5px #888888;
    -o-box-shadow: 0px 10px 5px #888888;
    -moz-box-shadow: 0px 10px 5px #888888;
}

.personalCard:hover .back,
.personalCard:hover .front {
    box-shadow: 0px 10px 5px #888888;
    /*设置阴影,可以自定义参数*/
    -webkit-box-shadow: 0px 10px 5px #888888;
    -o-box-shadow: 0px 10px 5px #888888;
    -moz-box-shadow: 0px 10px 5px #888888;
}

.flip {
    transition: transform 1s;
    -webkit-transition: transform 1s;
    transform: rotateY(180deg);
    -webkit-transform: rotateY(180deg);
    -moz-transform: rotateY(180deg);
    -o-transform: rotateY(180deg);
}
</style>
