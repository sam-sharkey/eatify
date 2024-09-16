// src/stores/itemStore.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { ItemOption, MenuItem } from "@/components/types"; // Assuming you have this type defined

export const useItemStore = defineStore("itemStore", () => {
  const itemOptions = ref<ItemOption[]>([]); // All available ingredients
  const selectedItems = ref<{
    [id: string]: { item: ItemOption; quantity: number };
  }>({}); // Selected ingredients with quantities
  const selectedMenuItem = ref<MenuItem | null>();

  // Check if an item is selected and get its quantity
  const clearAllItems = () => {
    selectedItems.value = {};
  };

  const setSelectedMenuItem = (menuItem: MenuItem) => {
    selectedMenuItem.value = menuItem; // Set the selected MenuItem
  };
  const clearSelectedMenuItem = () => {
    selectedMenuItem.value = null; // Clear the selected MenuItem if needed
  };

  // Computed property to categorize items
  const ingredientsByCategory = computed(() => {
    const categories: { [key: string]: ItemOption[] } = {};

    itemOptions.value.forEach((itemOption: ItemOption) => {
      // If the classification doesn't exist in categories, create it
      if (!categories[itemOption.classification]) {
        categories[itemOption.classification] = [];
      }

      // Push the itemOption into the respective category
      categories[itemOption.classification].push(itemOption);
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
    selectedMenuItem,
    clearAllItems,
    isItemSelected,
    addItem,
    removeItem,
    getItemQuantity,
    clearSelectedMenuItem,
    setSelectedMenuItem,
  };
});
