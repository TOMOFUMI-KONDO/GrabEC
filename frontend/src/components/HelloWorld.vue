<template>
  <div class="hello">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      message: "hogehoge"
    };
  },
  mounted() {
    const path = "http://localhost:5000/api/hello/Tomo";
    console.log(path);
    axios
      .get(path)
      .then(response => {
        console.log(response.data);
        this.message = response.data.msg;
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>
