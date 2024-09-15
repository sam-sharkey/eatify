// src/stores/itemStore.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { ItemOption } from "@/components/types"; // Assuming you have this type defined

export const useItemStore = defineStore("itemStore", () => {
  const itemOptions = ref<ItemOption[]>([]); // All available ingredients
  const selectedItems = ref<{
    [id: string]: { item: ItemOption; quantity: number };
  }>({}); // Selected ingredients with quantities

  // Computed property to categorize items
  const ingredientsByCategory = computed(() => {
    const categories: { [key: string]: ItemOption[] } = {};

    itemOptions.value.forEach((ingredient) => {
      // If the classification doesn't exist in categories, create it
      if (!categories[ingredient.classification]) {
        categories[ingredient.classification] = [];
      }

      // Push the ingredient into the respective category
      categories[ingredient.classification].push(ingredient);
    });

    return categories;
  });

  // Add an item or increment its quantity
  const addItem = (item: ItemOption) => {
    if (selectedItems.value[item.id]) {
      selectedItems.value[item.id].quantity += 1;
    } else {
      selectedItems.value[item.id] = { item, quantity: 1 };
    }
  };

  // Remove an item or decrement its quantity
  const removeItem = (itemId: string) => {
    if (selectedItems.value[itemId]) {
      if (selectedItems.value[itemId].quantity > 1) {
        selectedItems.value[itemId].quantity -= 1;
      } else {
        delete selectedItems.value[itemId]; // Remove the item if quantity reaches 0
      }
    }
  };

  // Check if an item is selected and get its quantity
  const getItemQuantity = (itemId: string) => {
    return selectedItems.value[itemId]?.quantity || 0;
  };

  // Check if an item is selected and get its quantity
  const isItemSelected = (itemId: string) => {
    return selectedItems.value[itemId]?.quantity || 0 == 0;
  };

  return {
    itemOptions,
    selectedItems,
    ingredientsByCategory,
    isItemSelected,
    addItem,
    removeItem,
    getItemQuantity,
  };
});
