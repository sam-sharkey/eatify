<template>
  <div
    :class="['highlights-widget-container']"
    :style="computedStyle"
    class="max-w-full overflow-hidden flex flex-col items-start justify-start relative"
    style="height: calc(100vh - 4.5rem)"
  >
    <HighlightItem
      v-if="currentIndex >= 0 && currentIndex < highlights.length"
      :headerLine="highlights[currentIndex].header"
      :body="highlights[currentIndex].title"
      :backgroundImage="highlights[currentIndex].image_src"
    />
    <button
      :class="['navigation-button']"
      :style="computedStyle"
      class="navigation-button right-24 fas fa-chevron-left text-black"
      @click="previousHighlight"
    />
    <button
      :class="['navigation-button']"
      :style="computedStyle"
      class="right-12 fas fa-chevron-right text-black"
      @click="nextHighlight"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import HighlightItem from "./HighlightItem.vue";
import { fetchHighlights } from "../../services/apiClient";
import { Highlight } from "../types";
import { useRestaurantStore } from "../../stores/restaurant"; // Import the store
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "HighlightsWidget",
  components: { HighlightItem },
  setup() {
    const highlights = ref<Highlight[]>([]);
    const currentIndex = ref(0);
    const store = useRestaurantStore(); // Use the Pinia store
    const styleStore = useStyleStore();

    onMounted(async () => {
      try {
        const restaurantId = store.getRestaurant.id; // Get the restaurant ID from the store
        if (restaurantId !== null) {
          const data = await fetchHighlights(restaurantId);
          highlights.value = data.filter(
            (highlight: Highlight) => highlight.tag === "Highlight"
          );
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Error fetching highlights:", error);
      }
    });

    const nextHighlight = () => {
      if (currentIndex.value < highlights.value.length - 1) {
        currentIndex.value++;
      } else {
        currentIndex.value = 0;
      }
    };

    const previousHighlight = () => {
      if (currentIndex.value > 0) {
        currentIndex.value--;
      } else {
        currentIndex.value = highlights.value.length - 1;
      }
    };

    const defaultStyles = `
    .navigation-button {
      background-color: var(
        --secondary-color
      ); /* Use CSS variable for the background color */
      border-radius: 50%;
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: absolute;
      top: 36px;
      border: none;
      cursor: pointer;
      z-index: 1;
    }

    .highlights-widget-container {}
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.type = "text/css";
      styleElement.innerHTML = defaultStyles + styleStore.highlightsCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return {
      highlights,
      currentIndex,
      nextHighlight,
      previousHighlight,
      computedStyle,
    };
  },
});
</script>
