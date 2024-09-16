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
        <div v-if="category != 'Custom'">
          <section
            class="self-stretch flex flex-col items-start justify-start py-[0rem] pl-[0rem] pr-[0.75rem] box-border gap-[1rem] max-w-full text-left text-[1.775rem] text-gray-100 font-inter"
          >
            <div
              class="tracking-[1px] leading-[2.25rem] mq450:text-[1.438rem] mq450:leading-[1.813rem]"
            >
              {{ category }}
            </div>
            <div
              class="grid gap-[1.5rem] text-center text-[0.594rem] grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
            >
              <MenuItemComponent
                v-for="item in menuItemsByCategory[category]"
                :key="item.name"
                :item="item"
                @click="goToOrderPage(item)"
              ></MenuItemComponent>
            </div>
          </section>
        </div>
        <CustomSaladsParent v-else></CustomSaladsParent>
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import RestaurantInfo from "./RestaurantInfo.vue";
import MenuItemComponent from "./MenuItemComponent.vue";
import CustomSaladsParent from "./CustomSaladsParent.vue";
import MenuCategoriesHeader from "./MenuCategoriesHeader.vue";
import { MenuItem as MenuItemType, Location } from "../types";
import { fetchMenuItems, fetchLocations } from "../../services/apiClient"; // Import the API function
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store
import { useRouter } from "vue-router";
import { useItemStore } from "@/stores/itemStore"; // Import the Pinia store

export default defineComponent({
  name: "OrderMenuPage",
  components: {
    RestaurantInfo,
    MenuItemComponent,
    CustomSaladsParent,
    MenuCategoriesHeader,
  },
  setup() {
    const router = useRouter();
    const menuCategories = ref<string[]>([]);
    const menuItems = ref<MenuItemType[]>([]);
    const location = ref<Location>();
    const itemStore = useItemStore(); // Access the Pinia store

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

    const menuItemsByCategory = computed(() => {
      const categories: { [key: string]: MenuItemType[] } = {};

      menuItems.value.forEach((menuItem: MenuItemType) => {
        // If the classification doesn't exist in categories, create it
        if (!categories[menuItem.classification]) {
          categories[menuItem.classification] = [];
        }

        // Push the itemOption into the respective category
        categories[menuItem.classification].push(menuItem);
      });

      return categories;
    });

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
            options: item.options,
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

    const goToOrderPage = (menuItem: MenuItemType) => {
      itemStore.setSelectedMenuItem(menuItem); // Set the selected MenuItem in the store
      router.push({ name: "Order" }); // Navigate to the OrderPage
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
      menuItemsByCategory,
      goToOrderPage,
      handleScroll,
      location,
      menuItems,
    };
  },
});
</script>
