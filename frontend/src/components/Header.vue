<template>
  <header class="d-flex justify-content-around align-items-center py-4">
    <h1 class="mb-0"><a href="/" class="text-light">GrabEC</a></h1>
    <b-link href="catalog" class="text-light">商品一覧を見る</b-link>
    <div class="d-flex">
      <SearchWindow class="mr-3" />
      <CartButton />
    </div>
  </header>
</template>

<script>
import SearchWindow from "@/components/SearchWindow";
import CartButton from "@/components/CartButton";

export default {
  name: "Header",
  components: { SearchWindow, CartButton }
};
</script>

<style lang="scss" scoped>
header {
  background-color: #00b306;
  color: #fafafa;

  h1 {
    font-size: 64px;
    a {
      &:hover {
        text-decoration: none;
        color: rgb(248, 249, 250) !important;
      }
    }
  }
}
</style>
