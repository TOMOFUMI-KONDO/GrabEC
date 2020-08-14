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
          <div class="mr-5">
            <FilledStar v-for="n of review" :key="n" class="mr-1" />
            <StrokeStar
              v-for="n of 5 - review"
              :key="n + review"
              class="mr-1"
            />
          </div>
          <b-button class="add-cart-button" @click.stop="addToCart">
            カートに追加
          </b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FilledStar from "@/components/FilledStar";
import StrokeStar from "@/components/StrokeStar";

export default {
  name: "ItemInCatalog",
  props: ["imgName", "name", "cost", "stock", "review"],
  components: { FilledStar, StrokeStar },
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
