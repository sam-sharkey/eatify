<template>
  <div
    class="max-h-[calc(100vh-80px)] flex flex-row bg-oldlace border-y border-solid border-gray-100"
  >
    <SelectedIngredients
      class="border-solid border-r border-gray-100"
      :is-customizing="isCustomizing"
      @toggle-customize="toggleCustomize"
    />

    <!-- Show MenuItem Image or Options Menu -->
    <div class="flex-1 overflow-hidden">
      <div
        v-if="!isCustomizing"
        class="flex justify-center items-center h-full bg-antiquewhite"
      >
        <!-- Display the selected MenuItem's image when not customizing -->
        <img
          :src="selectedMenuItem.image_src"
          alt="MenuItem Image"
          class="w-1/2 justify-center object-contain"
        />
      </div>
      <div
        v-else
        class="flex-1 overflow-x-hidden overflow-auto max-h-[calc(100vh-80px)]"
      >
        <OptionsMenu />
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
import { ItemOption } from "@/components/types";
import { fetchItemOptions } from "@/services/apiClient";

export default defineComponent({
  name: "OrderPage",
  components: {
    SelectedIngredients,
    OptionsMenu,
  },
  setup() {
    const itemOptions = ref<ItemOption[]>([]);
    const restaurantStore = useRestaurantStore();
    const itemStore = useItemStore();
    const isCustomizing = ref(false); // Track if the user is customizing

    // Get the selected menu item from the store
    const selectedMenuItem = computed(() => itemStore.selectedMenuItem);

    // Toggle between customizing and displaying the MenuItem image
    const toggleCustomize = () => {
      isCustomizing.value = !isCustomizing.value;
    };

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

    // Pre-select ingredients on mount
    const preselectIngredients = () => {
      if (itemStore.selectedMenuItem && itemStore.selectedMenuItem.options) {
        itemStore.selectedMenuItem.options.forEach((option: ItemOption) => {
          itemStore.addItem(option);
        });
      }
    };

    // Load item options on component mount
    onMounted(() => {
      loadItemOptions();
      preselectIngredients(); // Pre-select ingredients on mount
    });

    return {
      isCustomizing,
      selectedMenuItem,
      toggleCustomize,
    };
  },
});
</script>
