<template>
  <div
    class="self-stretch flex flex-row items-start justify-start relative text-center text-sm-3 text-gray-100 font-inter"
  >
    <img
      class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
      alt=""
      :src="background"
    />
    <div
      class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-end justify-start pt-3 px-3 pb-5 z-[1]"
    >
      <div
        class="w-full overflow-hidden flex flex-col items-start justify-start py-0 pl-[7px] pr-[3px] box-border max-w-[113.2px]"
      >
        <div
          class="self-stretch relative leading-[16px] inline-block min-w-[102.2px]"
          :style="sweetgreenHotStyle"
        >
          {{ sweetgreenHot }}
        </div>
        <div
          class="flex flex-row items-start justify-start py-0 pl-[30px] pr-[34px] text-sm-2"
          :style="sauceStyle"
        >
          <div
            class="relative leading-[16px] inline-block min-w-[39px]"
            :style="sauce1Style"
          >
            {{ sauce }}
          </div>
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
  name: "ContainerComponent4",
  props: {
    background: { type: String },
    sweetgreenHot: { type: String },
    sauce: { type: String },
    container: { type: String },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf: { type: String },
    propFlex: { type: String },
  },
});
</script>
