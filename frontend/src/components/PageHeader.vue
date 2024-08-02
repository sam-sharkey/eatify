<template>
  <div
    class="w-[1440px] bg-springwood max-w-full flex flex-row items-end justify-between py-5 px-6 box-border leading-[normal] tracking-[normal] gap-5 mq1150:flex-wrap"
  >
    <div
      class="w-[450px] flex flex-col items-start justify-end pt-0 px-0 pb-[7px] box-border max-w-full"
    >
      <HeaderLeft />
    </div>
    <img
      class="h-6 w-[162px] relative"
      loading="lazy"
      alt=""
      src="/logo.svg"
    /><HeaderRight />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import HeaderLeft from "./HeaderLeft.vue";
import HeaderRight from "./HeaderRight.vue";

export default defineComponent({
  name: "PageHeader",
  components: { HeaderLeft, HeaderRight },
});
</script>
