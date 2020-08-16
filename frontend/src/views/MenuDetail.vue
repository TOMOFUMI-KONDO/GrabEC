<template>
  <div class="menu-detail">
    <div
      class="d-flex justify-content-around align-items-center w-75 mx-auto my-5"
    >
      <b-img :src="menuImgSrc" :alt="menuName" class="image" />
      <div>
        <p class="menu-name">{{ menuName }}</p>
        <p>{{ menuDescription }}</p>
      </div>
    </div>
    <section v-if="isExistItem()">
      <h2 class="mt-5 text-center font-weight-bold">必要な食材一覧</h2>
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
    </section>
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
      menuImgName: "oval.svg",
      menuName: "",
      menuDescription: "",
      itemIds: [],
      items: []
    };
  },
  computed: {
    menuImgSrc() {
      return require("@/assets/images/" + this.menuImgName);
    }
  },
  methods: {
    addAllToCart() {
      alert("全ての必要な食材をカートに追加しました。");
    },
    isExistItem() {
      return this.items.length > 0;
    }
  },
  async created() {
    let path = process.env.VUE_APP_BASE_URL + "api/menu/" + this.menuId;
    await this.$api
      .get(path)
      .then(response => {
        const data = response.data;
        this.menuImgName = data.imgName;
        this.menuName = data.displayName;
        this.menuDescription = data.description;
      })
      .catch(error => {
        console.log(error);
      });

    path = process.env.VUE_APP_BASE_URL + "api/materials/" + this.menuId;
    await this.$api
      .get(path)
      .then(response => {
        this.itemIds = response.data;
      })
      .catch(error => {
        console.log(error);
      });
    for (const itemId of this.itemIds) {
      path = process.env.VUE_APP_BASE_URL + "api/product/" + itemId;
      console.log(path);
      await this.$api
        .get(path)
        .then(response => {
          this.items.push(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.menu-detail {
  .image {
    max-width: 300px;
    max-height: 300px;
  }

  .menu-name {
    font-size: 24px;
    font-weight: bold;
  }

  .item-list {
    list-style: none;
  }
}
</style>
