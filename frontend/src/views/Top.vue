<template>
  <div class="top w-75 mx-auto my-5">
    <section class="menu">
      <h2 class="mb-4">オススメの献立</h2>
      <ul class="d-flex justify-content-between">
        <Menu
          v-for="menu in menus"
          :id="menu.id"
          :img-name="menu.imgName"
          :display-name="menu.displayName"
          :key="menu.id"
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
      menus: []
    };
  },
  created() {
    const path = process.env.VUE_APP_BASE_URL + "api/menus";
    this.$api
      .get(path)
      .then(response => {
        this.menus = response.data;
      })
      .catch(error => {
        console.log(error);
      });
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
