<template>
  <div
    class="item-in-catalog d-flex align-items-center w-75 mx-auto my-4 px-4 border-dark"
    @click="jumpToDetail"
  >
    <b-img :src="src" :alt="name" />
    <div class="flex-fill ml-5">
      <p>{{ name }}</p>
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center">
          <div class="d-flex align-items-center mr-5">
            <p class="mr-5 mb-0">{{ cost }}円</p>
            <div class="d-flex align-items-center">
              <p class="mb-0">×</p>
              <b-input
                v-model="numberOfBuy"
                class="number-of-buy"
                @click.stop
              />
            </div>
          </div>
          <p class="mb-0">在庫：{{ stock }}</p>
        </div>
        <div class="d-flex align-items-center">
          <Stars :review="review" class="mr-5" />
          <OutlineButton
            class="add-cart-button"
            text="削除"
            handle-click="remove"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Stars from "@/components/Stars";
import OutlineButton from "@/components/OutlineButton";

export default {
  name: "ItemInCart",
  props: ["imgName", "name", "cost", "propsNumberOfBuy", "stock", "review"],
  components: { Stars, OutlineButton },
  data() {
    return {
      numberOfBuy: this.propsNumberOfBuy
    };
  },
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  methods: {
    jumpToDetail: () => {
      alert("jump to detail!");
    },
    remove: () => {
      alert("remove from cart");
    }
  }
};
</script>

<style lang="scss" scoped>
.item-in-catalog {
  border: 1px solid;
  cursor: pointer;

  &:hover {
    background-color: darken(#fff, 10%);
  }

  .number-of-buy {
    width: 30px;
    height: 30px;
    padding: 0;
    text-align: center;
  }

  .add-cart-button {
    background: none;
    border-color: #ff0070;
    color: #ff0070;

    &:hover {
      background: #ff0070;
      color: #fafafa;
    }
  }
}
</style>
