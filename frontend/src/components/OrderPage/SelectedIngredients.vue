<template>
  <!-- Header -->
  <div>
    <header class="px-6">
      <div class="flex justify-between items-center">
        <h1 class="text-3xl font-semibold">Create Your Own</h1>
        <img src="/svg1.svg" alt="Logo" class="w-8 h-8" loading="lazy" />
      </div>
      <!-- Dynamically display the total price and calories -->
      <p class="text-sm text-gray-600">
        {{ totalPrice.toFixed(2) }} - {{ totalCalories }} cal
      </p>
    </header>

    <!-- Selected Ingredients -->
    <div class="flex-1 overflow-hidden">
      <!-- Scrollable container -->
      <div
        class="flex-1 overflow-x-hidden overflow-y-auto max-h-[calc(100vh-300px)]"
      >
        <div
          class="max-h-[calc(100vh-200px)] w-full flex flex-col items-start justify-start pt-0 px-8 pb-6 gap-4 max-w-[1520px] text-center text-gray-700 font-inter"
        >
          <!-- Grid of Selected Ingredients -->
          <div class="w-full grid grid-cols-3 gap-2 justify-center pb-4">
            <ProductCard
              v-for="selectedItem in selectedItems"
              :key="selectedItem.item.id"
              :itemName="selectedItem.item.name"
              :containerImage="selectedItem.item.image_src"
              :initialQuantity="selectedItem.quantity"
              :item="selectedItem.item"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="px-16 py-4 border-t border-solid border-gray-100">
      <div class="flex justify-between">
        <button class="py-4 px-16 border border-gray-100 rounded-2xl">
          Cancel
        </button>
        <button class="py-4 px-16 bg-darkslategray-200 text-white rounded-2xl">
          I'm done
        </button>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useItemStore } from "@/stores/itemStore"; // Import the Pinia store
import ProductCard from "./ProductCard.vue";

export default defineComponent({
  name: "SelectedIngredients",
  components: {
    ProductCard,
  },
  setup() {
    const itemStore = useItemStore();

    // Computed property to get the selected items from the store
    const selectedItems = computed(() => {
      return Object.values(itemStore.selectedItems); // Get the selected items array from the store
    });

    // Computed property to calculate the total price of selected items
    const totalPrice = computed(() => {
      return selectedItems.value.reduce((total, selectedItem) => {
        return total + selectedItem.item.cost * selectedItem.quantity;
      }, 0);
    });

    // Computed property to calculate the total calories of selected items
    const totalCalories = computed(() => {
      return selectedItems.value.reduce((total, selectedItem) => {
        return total + selectedItem.item.calories * selectedItem.quantity;
      }, 0);
    });

    return {
      selectedItems,
      totalPrice,
      totalCalories,
    };
  },
});
</script>
