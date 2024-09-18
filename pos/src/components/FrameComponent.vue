<template>
  <div
    class="w-[1221.6px] flex flex-row items-start justify-between flex-wrap content-start py-0 px-5 box-border max-w-full gap-5 text-left text-base text-white font-poppins"
  >
    <div
      class="flex flex-row items-center justify-start gap-[35px] max-w-full mq750:flex-wrap"
    >
      <button
        class="cursor-pointer [border:none] py-[14.1px] px-[22px] bg-pink-100 flex-1 rounded-5xs-5 flex flex-row items-center justify-center box-border min-w-[99px] hover:bg-pink-300"
      >
        <div
          class="relative text-base font-medium font-poppins text-darkslategray-200 text-center"
        >
          Normal Menu
        </div>
      </button>
      <div class="relative font-medium">Special Deals</div>
      <div class="relative font-medium">New Year Special</div>
      <div class="relative font-medium">Deserts and Drinks</div>
    </div>
    <button
      class="cursor-pointer [border:none] py-[14.1px] px-[22px] bg-pink-100 rounded-5xs-5 flex flex-row items-center justify-center hover:bg-pink-300"
    >
      <div
        class="relative text-base font-medium font-poppins text-darkslategray-200 text-center"
      >
        Add Menu Item
      </div>
    </button>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "FrameComponent",
  });
</script>
