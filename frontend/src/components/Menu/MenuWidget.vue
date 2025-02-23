<template>
  <div
    :class="['menu-widget-container']"
    :style="computedStyle"
    class="w-[1840px] max-w-full flex flex-col items-center justify-start py-8 px-16 box-border gap-8"
  >
    <MenuNav
      :menuItems="menuClassifications"
      @selectClassification="filterItems"
    />
    <section
      class="w-[1440px] flex flex-row items-start justify-between px-16 box-border gap-8 max-w-[1440px] shrink-0 text-left menu-section"
    >
      <MenuItem
        v-for="item in displayedItems"
        :key="item.name"
        :header="item.name"
        :imageSrc="item.image_src"
        :description="item.description"
        buttonText="Order Now"
        class="flex-1"
      />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from "vue";
import MenuNav from "./MenuNav.vue";
import MenuItem from "./MenuItem.vue";
import { MenuItem as MenuItemType } from "@eatify/shared/src/types";
import { fetchMenuItems } from "@eatify/shared/src/apiClient"; // Import the API function
import { useStyleStore } from "../../stores/styleStore"; // Import the style store
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store

export default defineComponent({
  name: "MenuWidget",
  components: { MenuNav, MenuItem },
  setup() {
    const menuItems = ref<MenuItemType[]>([]);
    const menuClassifications = ref<string[]>([]);
    const filteredMenuItems = ref<MenuItemType[]>([]);
    const selectedClassification = ref<string | null>(null);
    const styleStore = useStyleStore(); // Use the style store
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
            options: item.options,
          }));

          // Extracting unique classifications
          menuClassifications.value = [
            ...new Set(data.map((item) => item.classification)),
          ];

          // Default to the first category if available
          if (menuClassifications.value.length > 0) {
            selectedClassification.value = menuClassifications.value[0];
            filterItems(selectedClassification.value);
          }
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to load menu items:", error);
      }
    };

    const filterItems = (classification: string) => {
      selectedClassification.value = classification;
      // Limit to the first three items in the selected classification
      filteredMenuItems.value = menuItems.value
        .filter((item) => item.classification === classification)
        .slice(0, 3);
    };

    // Using a computed property to easily track what items to display
    const displayedItems = computed(() => filteredMenuItems.value);

    onMounted(loadMenuItems);

    const defaultStyles = `
      .menu-widget-container {
        background-color: var(--base-color); /* Default bg-oldlace color */
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.type = "text/css";
      styleElement.innerHTML = defaultStyles + styleStore.menuCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return {
      menuItems,
      menuClassifications,
      displayedItems,
      filterItems,
      computedStyle,
    };
  },
});
</script>

<style scoped>
.menu-section {
  font-size: 3rem; /* text-5xl */
  font-family: "Roboto", sans-serif; /* font-roboto-regular-1575 */
  color: var(--dark-text-color); /* Replace text-huntergreen */
  gap: 24px;
}

@media (max-width: 1450px) {
  .menu-section {
    max-width: 100%;
  }
}
</style>
