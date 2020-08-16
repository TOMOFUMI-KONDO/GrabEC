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
    <div v-if="items.length > 0">
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
            @on-remove="remove"
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
      items: [],
      itemIds: [],
      stocks: [],
      sum: 0
    };
  },
  methods: {
    async clickBuy() {
      alert("お買い上げありがとうございます！");

      const path = process.env.VUE_APP_BASE_URL + "api/remove";
      for (const item of this.items) {
        let params = new URLSearchParams();
        params.append("id", item.id);
        await this.$api.post(path, params).catch(error => console.log(error));
      }

      const length = this.items.length;
      this.items.splice(0, length);
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
    },
    async getItems() {
      let path = process.env.VUE_APP_BASE_URL + "api/cart";
      await this.$api.get(path).then(response => {
        const data = response.data;
        for (const item of data) {
          this.itemIds.push(item.id);
          this.stocks.push(item.stock);
        }
      });
      for (let i = 0; i < this.itemIds.length; i++) {
        const itemId = this.itemIds[i];
        const stock = this.stocks[i];

        path = process.env.VUE_APP_BASE_URL + "api/product/" + itemId;
        await this.$api.get(path).then(response => {
          const item = response.data;
          item["numberOfBuy"] = stock;
          this.items.push(item);
        });
      }

      this.getSum();
    },
    remove(index) {
      this.items.splice(index, 1);
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
    this.getItems();
  }
};
</script>

<style lang="scss" scoped>
.catalog {
  list-style: none;
}
</style>
