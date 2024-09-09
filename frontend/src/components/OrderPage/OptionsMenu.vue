<template>
  <section
    class="bg-oldlace flex flex-col items-start justify-start pt-0 px-8 pb-4 text-gray-100"
  >
    <div class="w-full max-w-4xl mx-auto">
      <!-- Section Header -->
      <h2 class="text-xl font-semibold mb-4">Menu</h2>
      <div v-if="loading" class="text-center">Loading...</div>

      <div v-if="!loading" class="space-y-8">
        <!-- Bases Section -->
        <div v-if="ingredientsByCategory['Base']">
          <h3 class="text-lg font-medium mb-4">Bases</h3>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            <ProductCard
              v-for="ingredient in ingredientsByCategory['Base']"
              :key="ingredient.id"
              :image="ingredient.image_src"
              :name="ingredient.name"
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
              :image="ingredient.image_src"
              :name="ingredient.name"
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
              :image="ingredient.image_src"
              :name="ingredient.name"
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
              :image="ingredient.image_src"
              :name="ingredient.name"
              :in-stock="ingredient.is_in_stock"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent, ref, onMounted } from "vue";
import { ItemOption } from "../types";
import { fetchMenuItems, fetchItemOptions } from "../../services/apiClient"; // Import the API function
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store
import ProductCard from "./ProductCard.vue"; // Assume this component is created

export default defineComponent({
  name: "OptionsMenu",
  components: {
    ProductCard
  },
  data() {
    return {
      ingredients: [],
      loading: true,
    };
  },
  computed: {
    ingredientsByCategory() {
      const categories = {
        Base: [],
        Premium: [],
        Dressing: [],
      };
      this.ingredients.forEach((ingredient) => {
        if (categories[ingredient.classification]) {
          categories[ingredient.classification].push(ingredient);
        }
      });
      return categories;
    },
  },
  setup() {
    const restaurantStore = useRestaurantStore(); // Use the restaurant store

    const loadItemOptions = async () => {
      try {
        const restaurantId = restaurantStore.getRestaurant.id; // Get the restaurant ID from the store

        if (restaurantId !== null) {
          const data = await fetchMenuItems(restaurantId);

          // Constructing MenuItem objects from the API response
          menuItems.value = data.map((item: MenuItemType) => ({
            name: item.name,
            image_src: item.image_src,
            description: item.description,
            classification: item.classification,
            tag: item.tag,
            calories: item.calories,
            price: item.price,
          }));

          // Extracting unique classifications
          menuCategories.value = [
            ...new Set(data.map((item) => item.classification)),
          ];
          if (customCreationEnabled) {
            menuCategories.value.push("Custom");
          }
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to load menu items:", error);
      }
    };
  },
};
</script>
