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
import axios from "axios";
axios.defaults.baseURL = "http://localhost:5000";
axios.defaults.headers.post["Content-Type"] = "application/json;charset=utf-8";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";

export default {
  name: "Catalog",
  components: { ItemInCatalog },
  data() {
    return {
      items: [
        // {
        //   id: 1,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 2,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 3,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 4,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 5,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 6,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // },
        // {
        //   id: 7,
        //   imgName: "ベーコン.jpg",
        //   name: "みなさまのお墨付きベーコン 標準5枚入り×4パック",
        //   cost: 258,
        //   area: "東京",
        //   stock: 10,
        //   review: 3
        // }
      ]
    };
  },
  created() {
    const path = "/api/product";
    axios
      .get(path)
      .then(response => {
        console.log(response.data);
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
