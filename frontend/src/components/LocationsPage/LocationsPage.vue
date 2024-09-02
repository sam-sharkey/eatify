<template>
  <section
    :class="['locations-container']"
    :style="computedStyle"
    class="self-stretch flex flex-col items-start justify-start pr-[0.75rem] box-border gap-[1rem] max-w-full text-left text-[1.775rem] text-gray-100 font-inter"
  >
    <div class="p-4">
      {{ restaurantName }}
    </div>
    <div class="w-full grid gap-6 text-center py-6">
      <RestaurantInfo
        v-for="location in locations"
        :key="location.name"
        :location="location"
      />
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import { Location } from "../types";
import { fetchLocations } from "../../services/apiClient";
import RestaurantInfo from "../MenuPage/RestaurantInfo.vue";
import { useRestaurantStore } from "../../stores/restaurant";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "LocationListComponent",
  components: {
    RestaurantInfo,
  },
  setup() {
    const locations = ref<Location[]>([]);
    const restaurantStore = useRestaurantStore();
    const restaurantName = ref<string>(restaurantStore.restaurant.name);
    const styleStore = useStyleStore();

    const defaultStyles = `
      .locations-container {
        background-color: var(--primary-color-200);
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.innerHTML = defaultStyles + styleStore.headerCss;
      document.head.appendChild(styleElement);
      return "";
    });

    const loadLocations = async () => {
      try {
        const data = await fetchLocations(restaurantStore.restaurant.id); // Fetch locations from API

        // Constructing Location objects from the API response
        locations.value = data.map((item: Location) => ({
          name: item.name,
          address: item.address,
          phone_number: item.phone_number,
          opening_hours: item.opening_hours,
          image_src: `${process.env.VUE_APP_BACKEND_URL}` + item.image_src,
        }));
      } catch (error) {
        console.error("Failed to load locations:", error);
      }
    };

    onMounted(loadLocations);

    return {
      locations,
      restaurantName,
      computedStyle,
    };
  },
});
</script>
