<template>
  <div
    class="w-[1840px] max-w-full flex flex-col items-center justify-start pt-8 px-16 pb-0 box-border gap-24 leading-[normal] tracking-[normal] article-menu"
  >
    <MenuNav
      :menuItems="menuClassifications"
      @selectClassification="filterItems"
    />
    <section
      class="w-[1440px] flex flex-row items-start justify-between py-0 px-16 box-border gap-8 max-w-[1440px] shrink-0 text-left menu-section"
    >
      <MenuItem
        v-for="item in displayedItems"
        :key="item.name"
        :header="item.name"
        :imageSrc="item.imageSrc"
        :description="item.description"
        buttonText="Order Now"
        class="flex-1"
      />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from "vue";
import axios from "axios";
import MenuNav from "./MenuNav.vue";
import MenuItem from "./MenuItem.vue";
import { MenuItem as MenuItemType } from "../types";

export default defineComponent({
  name: "MenuWidget",
  components: { MenuNav, MenuItem },
  setup() {
    const menuItems = ref<MenuItemType[]>([]);
    const menuClassifications = ref<string[]>([]);
    const filteredMenuItems = ref<MenuItemType[]>([]);
    const selectedClassification = ref<string | null>(null);

    const fetchMenuItems = async () => {
      try {
        const response = await axios.get<MenuItemType[]>(
          "http://localhost:8000/api/menu-items/"
        );
        const data = response.data;

        // Constructing MenuItem objects from the API response
        menuItems.value = data.map((item: MenuItemType) => ({
          name: item.name,
          imageSrc: item.imageSrc,
          description: item.description,
          classification: item.classification,
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
      } catch (error) {
        console.error("Failed to fetch menu items:", error);
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

    onMounted(fetchMenuItems);

    return { menuItems, menuClassifications, displayedItems, filterItems };
  },
});
</script>

<style scoped>
.article-menu {
  background-color: var(--color-oldlace); /* Replacing bg-oldlace */
  font-size: 3rem; /* text-5xl */
  font-family: "Roboto", sans-serif; /* font-roboto-regular-1575 */
  color: var(--color-huntergreen); /* Replace text-huntergreen */
}

.menu-section {
  font-size: 3rem; /* text-5xl */
  font-family: "Roboto", sans-serif; /* font-roboto-regular-1575 */
  color: var(--color-huntergreen); /* Replace text-huntergreen */
  gap: 24px;
}

@media (max-width: 1450px) {
  .menu-section {
    max-width: 100%;
  }
}
</style>
