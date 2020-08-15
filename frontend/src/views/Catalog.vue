<template>
  <ul class="catalog">
    <li v-for="(item, index) in items" :key="index">
      <ItemInCatalog
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
      items: [
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.catalog {
  list-style: none;
}
</style>
