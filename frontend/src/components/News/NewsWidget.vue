<template>
  <div
    :class="['news-widget-container']"
    :style="computedStyle"
    class="max-w-full flex flex-col relative items-center justify-start p-5"
  >
    <a
      class="news-widget-title absolute left-8 mq450:text-lgi mq450:leading-[23px]"
      >The Latest</a
    >
    <a
      class="news-widget-readmore absolute right-8 text-base uppercase inline-block"
      >Read more →</a
    >
    <section
      class="news-widget-section flex flex-row flex-wrap items-start justify-center pt-12 px-[59px] pb-[13px] box-border gap-[13px] max-w-full lg:pl-[29px] lg:pr-[29px] lg:box-border"
    >
      <NewsLink
        v-for="highlight in newsHighlights"
        :key="highlight.title"
        :title="highlight.title"
        :header="highlight.header"
        :description="highlight.description1"
        :image_src="highlight.image_src"
      />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import NewsLink from "./NewsLink.vue";
import { fetchHighlights } from "../../services/apiClient";
import { Highlight } from "../types";
import { useRestaurantStore } from "../../stores/restaurant"; // Import the store
import { useStyleStore } from "../../stores/styleStore"; // Import the style store

export default defineComponent({
  name: "NewsWidget",
  components: { NewsLink },
  setup() {
    const store = useRestaurantStore(); // Use the Pinia store
    const styleStore = useStyleStore(); // Use the style store
    const newsHighlights = ref<Highlight[]>([]);

    const loadNewsHighlights = async () => {
      try {
        const restaurantId = store.getRestaurant.id; // Get the restaurant ID from the store
        if (restaurantId !== null) {
          const data = await fetchHighlights(restaurantId);
          newsHighlights.value = data.filter(
            (highlight) => highlight.tag === "News"
          );
        } else {
          console.error("Restaurant ID is not set.");
        }
      } catch (error) {
        console.error("Failed to fetch news highlights:", error);
      }
    };

    onMounted(loadNewsHighlights);

    const defaultStyles = `
      .news-widget-container {
        background-color: var(--base-color);
        color: var(--dark-text-color);
        font-family: "Roboto", sans-serif;
        font-size: 23.6px;
      }

      .news-widget-title {
        font-size: 23.6px;
        line-height: 29px;
        text-transform: uppercase;
      }

      .news-widget-readmore {
        font-size: 16px;
        text-transform: uppercase;
      }

      .news-widget-section {
        font-size: 16px;
        color: var(--dark-text-color);
        font-family: "Roboto", sans-serif;
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.type = "text/css";
      styleElement.innerHTML = defaultStyles + styleStore.newsCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return {
      newsHighlights,
      computedStyle,
    };
  },
});
</script>
