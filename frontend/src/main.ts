import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./services/store";
import "./assets/global.css";
import "@fortawesome/fontawesome-free/css/all.css";
import { createPinia } from "pinia";
import { useRestaurantStore } from "./stores/restaurant";
import { getRestaurantIdByName } from "./services/apiClient"; // Function to fetch restaurant ID

const pinia = createPinia();

const app = createApp(App).use(store).use(router).use(pinia);

// Async function to fetch the restaurant ID before app mounts
(async () => {
  const store = useRestaurantStore();
  const restaurantName = process.env.VUE_APP_RESTAURANT_NAME;

  try {
    const restaurantId = await getRestaurantIdByName(restaurantName);
    store.setRestaurantId(restaurantId); // Store the restaurant ID in Pinia
    console.log(`Restaurant ID: ${restaurantId}`);

    app.mount("#app"); // Mount the Vue app only after the restaurant ID is set
  } catch (error) {
    console.error("Failed to fetch restaurant ID:", error);
  }
})();
