<template>
  <div
    class="news-widget-container max-w-full flex flex-col relative items-center justify-start px-5"
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
import { defineComponent, ref, onMounted } from "vue";
import NewsLink from "./NewsLink.vue";
import { fetchHighlights } from "../../services/apiClient";
import { Highlight } from "../types";
import { useRestaurantStore } from "../../stores/restaurant"; // Import the store

export default defineComponent({
  name: "NewsWidget",
  components: { NewsLink },
  setup() {
    const store = useRestaurantStore(); // Use the Pinia store
    const newsHighlights = ref<Highlight[]>([]);

    const loadNewsHighlights = async () => {
      try {
        const restaurantId = store.getRestaurantId; // Get the restaurant ID from the store
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

    return {
      newsHighlights,
    };
  },
});
</script>

<style scoped>
.news-widget-container {
  background-color: var(
    --color-springwood
  ); /* Use a CSS variable or the actual color code */
  color: var(
    --color-huntergreen
  ); /* Use a CSS variable or the actual color code */
  font-family: "Roboto", sans-serif; /* Tailwind font-roboto-regular-155 */
  font-size: 23.6px; /* Tailwind text-[23.6px] */
}

.news-widget-title {
  font-size: 23.6px;
  line-height: 29px;
  text-transform: uppercase;
}

.news-widget-readmore {
  font-size: 16px; /* Tailwind text-base */
  text-transform: uppercase;
}

.news-widget-section {
  font-size: 16px; /* Tailwind text-base */
  color: var(--color-huntergreen);
  font-family: "Roboto", sans-serif;
}
</style>
