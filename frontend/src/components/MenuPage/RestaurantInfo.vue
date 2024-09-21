<template>
  <div
    class="w-full flex flex-col-2 justify-center px-10 max-w-screen-xl text-left text-gray-100 font-inter"
  >
    <div
      :class="['location-info-container']"
      :style="computedStyle"
      class="w-full lg:w-2/3 border-gray-300 rounded-lg flex flex-col-2 px-8"
    >
      <!-- Left Section: Store Information -->
      <div class="w-full lg:w-1/2 flex flex-col py-16 pr-10">
        <div class="text-3xl tracking-tight">Order from</div>
        <div class="text-4xl text-gray-800 underline">
          {{ location.name }}
        </div>
        <div class="mt-6 p-4 rounded-md border border-gray-300 bg-green-50">
          <div class="flex items-center">
            <img class="w-4 h-4 mr-2" alt="" src="/svg-2.svg" />
            <div class="text-base">
              Store is open for dining, pick-up, and delivery.
            </div>
          </div>
        </div>
      </div>
      <!-- Right Section: Store Details Card -->
      <div class="w-full lg:w-1/2 flex flex-col items-start justify-center p-4">
        <div class="w-full p-6 border">
          <div class="text-base mb-1">{{ location.address }}</div>
          <div class="text-base mb-4">{{ location.phone_number }}</div>
          <div class="text-base">{{ location.opening_hours }}</div>
        </div>
      </div>
    </div>
    <!-- Image Section -->
    <div class="w-full lg:w-1/3 flex justify-center py-7">
      <img
        class="w-60 h-60 object-cover rounded-md"
        loading="lazy"
        :alt="location.name"
        :src="location.image_src"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { Location } from "@eatify/shared/src/types";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "RestaurantInfo",
  props: {
    location: {
      type: Object as () => Location,
      required: true,
    },
  },
  setup() {
    const styleStore = useStyleStore();

    const defaultStyles = `
      .location-info-container {
        background-color: var(--primary-color-400);
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.innerHTML = defaultStyles + styleStore.headerCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return { computedStyle };
  },
});
</script>
