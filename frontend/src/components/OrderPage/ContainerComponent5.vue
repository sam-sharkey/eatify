<template>
  <div
    class="self-stretch flex flex-row items-start justify-start relative text-center text-sm-6 text-gray-100 font-inter"
  >
    <img
      class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
      alt=""
      src="/background-10.svg"
    />
    <div
      class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-end justify-start pt-3 px-3 pb-5 z-[1]"
    >
      <div
        class="overflow-hidden flex flex-col items-start justify-start py-0 pl-[17px] pr-3 box-border max-w-[113.2px]"
      >
        <div class="relative leading-[16px] inline-block min-w-[83px]">
          {{ noriSesame }}
        </div>
        <div
          class="flex flex-row items-start justify-start py-0 pl-1.5 pr-3.5 text-sm-1"
        >
          <a
            class="[text-decoration:none] relative leading-[16px] text-[inherit] inline-block min-w-[65px]"
            :style="seasoningStyle"
            >{{ seasoning }}</a
          >
        </div>
      </div>
      <div
        class="self-stretch flex flex-row items-start justify-end py-0 pl-3 pr-[11px]"
      >
        <img
          class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
          alt=""
          :src="container"
        />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ContainerComponent5",
  props: {
    noriSesame: { type: String },
    seasoning: { type: String },
    container: { type: String },
    propTextDecoration: { type: String },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
  },
});
</script>
