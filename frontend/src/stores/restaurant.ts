// stores/restaurant.js or stores/restaurant.ts
import { defineStore } from "pinia";
import { useLocalStorage } from "@vueuse/core";
import { Restaurant } from "../components/types";

export const useRestaurantStore = defineStore("restaurant", {
  state: () => ({
    restaurant: useLocalStorage<Restaurant>("restaurant", {
      id: 0,
      logo_src: "",
      name: "",
    }), // Use local storage for persistence
  }),
  actions: {
    setRestaurant(restaurant: Restaurant) {
      this.restaurant = restaurant;
    },
  },
  getters: {
    getRestaurant: (state) => state.restaurant,
  },
});
