<template>
  <div
    :class="['feature-widget-container']"
    :style="computedStyle"
    class="max-w-full flex flex-col p-8 relative"
  >
    <PictureWidget
      v-if="currentHighlight"
      :title="currentHighlight.title"
      :header="currentHighlight.header"
      :description1="currentHighlight.description1"
      :description2="currentHighlight.description2"
      :imageSrc="currentHighlight.image_src"
    />
    <button
      :class="['navigation-button']"
      :style="computedStyle"
      class="h-8 w-8 absolute top-8 right-12 rounded-full bg-razzmatazz flex items-center justify-center z-[1]"
      @click="nextHighlight"
    >
      <i class="fas fa-arrow-right text-black"></i>
    </button>
    <button
      :class="['navigation-button']"
      :style="computedStyle"
      class="h-8 w-8 absolute top-8 right-24 rounded-full bg-razzmatazz flex items-center justify-center z-[1]"
      @click="previousHighlight"
    >
      <i class="fas fa-arrow-left text-black"></i>
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from "vue";
import PictureWidget from "./PictureWidget.vue";
import { fetchHighlights } from "../../services/apiClient";
import { Highlight } from "../types";
import { useRestaurantStore } from "../../stores/restaurant"; // Import the store
import { useStyleStore } from "../../stores/styleStore"; // Import the style store

export default defineComponent({
  name: "FeatureWidget",
  components: { PictureWidget },
  setup() {
    const highlights = ref<Highlight[]>([]);
    const currentIndex = ref(0);
    const store = useRestaurantStore(); // Use the Pinia store
    const styleStore = useStyleStore(); // Use the style store

    const currentHighlight = computed(() => {
      return highlights.value[currentIndex.value];
    });

    const loadHighlights = async () => {
      try {
        const restaurantId = store.getRestaurant.id; // Get the restaurant ID from the store
        if (restaurantId !== null) {
          const data = await fetchHighlights(restaurantId);
          highlights.value = data.filter(
            (highlight: Highlight) => highlight.tag === "FeaturedMenu"
          );
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to fetch highlights:", error);
      }
    };

    const nextHighlight = () => {
      currentIndex.value = (currentIndex.value + 1) % highlights.value.length;
    };

    const previousHighlight = () => {
      currentIndex.value =
        (currentIndex.value - 1 + highlights.value.length) %
        highlights.value.length;
    };

    onMounted(loadHighlights);

    const defaultStyles = `
        .feature-widget-container {
            background-color: var( --primary-color ); /* Default bg-tasman color */
        }

        .navigation-button {
           background-color: var(--secondary-color)
          }
      `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.type = "text/css";
      styleElement.innerHTML = defaultStyles + styleStore.featureCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return {
      currentHighlight,
      nextHighlight,
      previousHighlight,
      computedStyle,
    };
  },
});
</script>
