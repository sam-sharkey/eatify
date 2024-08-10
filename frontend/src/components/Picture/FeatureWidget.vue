<template>
  <div class="bg-tasman max-w-full flex flex-col p-8 relative">
    <PictureWidget
      v-if="currentHighlight"
      :title="currentHighlight.title"
      :header="currentHighlight.header"
      :description1="currentHighlight.description1"
      :description2="currentHighlight.description2"
      :imageSrc="currentHighlight.image_src"
    />
    <button
      class="h-8 w-8 absolute top-8 right-12 rounded-full bg-razzmatazz flex items-center justify-center z-[1]"
      @click="nextHighlight"
    >
      <i class="fas fa-arrow-right text-black"></i>
    </button>
    <button
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

export default defineComponent({
  name: "FeatureWidget",
  components: { PictureWidget },
  setup() {
    const highlights = ref<Highlight[]>([]);
    const currentIndex = ref(0);

    const currentHighlight = computed(() => {
      return highlights.value[currentIndex.value];
    });

    const loadHighlights = async () => {
      try {
        const data = await fetchHighlights();
        highlights.value = data.filter(
          (highlight: Highlight) => highlight.tag === "FeaturedMenu"
        );
        console.log(highlights.value);
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

    return {
      currentHighlight,
      nextHighlight,
      previousHighlight,
    };
  },
});
</script>

<style scoped>
.bg-tasman {
  background-color: #d0e8e8; /* Example color, adjust as needed */
}
</style>
