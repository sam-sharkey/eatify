<template>
  <div
    class="bg-springwood flex flex-row items-start justify-start py-0 px-6 box-border gap-6 max-w-full text-left text-base text-huntergreen font-roboto-regular-155 mq750:flex-wrap"
  >
    <div class="flex flex-col items-start justify-start pt-[7px] px-0 pb-0">
      <a
        class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[72px]"
        >Outpost</a
      >
    </div>
    <div class="flex flex-col items-start justify-start pt-[7px] px-0 pb-0">
      <a
        class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[100px]"
        >Our Mission</a
      >
    </div>
    <div
      class="flex flex-col items-start justify-start pt-[7px] px-0 pb-0 text-base-9"
    >
      <a
        class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[75px]"
        >Catering</a
      >
    </div>
    <GenericButton />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "./GenericButton.vue";

export default defineComponent({
  name: "HeaderRight",
  components: { GenericButton },
});
</script>
