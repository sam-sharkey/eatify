<template>
  <div>
    <!-- Header -->
    <header class="px-6">
      <div class="flex justify-between items-center">
        <h1 class="text-3xl font-thin">
          Customize a {{ selectedMenuItem.name }}
        </h1>
        <img src="/svg1.svg" alt="Logo" class="w-8 h-8" loading="lazy" />
      </div>
      <p class="text-sm text-gray-600">
        {{ totalPrice.toFixed(2) }} - {{ totalCalories }} cal
      </p>
    </header>

    <!-- Selected Ingredients -->
    <div class="flex-1 overflow-hidden">
      <div
        class="flex-1 overflow-x-hidden overflow-y-auto max-h-[calc(100vh-300px)]"
      >
        <div
          class="max-h-[calc(100vh-200px)] w-full flex flex-col items-start justify-start pt-0 px-8 pb-6 gap-4 max-w-[1520px] text-center text-gray-700 font-inter"
        >
          <div class="w-full grid grid-cols-3 gap-2 justify-center pb-4">
            <ProductCard
              v-for="selectedItem in selectedItems"
              :key="selectedItem.item_option.id"
              :itemName="selectedItem.item_option.name"
              :containerImage="selectedItem.item_option.image_src"
              :initialQuantity="selectedItem.quantity"
              :item="selectedItem.item_option"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Footer with Customize/Cancel button -->
    <footer class="px-16 py-4 border-t border-solid border-gray-100">
      <div class="flex justify-between">
        <button
          class="py-4 px-16 border border-gray-100 rounded-2xl"
          @click="toggleCustomize"
        >
          {{ isCustomizing ? "Cancel" : "Customize" }}
        </button>
        <button
          class="py-4 px-16 bg-darkslategray-200 text-white rounded-2xl"
          @click="$emit('done')"
        >
          I'm done
        </button>
      </div>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useItemStore } from "@/stores/itemStore";
import ProductCard from "./ProductCard.vue";

export default defineComponent({
  name: "SelectedIngredients",
  components: {
    ProductCard,
  },
  props: {
    isCustomizing: {
      type: Boolean,
      required: true,
    },
  },
  emits: ["toggle-customize", "done"],
  setup(props, { emit }) {
    const itemStore = useItemStore();

    // Computed property to get the selected menu item
    const selectedMenuItem = computed(() => itemStore.selectedMenuItem);

    // Computed property to get selected items from the store
    const selectedItems = computed(() =>
      Object.values(itemStore.selectedItems)
    );

    // Compute the total price
    const totalPrice = computed(() => {
      return selectedItems.value.reduce((total, selectedItem) => {
        return total + selectedItem.item_option.cost * selectedItem.quantity;
      }, 0);
    });

    // Compute the total calories
    const totalCalories = computed(() => {
      return selectedItems.value.reduce((total, selectedItem) => {
        return (
          total + selectedItem.item_option.calories * selectedItem.quantity
        );
      }, 0);
    });

    // Toggle the customization mode
    const toggleCustomize = () => {
      emit("toggle-customize");
    };

    return {
      selectedMenuItem,
      selectedItems,
      totalPrice,
      totalCalories,
      toggleCustomize,
    };
  },
});
</script>
