<template>
  <div>
    <div class="d-flex justify-content-center my-5">
      <PriceSum :sum="sum" class="mr-5" />
      <div class="my-auto">
        <OutlineButton
          text="購入手続き"
          :handle-click="clickBuy"
          class="ml-5 px-4 py-3"
        />
      </div>
    </div>
    <ul class="catalog">
      <li v-for="(item, index) in items" :key="item.id">
        <ItemInCart
          :id="item.id"
          :index="index"
          :img-name="item.imgName"
          :name="item.name"
          :cost="item.cost"
          :area="item.area"
          :prop-number-of-buy="item.numberOfBuy"
          :stock="item.stock"
          :review="item.review"
          @handle-change="handleChange"
        />
      </li>
    </ul>
    <div class="d-flex justify-content-center my-5">
      <PriceSum :sum="sum" class="mr-5" />
      <div class="my-auto">
        <OutlineButton
          text="購入手続き"
          :handle-click="clickBuy"
          class="ml-5 px-4 py-3"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ItemInCart from "@/components/ItemInCart";
import OutlineButton from "@/components/OutlineButton";
import PriceSum from "@/components/PriceSum";

export default {
  name: "Cart",
  components: { ItemInCart, OutlineButton, PriceSum },
  data() {
    return {
      items: [
        {
          id: 1,
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          id: 2,
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          id: 3,
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        },
        {
          id: 4,
          imgName: "ベーコン.jpg",
          name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
          numberOfBuy: 1,
          cost: 258,
          area: "東京",
          stock: 10,
          review: 3
        }
      ],
      sum: 0
    };
  },
  methods: {
    clickBuy() {
      alert("購入手続きをします。");
    },
    getSum() {
      let sum = 0;
      for (const item of this.items) {
        sum += item.cost * item.numberOfBuy;
      }

      this.sum = sum;
    },
    handleChange(arg) {
      this.items[arg.index].numberOfBuy = arg.value;
    }
  },
  watch: {
    items: {
      handler: function() {
        this.getSum();
      },
      deep: true
    }
  },
  created() {
    this.getSum();
  }
};
</script>

<style lang="scss" scoped>
.catalog {
  list-style: none;
}
</style>
