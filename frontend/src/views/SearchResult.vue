<template>
  <ul v-if="items.length > 0" class="search-result">
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
</template>

<script>
import ItemInCatalog from "@/components/ItemInCatalog";

export default {
  name: "SearchResult",
  props: ["propsSearchWord"],
  components: { ItemInCatalog },
  data() {
    return {
      searchWord: this.propsSearchWord,
      items: []
    };
  },
  methods: {
    getProducts() {
      console.log("getProducts");
      const path =
        process.env.VUE_APP_BASE_URL +
        "api/products/" +
        (this.searchWord === undefined
          ? this.$store.getters.searchWordState
          : this.searchWord);
      this.$api
        .get(path)
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getProducts();
  },
  mounted() {
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === "onSearchWordStateChanged") {
        this.searchWord = state.searchWord;
        this.getProducts();
      }
    });
  }
};
</script>

<style lang="scss" scoped>
.search-result {
  list-style: none;
}
</style>
