<template>
  <b-button @click.stop="handleClick" class="button">
    {{ text }}
  </b-button>
</template>

<script>
export default {
  name: "OutlineButton",
  props: ["text", "handleClick"]
};
</script>

<style lang="scss" scoped>
.button {
  background: none;
  border-color: #ff0070;
  color: #ff0070;

  &:hover {
    background: #ff0070;
    border-color: #ff0070;
    color: #fafafa;
  }

  &:active {
    background-color: #ff0070 !important;
    border-color: #ff0070 !important;
    color: #fafafa !important;
  }

  &:focus {
    background-color: #ff0070 !important;
    border-color: #ff0070 !important;
    color: #fafafa !important;
    box-shadow: none !important;
  }
}
</style>
