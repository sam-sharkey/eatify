<template>
  <div
    class="w-full relative bg-oldlace text-left text-[0.994rem] text-gray-200 font-inter"
  >
    <RestaurantInfo />

    <MenuCategoriesHeader
      :categories="menuCategories"
      :activeCategory="activeCategory"
    />

    <main
      class="pt-4 pb-8 px-4 gap-[4rem] mq450:gap-[1rem]"
      @scroll="handleScroll"
    >
      <div
        v-for="category in menuCategories"
        :key="category"
        :data-category="category"
        class="menu-section p-6"
      >
        <component
          :is="
            category === 'Custom' ? 'CustomSaladsParent' : 'MenuListComponent'
          "
          :menuItemClassification="category"
        />
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import RestaurantInfo from "./RestaurantInfo.vue";
import MenuListComponent from "./MenuListComponent.vue";
import CustomSaladsParent from "./CustomSaladsParent.vue";
import MenuCategoriesHeader from "./MenuCategoriesHeader.vue";
import { MenuItem as MenuItemType } from "../types";
import { fetchMenuItems } from "../../services/apiClient"; // Import the API function
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store

export default defineComponent({
  name: "OrderMenuPage",
  components: {
    RestaurantInfo,
    MenuListComponent,
    CustomSaladsParent,
    MenuCategoriesHeader,
  },
  setup() {
    const menuCategories = ref<string[]>([]);
    const menuItems = ref<MenuItemType[]>([]);

    const activeCategory = ref("");

    const handleScroll = () => {
      const sections = document.querySelectorAll(".menu-section");

      for (const section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom >= 100) {
          activeCategory.value =
            section.getAttribute("data-category") || activeCategory.value;
          break;
        }
      }
    };

    const customCreationEnabled = true;

    const restaurantStore = useRestaurantStore(); // Use the restaurant store

    const loadMenuItems = async () => {
      try {
        const restaurantId = restaurantStore.getRestaurantId; // Get the restaurant ID from the store

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

    onMounted(async () => {
      await loadMenuItems();
      activeCategory.value = menuCategories.value[0];
      document.addEventListener("scroll", handleScroll);
    });

    return {
      menuCategories,
      activeCategory,
      handleScroll,
    };
  },
});
</script>
