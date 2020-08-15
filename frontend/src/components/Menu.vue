<template>
  <div class="menu">
    <b-img :src="src" :alt="displayName" class="image" @click="handleClick" />
    <p class="mt-2 text-center display-name">{{ displayName }}</p>
  </div>
</template>

<script>
export default {
  name: "Menu",
  props: ["imgName", "displayName"],
  computed: {
    src() {
      return require("@/assets/images/" + this.imgName);
    }
  },
  methods: {
    handleClick() {
      this.$router.push({ name: "MenuDetail" });
    }
  }
};
</script>

<style lang="scss" scoped>
.menu {
  .image {
    max-width: 300px;
    cursor: pointer;

    &:hover {
      opacity: 0.7;
    }
  }

  .display-name {
    font-size: 24px;
  }
}
</style>
