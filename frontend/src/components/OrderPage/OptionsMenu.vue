<template>
  <section
    class="w-full h-full bg-oldlace flex flex-col items-start justify-start pt-0 pb-4 text-gray-100"
  >
    <!-- Menu Categories Header -->
    <MenuCategoriesHeader
      :categories="Object.keys(ingredientsByCategory)"
      :activeCategory="activeCategory"
      class="w-full sticky top-0 z-10"
    />

    <!-- Ingredients List by Category -->
    <div class="w-full z-0 px-12 max-w-4xl mx-2">
      <!-- Iterate through each category -->
      <div
        v-for="category in Object.keys(ingredientsByCategory)"
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
            :itemName="ingredient.name"
            :containerImage="ingredient.image_src"
            :item="ingredient"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import { useItemStore } from "@/stores/itemStore"; // Import the Pinia store
import ProductCard from "./ProductCard.vue"; // Assume this component is created
import MenuCategoriesHeader from "../MenuPage/MenuCategoriesHeader.vue";

export default defineComponent({
  name: "OptionsMenu",
  components: {
    ProductCard,
    MenuCategoriesHeader,
  },
  setup() {
    // Access the Pinia store
    const itemStore = useItemStore();

    const activeCategory = ref("");

    // Handle scrolling to update active category
    const handleScroll = () => {
      const sections = document.querySelectorAll(".option-section");
      for (const section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom >= 100) {
          activeCategory.value =
            section.getAttribute("data-category") || activeCategory.value;
          break;
        }
      }
    };

    // Set up scrolling listener on mounted
    onMounted(() => {
      document.addEventListener("scroll", handleScroll);
    });

    // Computed property to get updated ingredients by category from the store
    const ingredientsByCategory = computed(() => {
      return itemStore.ingredientsByCategory;
    });

    return {
      activeCategory,
      ingredientsByCategory,
    };
  },
});
</script>

<style scoped>
/* Add any custom styles */
</style>
