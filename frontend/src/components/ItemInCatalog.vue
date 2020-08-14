<template>
  <div
    class="item-in-catalog d-flex align-items-center w-75 mx-auto my-4 px-4 border-dark"
    @click="jumpToDetail"
  >
    <b-img :src="src" :alt="name" />
    <div class="flex-fill ml-5">
      <p>{{ name }}</p>
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <p class="mr-5 mb-0">{{ cost }}円</p>
          <p class="mb-0">在庫：{{ stock }}</p>
        </div>
        <div class="d-flex align-items-center">
          <Stars :review="review" class="mr-5" />
          <OutlineButton
            class="add-cart-button"
            text="カートに追加"
            handle-click="addToCart"
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
  name: "ItemInCatalog",
  props: ["imgName", "name", "cost", "stock", "review"],
  components: { Stars, OutlineButton },
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  methods: {
    jumpToDetail: () => {
      alert("jump to detail!");
    },
    addToCart: () => {
      alert("add to cart");
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
