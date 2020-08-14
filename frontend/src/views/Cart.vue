<template>
  <ul class="catalog">
    <li v-for="(item, index) in items" :key="index">
      <ItemInCart
        :img-name="item.imgName"
        :name="item.name"
        :cost="item.cost"
        :props-number-of-buy="item.numberOfBuy"
        :stock="item.stock"
        :review="item.review"
      />
    </li>
  </ul>
</template>

<script>
import ItemInCart from "@/components/ItemInCart";

export default {
  name: "Cart",
  components: { ItemInCart },
  data() {
    return {
      items: [
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          stock: 10,
          review: 3
        },
        {
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
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
