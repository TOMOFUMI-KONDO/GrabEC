<template>
  <p class="price-sum mb-0">
    合計：
    <span class="pr-1">{{ sum }}</span>
    円
  </p>
</template>

<script>
export default {
  name: "PriceSum",
  props: ["sum"]
};
</script>

<style lang="scss" scoped>
.price-sum {
  span {
    font-size: 48px;
  }
}
</style>
