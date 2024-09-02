<template>
  <section
    class="self-stretch flex flex-col items-start justify-start py-[0rem] pl-[0rem] pr-[0.75rem] box-border gap-[1rem] max-w-full text-left text-[1.775rem] text-gray-100 font-inter"
  >
    <div
      class="tracking-[1px] leading-[2.25rem] mq450:text-[1.438rem] mq450:leading-[1.813rem]"
    >
      {{ menuItemClassification }}
    </div>
    <div
      class="grid gap-[1.5rem] text-center text-[0.594rem] grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <div
        v-for="item in filteredMenuItems"
        :key="item.name"
        class="relative p-[1.625rem] rounded-lg bg-antiquewhite flex flex-col items-start gap-[1rem]"
      >
        <div
          v-if="item.tag"
          class="absolute top-2 left-2 bg-yellow m-2 py-1 px-2 rounded text-4 uppercase tracking-[1px]"
        >
          {{ item.tag }}
        </div>
        <img
          :src="item.image_src"
          :alt="item.name"
          class="w-full h-full object-cover rounded-lg"
        />
        <div class="w-full text-left text-[1.125rem]">
          <h3 class="leading-[1.5rem]">{{ item.name }}</h3>
          <p class="text-[0.931rem] leading-[1.375rem]">
            {{ item.description }}
          </p>
          <div
            class="mt-4 border border-darkslategray-100 py-[0.125rem] px-[0.5rem] rounded text-[0.669rem] uppercase tracking-[1px]"
          >
            ${{ item.price }} — {{ item.calories }} cal
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { MenuItem as MenuItemType } from "../types";
import { fetchMenuItems } from "../../services/apiClient"; // Import the API function
import { useRestaurantStore } from "../../stores/restaurant"; // Import the restaurant store

export default defineComponent({
  name: "MenuListComponent",
  props: {
    menuItemClassification: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const menuItems = ref<MenuItemType[]>([]);
    const menuClassifications = ref<string[]>([]);
    const filteredMenuItems = ref<MenuItemType[]>([]);
    const selectedClassification = ref<string | null>(null);
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
          menuClassifications.value = [
            ...new Set(data.map((item) => item.classification)),
          ];

          // Default to the first category if available
          if (menuClassifications.value.length > 0) {
            selectedClassification.value = menuClassifications.value[0];
            filteredMenuItems.value = menuItems.value.filter(
              (item) => item.classification === props.menuItemClassification
            );
          }
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to load menu items:", error);
      }
    };

    onMounted(loadMenuItems);

    return {
      filteredMenuItems,
    };
  },
});
</script>
