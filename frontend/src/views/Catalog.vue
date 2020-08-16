<template>
  <ul class="catalog">
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
  name: "Catalog",
  components: { ItemInCatalog },
  data() {
    return {
      items: []
    };
  },
  created() {
    const path = process.env.VUE_APP_BASE_URL + "api/products";
    this.$api
      .get(path)
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>

<style lang="scss" scoped>
.catalog {
  list-style: none;
}
</style>
