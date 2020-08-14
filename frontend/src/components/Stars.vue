<template>
  <div>
    <FilledStar v-for="n of review" :key="n" class="mr-1" />
    <StrokeStar v-for="n of 5 - review" :key="n + review" class="mr-1" />
  </div>
</template>

<script>
import FilledStar from "@/components/FilledStar";
import StrokeStar from "@/components/StrokeStar";

export default {
  name: "Stars",
  props: ["review"],
  components: { FilledStar, StrokeStar }
};
</script>

<style scoped></style>
