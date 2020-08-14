<template>
  <b-button @click.stop="handleClick">
    {{ text }}
  </b-button>
</template>

<script>
export default {
  name: "OutlineButton",
  props: ["text", "handleClick"]
};
</script>
