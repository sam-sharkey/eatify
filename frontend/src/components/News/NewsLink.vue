<template>
  <div
    class="rounded-xl bg-starkwhite flex flex-row items-start justify-center py-5 px-4 box-border gap-6 min-h-[220px] max-w-full text-left text-base text-huntergreen font-roboto-regular-155 mq750:flex-wrap"
  >
    <div
      class="w-[235.3px] flex flex-col items-start justify-between min-w-[235.3px] min-h-[180px] mq750:flex-1"
    >
      <div
        class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-5 gap-[5px]"
      >
        <div class="self-stretch flex flex-col items-start justify-start">
          <div class="self-stretch relative leading-[20px] uppercase">
            {{ source }}
          </div>
        </div>
        <div
          class="self-stretch flex flex-col items-start justify-start font-georgia-regular-16"
        >
          <div class="self-stretch relative leading-[20px]">{{ caption }}</div>
        </div>
      </div>
      <div
        class="self-stretch flex flex-col items-start justify-start text-base-5"
      >
        <div class="self-stretch relative leading-[20px]">
          <p class="m-0">{{ diveIntoAJuicyPocastWithO }}</p>
          <p class="m-0">Read more →</p>
        </div>
      </div>
    </div>
    <img
      class="h-[180px] w-[180px] relative rounded-xl overflow-hidden shrink-0 object-cover max-w-[180px] min-h-[180px] mq750:w-full"
      loading="lazy"
      alt=""
      :src="figureInTheNews01V3png"
    />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "NewsLink",
  props: {
    source: { type: String, default: "NPR HOW I BUILT THIS" },
    caption: {
      type: String,
      default: "sweetgreen: Nicolas Jammet & Jonathan Neman",
    },
    diveIntoAJuicyPocastWithO: { type: String },
    figureInTheNews01V3png: { type: String },
  },
});
</script>
