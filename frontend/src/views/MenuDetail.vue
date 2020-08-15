<template>
  <div class="menu-detail">
    <div
      class="d-flex justify-content-around align-items-center w-75 mx-auto my-5"
    >
      <b-img :src="menuImgSrc" :alt="menuName" />
      <div>
        <p class="menu-name">{{ menuName }}</p>
        <p>{{ menuDescription }}</p>
      </div>
    </div>
    <h2 class="text-center font-weight-bold">必要な食材一覧</h2>
    <ul class="item-list">
      <li v-for="item in items" :key="item.id">
        <ItemInCatalog
          :id="item.id"
          :img-name="item.imgName"
          :name="item.name"
          :cost="item.cost"
          :area="item.area"
          :stock="item.stock"
          :review="item.review"
        />
      </li>
    </ul>
    <div class="text-center my-5">
      <OutlineButton
        text="まとめてカートに追加"
        :handle-click="addAllToCart"
        class="py-3 px-4"
      />
    </div>
  </div>
</template>

<script>
import ItemInCatalog from "@/components/ItemInCatalog";
import OutlineButton from "@/components/OutlineButton";

export default {
  name: "MenuDetail",
  props: ["menuId"],
  components: { OutlineButton, ItemInCatalog },
  data() {
    return {
      //todo: データベースから取得してくる
      menuImgName: "ベーコン.jpg",
      menuName: "焼きベーコン",
      menuDescription:
        "おいしいですよ。おいしいですよ。おいしいですよ。おいしいですよ。おいしいですよ。おいしいですよ。",
      items: [
        {
          id: 1,
          imgName: "ベーコン.jpg",
          name: "ベーコン　500g",
          cost: 100,
          area: "東京",
          stock: 10,
          review: 2
        },
        {
          id: 2,
          imgName: "ベーコン.jpg",
          name: "ベーコン　500g",
          cost: 1000,
          area: "東京",
          stock: 100,
          review: 4
        }
      ]
    };
  },
  computed: {
    menuImgSrc() {
      return require("@/assets/images/" + this.menuImgName);
    },
    itemImgSrcs() {
      let srcs;
      for (const item of this.items) {
        srcs.push(require("@/assets/images/" + item.imgName));
      }
      return srcs;
    }
  },
  methods: {
    addAllToCart() {
      alert("全ての必要な食材をカートに追加しました。");
    }
  }
};
</script>

<style lang="scss" scoped>
.menu-detail {
  .menu-name {
    font-size: 24px;
    font-weight: bold;
  }

  .item-list {
    list-style: none;
  }
}
</style>
