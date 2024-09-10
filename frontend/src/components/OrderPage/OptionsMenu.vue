<template>
  <section
    class="bg-oldlace flex flex-col items-start justify-start pt-0 px-8 pb-4 text-gray-100"
  >
    <div class="w-full max-w-4xl mx-auto">
      <!-- Section Header -->
      <h2 class="text-xl font-semibold mb-4">Menu</h2>
      <div v-if="ingredientsByCategory" class="space-y-8">
        <!-- Bases Section -->
        <div v-if="ingredientsByCategory['Base']">
          <h3 class="text-lg font-medium mb-4">Bases</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <ProductCard
              v-for="ingredient in ingredientsByCategory['Base']"
              :key="ingredient.id"
              :containerImage="ingredient.image_src"
              :itemName="ingredient.name"
              :in-stock="ingredient.is_in_stock"
            />
          </div>
        </div>

        <!-- Topping Section -->
        <div v-if="ingredientsByCategory['Topping']">
          <h3 class="text-lg font-medium mb-4">Topping</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <ProductCard
              v-for="ingredient in ingredientsByCategory['Topping']"
              :key="ingredient.id"
              :containerImage="ingredient.image_src"
              :itemName="ingredient.name"
              :in-stock="ingredient.is_in_stock"
            />
          </div>
        </div>

        <!-- Premiums Section -->
        <div v-if="ingredientsByCategory['Premium']">
          <h3 class="text-lg font-medium mb-4">Premiums</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <ProductCard
              v-for="ingredient in ingredientsByCategory['Premium']"
              :key="ingredient.id"
              :containerImage="ingredient.image_src"
              :itemName="ingredient.name"
              :in-stock="ingredient.is_in_stock"
            />
          </div>
        </div>

        <!-- Dressings Section -->
        <div v-if="ingredientsByCategory['Dressing']">
          <h3 class="text-lg font-medium mb-4">Dressings</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <ProductCard
              v-for="ingredient in ingredientsByCategory['Dressing']"
              :key="ingredient.id"
              :containerImage="ingredient.image_src"
              :itemName="ingredient.name"
              :in-stock="ingredient.is_in_stock"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import { ItemOption } from "../types";
import { fetchItemOptions } from "../../services/apiClient"; // Import the API function
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store
import ProductCard from "./ProductCard.vue"; // Assume this component is created

export default defineComponent({
  name: "OptionsMenu",
  components: {
    ProductCard,
  },
  setup() {
    const restaurantStore = useRestaurantStore(); // Use the restaurant store
    const itemOptions = ref<ItemOption[]>([]);
    const menuCategories = ref<string[]>([]);

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

    const loadItemOptions = async () => {
      try {
        const restaurantId = restaurantStore.getRestaurant.id; // Get the restaurant ID from the store

        if (restaurantId !== null) {
          const data = await fetchItemOptions(restaurantId);

          // Constructing MenuItem objects from the API response
          itemOptions.value = data.map((item: ItemOption) => ({
            name: item.name,
            image_src: item.image_src,
            classification: item.classification,
            calories: item.calories,
            cost: item.cost,
            is_in_stock: item.is_in_stock,
          }));

          // Extracting unique classifications
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

    onMounted(loadItemOptions);

    return { ingredientsByCategory };
  },
});
</script>
