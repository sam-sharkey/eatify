<template>
  <button
    class="cursor-pointer border-black border-[1px] border-solid pt-2 px-[47px] pb-1.5 bg-[transparent] rounded-981xl flex flex-row items-center justify-start whitespace-nowrap hover:bg-darkslategray-200 hover:border-darkslategray-100 hover:border-[1px] hover:border-solid hover:box-border"
  >
    <div
      class="relative text-base leading-[16px] uppercase font-roboto-regular-155 text-black text-center inline-block min-w-[91px]"
    >
      {{ text }}
    </div>
  </button>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "GenericButton",
  props: {
    text: { type: String, default: "ORDER NOW" },
  },
});
</script>
