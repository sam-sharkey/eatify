// src/router/index.ts
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomePage from "../components/HomePage/HomePage.vue";
import MenuPage from "../components/MenuPage/MenuPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/menu",
    name: "Menu",
    component: MenuPage,
  },
  /*{
    path: "/locations",
    name: "Locations",
    component: LocationsPage,
  },
  {
    path: "/reservations",
    name: "Reserve",
    component: ReservePage,
  },*/
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
