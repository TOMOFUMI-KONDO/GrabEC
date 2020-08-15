<template>
  <div class="top w-75 mx-auto my-5">
    <section class="menu">
      <h2 class="mb-4">オススメの献立</h2>
      <ul class="d-flex justify-content-between">
        <Menu
          v-for="menu in menus"
          :img-name="menu.imgName"
          :display-name="menu.displayName"
          :key="menu.imgName"
        />
      </ul>
    </section>
    <section class="search-window">
      <h2 class="mb-4">商品を検索</h2>
      <SearchWindow />
    </section>
  </div>
</template>

<script>
import Menu from "@/components/Menu";
import SearchWindow from "@/components/SearchWindow";

export default {
  name: "Top",
  components: { SearchWindow, Menu },
  data() {
    return {
      menus: [
        { imgName: "卵焼き.jpg", displayName: "和食" },
        { imgName: "オムライス.jpg", displayName: "洋食" },
        { imgName: "餃子.jpg", displayName: "中華" }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.top {
  .menu {
    ul {
      list-style: none;
      padding-left: 0;

      li {
        img {
          max-width: 300px;
        }
      }
    }
  }
}
</style>
