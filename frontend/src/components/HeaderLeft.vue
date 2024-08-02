<template>
  <div
    class="bg-springwood flex flex-row items-start justify-start py-0 px-6 box-border gap-6 max-w-full text-left text-base text-huntergreen font-roboto-regular-155 mq450:flex-wrap"
  >
    <a
      class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[85px]"
      >Locations</a
    >
    <a
      class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[81px]"
      >Our Menu</a
    >
    <a
      class="[text-decoration:none] relative text-base-9 leading-[16px] uppercase text-[inherit] inline-block min-w-[97px]"
      >The Market</a
    >
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "HeaderLeft",
});
</script>
