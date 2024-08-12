// stores/restaurant.js or stores/restaurant.ts
import { defineStore } from "pinia";
import { useLocalStorage } from "@vueuse/core";

export const useRestaurantStore = defineStore("restaurant", {
  state: () => ({
    restaurantId: useLocalStorage<number | null>("restaurantId", null), // Use local storage for persistence
  }),
  actions: {
    setRestaurantId(id: number) {
      this.restaurantId = id;
    },
  },
  getters: {
    getRestaurantId: (state) => state.restaurantId,
  },
});
