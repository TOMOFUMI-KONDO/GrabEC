<template>
  <div class="top">
    <h2>レシピカテゴリ</h2>
    <ul class="top_recipe">
      <li>
        <a href="#">
          <img src="" alt="和食">
        </a>
      </li>
      <li>
        <a href="#">
          <img src="" alt="洋食">
        </a>
      </li>
      <li>
        <a href="#">
          <img src="" alt="中華">
        </a>
      </li>
    </ul>

  </div>
</template>

<style lang="scss">
  .top_recipe {
    list-style: none;
    background: #f7f3a8;
  }
  .top_recipe:after {
    content: '';
    display: block;
    clear: both;
  }
  .top_recipe li {
    float: left;
  }
</style>
<script>
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Top",
  // components: {
  //   HelloWorld
  // }
};
</script>