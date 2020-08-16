<template>
  <div class="search-window position-relative">
    <b-input
      v-model="searchWord"
      v-on:keyup.enter="search"
      placeholder="キーワードから商品を探す"
      class="search-input"
    />
    <b-icon icon="search" class="search-icon" />
  </div>
</template>

<script>
export default {
  name: "SearchWindow",
  data() {
    return {
      searchWord: ""
    };
  },
  methods: {
    search() {
      if (this.$router.currentRoute.name === "SearchResult") {
        console.log("hoge");
        this.$store.commit("onSearchWordStateChanged", this.searchWord);
      } else {
        this.$router
          .push({
            name: "SearchResult",
            params: { searchWord: this.searchWord }
          })
          .catch(() => {});
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.search-window {
  min-width: 400px;

  > * {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
  }

  .search-input {
    width: 100%;
  }

  .search-icon {
    right: 10px;
    color: #111;
  }
}
</style>
