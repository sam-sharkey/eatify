import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
// Import Vuetify and its styles
import { createVuetify } from "vuetify";
import "vuetify/styles"; // Global Vuetify styles

// Import Vuetify components and directives (optional, for tree-shaking)
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

import Menu from "./pages/Menu.vue";
import Orders from "./pages/Orders.vue";
import "./global.css";

interface Route {
  path: string;
  name: string;
  component: any;
}

const routes: Route[] = [
  {
    path: "/Menu",
    name: "Menu",
    component: Menu,
  },
  {
    path: "/Orders",
    name: "Orders",
    component: Orders,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Create Vuetify instance
const vuetify = createVuetify({
  components,
  directives,
});

router.beforeEach((toRoute, _, next) => {
  const metaTitle = toRoute?.meta?.title as string;
  const metaDesc = toRoute?.meta?.description as string;

  window.document.title = metaTitle || "Application";
  if (metaDesc) {
    addMetaTag(metaDesc);
  }
  next();
});

const addMetaTag = (value: string) => {
  const element = document.querySelector(`meta[name='description']`);
  if (element) {
    element.setAttribute("content", value);
  }
};

createApp(App).use(router).use(vuetify).mount("#app");

export default router;
