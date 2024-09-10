<template>
  <div
    class="w-full relative bg-oldlace text-left text-[0.994rem] text-gray-200 font-inter"
  >
    <RestaurantInfo
      v-if="location"
      RestaurantInfo
      :key="location.name"
      :location="location"
      class="pt-10 pb-4"
    />

    <MenuCategoriesHeader
      :categories="menuCategories"
      :activeCategory="activeCategory"
      class="top-20"
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
import { MenuItem as MenuItemType, Location } from "../types";
import { fetchMenuItems, fetchLocations } from "../../services/apiClient"; // Import the API function
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
    const location = ref<Location>();

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

    const loadLocations = async () => {
      try {
        const data = await fetchLocations(restaurantStore.restaurant.id); // Fetch locations from API

        // Constructing Location objects from the API response
        location.value = data[0];
        if (location.value) {
          location.value.image_src =
            `${process.env.VUE_APP_BACKEND_URL}` + location.value.image_src;
        }
      } catch (error) {
        console.error("Failed to load locations:", error);
      }
    };

    onMounted(async () => {
      await loadMenuItems();
      await loadLocations();
      activeCategory.value = menuCategories.value[0];
      document.addEventListener("scroll", handleScroll);
    });

    return {
      menuCategories,
      activeCategory,
      handleScroll,
      location,
    };
  },
});
</script>
