<template>
  <b-link href="#">
    <b-button variant="none" class="cart-button">
      <b-icon icon="cart3" variant="light" font-scale="2.0" class="icon" />
      <p class="text-light mb-0">カートを見る</p>
    </b-button>
  </b-link>
</template>

<script>
export default {
  name: "CartButton"
};
</script>

<style lang="scss" scoped>
.cart-button {
  &:hover {
    > * {
      color: #ff0070 !important;
    }
  }

  p {
    font-size: 14px;
  }
}
</style>
