<template>
  <div
    class="relative w-full min-h-screen bg-gray text-left text-white font-poppins px-4"
  >
    <!-- Top Bar with Menu -->
    <div class="flex items-center space-x-4 p-4">
      <img
        src="/group-1000010089@2x.png"
        alt="Menu Icon"
        class="w-8 h-8 object-contain"
        loading="lazy"
      />
      <a href="#" class="text-xl font-medium text-white [text-decoration:none]">
        Menu
      </a>
    </div>

    <!-- User Profile Section -->
    <div class="absolute top-4 right-8 flex flex-col items-center space-y-2">
      <div
        class="relative flex items-center justify-center bg-pink-100 rounded-full w-10 h-10"
      >
        <span class="text-darkslategray-200 text-sm">01</span>
      </div>
      <img
        src="/ellipse-1@2x.png"
        alt="User Profile"
        class="w-10 h-10 rounded-full object-cover"
        loading="lazy"
      />
    </div>

    <!-- Sidebar -->
    <MenuCategoryNav
      :menuItems="groupedMenuItems"
      @select-category="handleCategorySelect"
    />

    <!-- Product Table Section -->
    <section class="px-4 max-w-7xl mx-auto">
      <ProductTable :categoryItems="filteredCategoryItems" />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from "vue";
import MenuCategoryNav from "../components/MenuCategoryNav.vue";
import ProductTable from "../components/ProductTable.vue";
import { fetchMenuItems } from "../services/apiClient"; // API client to fetch menu items

export default defineComponent({
  name: "Menu",
  components: { MenuCategoryNav, ProductTable },
  setup() {
    const menuItems = ref([]);

    // Grouped menu items for display in the categories navigation
    const groupedMenuItems = ref([]);

    // Currently selected category items
    const selectedCategory = ref("All");
    const filteredCategoryItems = computed(() => {
      if (selectedCategory.value === "All") {
        return menuItems.value;
      }
      return menuItems.value.filter(
        (item) => item.classification === selectedCategory.value
      );
    });

    const loadMenuItems = async () => {
      try {
        const data = await fetchMenuItems(1);

        // Group menu items by category
        const categoryMap = data.reduce((acc: any, item: any) => {
          const category = item.classification || "Uncategorized";
          if (!acc[category]) {
            acc[category] = [];
          }
          acc[category].push(item);
          return acc;
        }, {});

        menuItems.value = data;

        // Format grouped data for `MenuCategoryNav`
        groupedMenuItems.value = Object.keys(categoryMap).map((category) => ({
          name: category,
          items: `${categoryMap[category].length} items`,
          groupIcon: categoryMap[category][0].image_src, // Update icon path for each category
        }));
      } catch (error) {
        console.error("Error loading menu items:", error);
      }
    };

    const handleCategorySelect = (category: string) => {
      selectedCategory.value = category;
    };

    onMounted(() => {
      loadMenuItems();
    });

    return {
      groupedMenuItems,
      filteredCategoryItems,
      handleCategorySelect,
    };
  },
});
</script>

<style scoped>
/* Add any specific styles if necessary */
</style>
