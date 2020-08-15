<template>
  <div
    class="item-in-catalog d-flex align-items-center w-75 mx-auto my-4 px-4 border-dark"
    @click="jumpToDetail"
  >
    <b-img :src="src" :alt="name" class="image" />
    <div class="flex-fill ml-5">
      <p>{{ name }}</p>
      <div class="d-flex justify-content-between">
        <div class="d-flex align-items-center">
          <div class="d-flex align-items-center mr-5">
            <p class="mr-5 mb-0">{{ cost }}円</p>
            <div class="d-flex align-items-center">
              <p class="mb-0">×</p>
              <b-input
                :value="numberOfBuy"
                min="1"
                type="number"
                class="number-of-buy"
                @click.stop
                @change="handleChange"
              />
            </div>
          </div>
          <p class="mr-5 mb-0">在庫：{{ stock }}</p>
          <p class="mb-0">産地：{{ area }}</p>
        </div>
        <div class="d-flex align-items-center">
          <Stars :review="review" class="mr-5" />
          <OutlineButton text="削除" :handle-click="remove" />
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
  props: [
    "id",
    "index",
    "imgName",
    "name",
    "cost",
    "propNumberOfBuy",
    "area",
    "stock",
    "review"
  ],
  components: { Stars, OutlineButton },
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  data() {
    return {
      numberOfBuy: this.propNumberOfBuy
    };
  },
  methods: {
    jumpToDetail: function() {
      this.$router.push({ name: "Detail", params: { itemId: this.id } });
    },
    remove: function() {
      alert("remove from cart");
    },
    handleChange: function(value) {
      if (value > 0) {
        this.numberOfBuy = value;
        this.$emit("handle-change", {
          value: value,
          index: this.index
        });
      }
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
    max-width: 300px;
  }

  .number-of-buy {
    width: 45px;
    height: 30px;
    padding: 0;
    text-align: center;
  }
}
</style>
