<template>
  <div
    :class="['news-link-container']"
    :style="computedStyle"
    class="rounded-xl flex flex-row items-start justify-center py-5 px-4 box-border gap-6 min-h-[220px] max-w-full text-left text-base text-huntergreen font-roboto-regular-155 mq750:flex-wrap"
  >
    <div
      class="w-[235.3px] flex flex-col items-start justify-between min-w-[235.3px] min-h-[180px] mq750:flex-1"
    >
      <div
        class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-5 gap-[5px]"
      >
        <div class="self-stretch flex flex-col items-start justify-start">
          <div class="self-stretch relative leading-[20px] uppercase">
            {{ title }}
          </div>
        </div>
        <div
          class="self-stretch flex flex-col items-start justify-start font-georgia-regular-16"
        >
          <div class="self-stretch relative leading-[20px]">{{ header }}</div>
        </div>
      </div>
      <div
        class="self-stretch flex flex-col items-start justify-start text-base-5"
      >
        <div class="self-stretch relative leading-[20px]">
          <p class="m-0">{{ description }}</p>
          <p class="m-0">Read more →</p>
        </div>
      </div>
    </div>
    <img
      class="h-[180px] w-[180px] relative rounded-xl overflow-hidden shrink-0 object-cover max-w-[180px] min-h-[180px] mq750:w-full"
      loading="lazy"
      alt=""
      :src="image_src"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "NewsLink",
  props: {
    title: { type: String, default: "NPR HOW I BUILT THIS" },
    header: {
      type: String,
      default: "sweetgreen: Nicolas Jammet & Jonathan Neman",
    },
    description: { type: String },
    image_src: { type: String },
  },
  setup() {
    const styleStore = useStyleStore();

    const defaultStyles = `
      .news-link-container {
        background-color: var(--base-color-dark);
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
      computedStyle,
    };
  },
});
</script>
