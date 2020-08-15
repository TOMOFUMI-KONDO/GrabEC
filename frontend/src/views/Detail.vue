<template>
  <div class="detail d-flex align-items-center w-75 mx-auto my-5">
    <b-img :src="src" :alt="name" class="w-25 mr-5" />
    <div class="flex-fill ml-5">
      <p class="name">{{ name }}</p>
      <div class="d-flex justify-content-between">
        <div>
          <div class="d-flex">
            <Tag
              v-for="(tag, index) in tags"
              :name="tag"
              :key="index"
              class="mx-1"
            />
          </div>
          <Stars :review="review" class="mb-4" />
          <p>在庫：{{ stock }}</p>
          <p>産地：{{ area }}</p>
        </div>
        <div class="d-flex flex-column align-items-end">
          <p class="cost">
            <span>{{ cost }}</span>
            円
          </p>
          <div class="d-flex align-items-center mb-4">
            <p class="mb-0">×</p>
            <b-input
              v-model="numberOfBuy"
              min="1"
              type="number"
              class="input"
            />
          </div>
          <OutlineButton
            text="カートに追加"
            :handle-click="addToCart"
            class="px-4 py-3"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Stars from "@/components/Stars";
import OutlineButton from "@/components/OutlineButton";
import Tag from "@/components/Tag";

export default {
  name: "Detail",
  props: ["itemId"],
  components: { Stars, OutlineButton, Tag },
  data() {
    return {
      //todo: データベースから取得するようにする
      imgName: "ベーコン.jpg",
      name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
      tags: ["野菜", "生鮮食品"],
      cost: 100,
      stock: 10,
      area: "東京",
      review: 4,
      numberOfBuy: 1
    };
  },
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  methods: {
    addToCart() {
      alert("Item was added to cart.");
    }
  }
};
</script>

<style lang="scss" scoped>
.detail {
  font-size: 20px;

  .name {
    font-size: 32px;
  }

  .cost {
    > span {
      font-size: 62px;
      font-weight: bold;
    }
  }

  .input {
    width: 45px;
    padding: 0;
    text-align: center;
  }
}
</style>
