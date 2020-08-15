<template>
  <p class="tag px-2 py-1">{{ name }}</p>
</template>

<script>
export default {
  name: "Tag",
  props: ["name"]
};
</script>

<style lang="scss" scoped>
.tag {
  border-radius: 0.25rem;
  background-color: #ff0070;
  color: #fafafa;
  font-size: 14px;
}
</style>
