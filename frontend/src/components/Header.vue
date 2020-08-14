<template>
  <header class="d-flex justify-content-around align-items-center py-4">
    <h1 class="mb-0">GrabEC</h1>
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

  .nav {
    a {
      font-weight: bold;

      &.router-link-exact-active {
        color: #ff0070;
      }
    }
  }
}
</style>
