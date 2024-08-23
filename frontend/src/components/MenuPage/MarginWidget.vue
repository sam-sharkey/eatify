<template>
  <div
    class="self-stretch flex flex-col items-start justify-end pt-[1.375rem] px-[0rem] pb-[0rem] box-border min-h-[2.5rem] text-center text-[0.694rem] text-gray-100 font-inter"
  >
    <div
      class="self-stretch flex flex-row items-start justify-start pt-[1rem] px-[0rem] pb-[0rem]"
    >
      <div class="flex flex-col items-start justify-start">
        <div
          class="rounded border-darkslategray-100 border-[1px] border-solid flex flex-col items-center justify-center py-[0.125rem] px-[0.437rem]"
        >
          <div
            class="flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
          >
            <div
              class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[6.813rem]"
            >
              {{ cal }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "MarginWidget",
  props: {
    cal: { type: String },
  },
});
</script>
