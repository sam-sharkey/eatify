// stores/restaurant.js or stores/restaurant.ts
import { defineStore } from "pinia";
import { useLocalStorage } from "@vueuse/core";
import { Restaurant, Location } from "@eatify/shared/src/types";

export const useRestaurantStore = defineStore("restaurant", {
  state: () => ({
    restaurant: useLocalStorage<Restaurant>("restaurant", {
      id: 0,
      logo_src: "",
      name: "",
    }), // Use local storage for persistence
    location: useLocalStorage<Location | null>("location", null), // Use local storage for persistence
  }),
  actions: {
    setRestaurant(restaurant: Restaurant) {
      this.restaurant = restaurant;
    },
    setLocation(location: Location) {
      this.location = location;
    },
  },
  getters: {
    getRestaurant: (state) => state.restaurant,
    getLocation: (state) => state.location,
  },
});
