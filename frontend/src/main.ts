import { createApp } from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./services/store";
import "./assets/global.css";
import "@fortawesome/fontawesome-free/css/all.css";
import { createPinia } from "pinia";
import { useRestaurantStore } from "./stores/restaurant";
import { getRestaurantByName } from "./services/apiClient"; // Function to fetch restaurant ID

const pinia = createPinia();

const app = createApp(App).use(store).use(router).use(pinia);

// Async function to fetch the restaurant ID before app mounts
(async () => {
  const store = useRestaurantStore();
  const restaurantName = process.env.VUE_APP_RESTAURANT_NAME;

  try {
    const restaurant = await getRestaurantByName(restaurantName);
    store.setRestaurant(restaurant); // Store the restaurant ID in Pinia
    console.log(`Restaurant : ${restaurant.name}`);

    app.mount("#app"); // Mount the Vue app only after the restaurant ID is set
  } catch (error) {
    console.error("Failed to fetch restaurant ID:", error);
  }
})();
