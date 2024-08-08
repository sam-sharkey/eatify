<template>
  <div
    class="max-w-full overflow-hidden flex flex-col items-start justify-start leading-[normal] tracking-[normal] relative"
  >
    <HighlightItem
      v-if="currentIndex >= 0 && currentIndex < highlights.length"
      :headerLine1="highlights[currentIndex].headerLine1"
      :headerLine2="highlights[currentIndex].headerLine2"
      :body="highlights[currentIndex].body"
      :backgroundImage="highlights[currentIndex].backgroundImage"
    />
    <button
      class="navigation-button right-24 fas fa-chevron-left text-black"
      @click="previousHighlight"
    />
    <button
      class="navigation-button right-12 fas fa-chevron-right text-black"
      @click="nextHighlight"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import HighlightItem from "./HighlightItem.vue";

interface Highlight {
  headerLine1: string;
  headerLine2: string;
  body: string;
  backgroundImage: string;
}

export default defineComponent({
  name: "HighlightsWidget",
  components: { HighlightItem },
  setup() {
    const highlights = ref<Highlight[]>([
      {
        headerLine1: "Introducing Caramelized",
        headerLine2: "Garlic Steak at Sweetgreen",
        body: "Grass-fed, pasture-raised",
        backgroundImage: "/public/picturecontainer@3x.png",
      },
      {
        headerLine1: "Fresh and Flavorful",
        headerLine2: "Summer Salads Available Now",
        body: "Locally sourced ingredients",
        backgroundImage: "/public/summer-salad.png",
      },
      {
        headerLine1: "New Seasonal Bowl",
        headerLine2: "Try the Autumn Harvest Bowl",
        body: "A cozy, nutritious blend",
        backgroundImage: "/public/autumn-bowl.png",
      },
    ]);

    const currentIndex = ref(0);

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

    return {
      highlights,
      currentIndex,
      nextHighlight,
      previousHighlight,
    };
  },
});
</script>

<style scoped>
.navigation-button {
  background-color: var(
    --color-razzmatazz
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

.navigation-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
