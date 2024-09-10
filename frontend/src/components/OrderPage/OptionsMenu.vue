<template>
  <section
    class="w-full h-full bg-oldlace flex flex-col items-start justify-start pt-0 pb-4 text-gray-100"
  >
    <MenuCategoriesHeader
      :categories="menuCategories"
      :activeCategory="activeCategory"
      class="w-full sticky top-0 z-10"
    />
    <div class="w-full z-0 px-12 max-w-4xl mx-2">
      <div v-if="ingredientsByCategory" class="space-y-8">
        <!-- Bases Section -->
        <div
          v-for="category in menuCategories"
          :key="category"
          class="option-section"
          :data-category="category"
        >
          <h3 class="text-lg font-medium mb-4">{{ category }}</h3>
          <div
            class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4"
          >
            <ProductCard
              v-for="ingredient in ingredientsByCategory[category]"
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
import MenuCategoriesHeader from "../MenuPage/MenuCategoriesHeader.vue";

export default defineComponent({
  name: "OptionsMenu",
  components: {
    ProductCard,
    MenuCategoriesHeader,
  },
  setup() {
    const restaurantStore = useRestaurantStore(); // Use the restaurant store
    const itemOptions = ref<ItemOption[]>([]);
    const menuCategories = ref<string[]>([]);

    const activeCategory = ref("");

    const handleScroll = () => {
      const sections = document.querySelectorAll(".option-section");
      console.log(sections);

      for (const section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom >= 100) {
          activeCategory.value =
            section.getAttribute("data-category") || activeCategory.value;
          break;
        }
      }
    };

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

    onMounted(async () => {
      loadItemOptions();
      document.addEventListener("scroll", handleScroll);
    });

    return { ingredientsByCategory, menuCategories, activeCategory };
  },
});
</script>
