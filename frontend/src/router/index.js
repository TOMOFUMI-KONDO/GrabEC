import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import Top from "../views/Top.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  // {
  //   path: "/",
  //   name: "Home",
  //   component: Home
  // },
  {
    path: "/",
    name: "Top",
    component: Top
  },
  {
    path: "*",
    name: "NotFound",
    component: NotFound
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
