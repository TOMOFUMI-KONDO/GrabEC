<template>
  <div class="search-window position-relative">
    <b-input placeholder="キーワードから商品を探す" class="search-input" />
    <b-icon icon="search" class="search-icon" />
  </div>
</template>

<script>
export default {
  name: "SearchWindow"
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
