<template>
  <div
    :class="['picture-widget-container']"
    :style="computedStyle"
    class="max-w-full flex flex-col p-8 relative"
  >
    <div class="uppercase mb-2 text-huntergreen absolute top-8 left-8">
      {{ title }}
    </div>
    <section
      class="w-full flex flex-wrap pt-16 text-left picture-widget-section"
    >
      <div
        class="flex-1 flex relative flex-col min-w-[433px] max-w-full lg:flex-1"
      >
        <div class="flex flex-col">
          <div class="text-header">{{ header }}</div>
          <div class="text-body pt-4">{{ description1 }}</div>
          <div class="text-body py-4">{{ description2 }}</div>
        </div>
        <GenericButton class="w-[197px]" />
      </div>
      <div
        class="flex-1 aspect-square py-6 px-1 box-border min-w-[433px] max-w-full lg:flex-1"
      >
        <img
          class="rounded-xl max-w-full max-h-[659px] object-cover"
          loading="lazy"
          alt="Dish"
          :src="imageSrc"
        />
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import GenericButton from "../Common/GenericButton.vue";
import { useStyleStore } from "../../stores/styleStore"; // Import the style store

export default defineComponent({
  name: "PictureWidget",
  components: { GenericButton },
  props: {
    title: {
      type: String,
      required: true,
    },
    header: {
      type: String,
      required: true,
    },
    description1: {
      type: String,
      required: true,
    },
    description2: {
      type: String,
      required: true,
    },
    imageSrc: {
      type: String,
      required: true,
    },
  },
  setup() {
    const styleStore = useStyleStore(); // Use the style store

    const defaultStyles = `
      .picture-widget-container {
        background-color: var(--color-tasman); /* Default bg-tasman color */
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
      computedStyle,
    };
  },
});
</script>

<style scoped>
.picture-widget-section {
  font-size: 1rem; /* Base text size */
  color: var(--color-huntergreen);
  font-family: "Roboto", sans-serif;
}

.text-header {
  font-size: 4rem; /* Large text size for the header */
}

.text-body {
  font-size: 1.5rem; /* S */
}
</style>
