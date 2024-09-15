<template>
  <div
    class="w-full flex flex-col items-start justify-start pt-0 px-8 pb-6 gap-4 max-w-[1520px] text-center text-gray-700 font-inter"
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

    return {
      selectedItems,
    };
  },
});
</script>
