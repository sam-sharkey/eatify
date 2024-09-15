<template>
  <div
    class="max-h-[calc(100vh-80px)] flex flex-row bg-oldlace border-y border-solid border-gray-100"
  >
    <SelectedIngredients
      :selected-items="selectedIngredients"
      @deselect-item="handleDeselect"
      class="border-solid border-r border-gray-100"
    />

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
import { useRestaurantStore } from "@/stores/restaurant";
import { useItemStore } from "@/stores/itemStore";
import { ItemOption, MenuItem } from "@/components/types";
import { fetchItemOptions } from "@/services/apiClient";

export default defineComponent({
  name: "OrderPage",
  components: {
    SelectedIngredients,
    OptionsMenu,
  },
  props: {
    menuItem: {
      type: Object as () => MenuItem | null,
      required: false, // MenuItem is passed via the route, it may be null initially
    },
  },
  setup(props) {
    const itemOptions = ref<ItemOption[]>([]); // All item options fetched from the backend
    const selectedIngredients = ref<ItemOption[]>([]); // Selected ingredients
    const restaurantStore = useRestaurantStore();
    const itemStore = useItemStore();

    // Compute ingredients by category
    const ingredientsByCategory = computed(() => {
      const categories: { [key: string]: ItemOption[] } = {};
      itemOptions.value.forEach((ingredient) => {
        if (!categories[ingredient.classification]) {
          categories[ingredient.classification] = [];
        }
        categories[ingredient.classification].push(ingredient);
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
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to load item options:", error);
      }
    };

    // Handle the menuItem prop to pre-select ingredients
    const preselectIngredients = () => {
      if (props.menuItem && props.menuItem.options) {
        selectedIngredients.value = [...props.menuItem.options];
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
      preselectIngredients(); // Pre-select ingredients on mount
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
