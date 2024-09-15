<template>
  <div
    class="max-h-[calc(100vh-80px)] flex flex-row bg-oldlace border-y border-solid border-gray-100"
  >
    <!-- Sidebar -->
    <div
      class="w-[525px] max-w-full bg-oldlace border-r border-solid border-gray-100 shrink-0"
    >
      <!-- Header -->
      <header class="px-6">
        <div class="flex justify-between items-center">
          <h1 class="text-3xl font-semibold">Create Your Own</h1>
          <img src="/svg1.svg" alt="Logo" class="w-8 h-8" loading="lazy" />
        </div>
        <p class="text-sm text-gray-600">$19.70 - 915 cal</p>
      </header>

      <!-- Selected Ingredients -->
      <div class="flex-1 overflow-hidden">
        <!-- Scrollable container -->
        <div
          class="flex-1 overflow-x-hidden overflow-y-auto max-h-[calc(100vh-300px)]"
        >
          <SelectedIngredients
            :selected-items="selectedIngredients"
            @deselect-item="handleDeselect"
            class="max-h-[calc(100vh-200px)]"
          />
        </div>
      </div>

      <!-- Footer -->
      <footer class="px-16 py-4 border-t border-solid border-gray-100">
        <div class="flex justify-between">
          <button class="py-4 px-16 border border-gray-100 rounded-2xl">
            Cancel
          </button>
          <button
            class="py-4 px-16 bg-darkslategray-200 text-white rounded-2xl"
          >
            I'm done
          </button>
        </div>
      </footer>
    </div>

    <!-- Options Menu -->
    <div class="flex-1 overflow-hidden">
      <!-- Scrollable container -->
      <div
        class="flex-1 overflow-x-hidden overflow-auto max-h-[calc(100vh-80px)]"
      >
        <OptionsMenu
          :ingredients-by-category="ingredientsByCategory"
          :selected-items="selectedIngredients"
          @select-item="handleSelect"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from "vue";
import SelectedIngredients from "./SelectedIngredients.vue";
import OptionsMenu from "./OptionsMenu.vue";
import { fetchItemOptions } from "@/services/apiClient"; // Import the API function
import { useRestaurantStore } from "@/stores/restaurant"; // Assuming you have this store
import { useItemStore } from "@/stores/itemStore"; // Import the Pinia store
import { ItemOption } from "@/components/types";

export default defineComponent({
  name: "OrderPage",
  components: {
    SelectedIngredients,
    OptionsMenu,
  },
  setup() {
    const itemOptions = ref<ItemOption[]>([]); // All item options fetched from the backend
    const selectedIngredients = ref<ItemOption[]>([]); // Selected ingredients
    const menuCategories = ref<string[]>([]); // Categories derived from item options
    const restaurantStore = useRestaurantStore(); // Access the restaurant store
    const itemStore = useItemStore(); // Access the restaurant store

    // Compute ingredients by category
    const ingredientsByCategory = computed(() => {
      const categories: { [key: string]: ItemOption[] } = {
        Base: [],
        Premium: [],
        Dressing: [],
        Topping: [],
      };
      itemOptions.value.forEach((ingredient) => {
        if (categories[ingredient.classification]) {
          categories[ingredient.classification].push(ingredient);
        }
      });
      return categories;
    });

    // Load item options from the backend
    const loadItemOptions = async () => {
      try {
        const restaurantId = restaurantStore.getRestaurant.id;

        if (restaurantId !== null) {
          const data = await fetchItemOptions(restaurantId);

          // Assign item options
          itemOptions.value = data.map((item: ItemOption) => ({
            id: item.id,
            name: item.name,
            image_src: item.image_src,
            classification: item.classification,
            calories: item.calories,
            cost: item.cost,
            is_in_stock: item.is_in_stock,
          }));
          itemStore.itemOptions = itemOptions.value;

          // Extract unique categories
          menuCategories.value = [
            ...new Set(data.map((item) => item.classification)),
          ];
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to load item options:", error);
      }
    };

    // Handle selection of an ingredient
    const handleSelect = (ingredient: ItemOption) => {
      if (!selectedIngredients.value.includes(ingredient)) {
        selectedIngredients.value.push(ingredient);
      }
    };

    // Handle deselection of an ingredient
    const handleDeselect = (ingredient: ItemOption) => {
      selectedIngredients.value = selectedIngredients.value.filter(
        (item) => item !== ingredient
      );
    };

    // Load item options on component mount
    onMounted(() => {
      loadItemOptions();
    });

    return {
      ingredientsByCategory,
      selectedIngredients,
      handleSelect,
      handleDeselect,
    };
  },
});
</script>
