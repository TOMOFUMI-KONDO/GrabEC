<template>
  <div
    class="item-in-catalog d-flex align-items-center w-75 mx-auto my-4 px-4 border-dark"
    @click="jumpToDetail"
  >
    <b-img :src="src" :alt="name" class="image" />
    <div class="flex-fill ml-5">
      <p>{{ name }}</p>
      <div class="d-flex justify-content-between">
        <div class="d-flex">
          <p class="mr-5 mb-0">{{ cost }}円</p>
          <p class="mr-5 mb-0">在庫：{{ stock }}</p>
          <p class="mb-0">産地：{{ area }}</p>
        </div>
        <div class="d-flex align-items-center">
          <Stars :review="review" class="mr-5" />
          <OutlineButton text="カートに追加" :handle-click="addToCart" />
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
  props: ["id", "imgName", "name", "cost", "area", "stock", "review"],
  components: { Stars, OutlineButton },
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  methods: {
    jumpToDetail: function() {
      this.$router.push({ name: "Detail", params: { itemId: this.id } });
    },
    addToCart: function() {
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

  .image {
    max-width: 200px;
    max-height: 200px;
  }
}
</style>
