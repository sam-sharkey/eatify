<template>
  <div
    class="w-[127px] flex flex-col items-center justify-center gap-2.5 text-center text-29xl text-black font-georgia-regular-48-title"
  >
    <a
      class="[text-decoration:none] self-stretch relative tracking-[-2.25px] leading-[48px] capitalize text-[inherit] inline-block min-w-[127px] mq450:text-10xl mq450:leading-[29px] mq825:text-19xl mq825:leading-[38px]"
      >{{ text }}</a
    >
    <img
      class="w-[18px] h-[18px] relative object-cover"
      loading="lazy"
      alt=""
      src="/full-stop@2x.png"
    />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "OnHover",
  props: {
    text: { type: String, default: "Salads" },
  },
});
</script>
