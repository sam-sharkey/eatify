<template>
  <div
    class="self-stretch h-[100px] relative text-left text-sm text-white font-poppins"
  >
    <div
      class="absolute h-full w-full top-[0%] right-[0%] bottom-[0%] left-[0%] bg-darkslategray-300"
      :style="itemSeparatorStyle"
    />
    <div
      class="absolute top-[39%] left-[72.03%] inline-block min-w-[47px] whitespace-nowrap"
    >
      $55.00
    </div>
    <div
      class="absolute top-[39%] left-[80.77%] text-pink-200 inline-block min-w-[55px]"
    >
      In Stock
    </div>
    <div class="absolute top-[39%] left-[40.82%] inline-block min-w-[76px]">
      #22314644
    </div>
    <div class="absolute top-[39%] left-[51.85%] inline-block min-w-[61px]">
      119 items
    </div>
    <div class="absolute top-[39%] left-[61.7%] inline-block min-w-[57px]">
      Chicken
    </div>
    <div class="absolute top-[19%] left-[4.41%] inline-block min-w-[30px]">
      #101
    </div>
    <div
      class="absolute top-[16px] left-[191px] flex flex-col items-start justify-start gap-[5px]"
    >
      <div class="flex flex-col items-start justify-center py-0 pl-0 pr-5">
        <div class="relative">Chicken Parmesan</div>
      </div>
      <div class="flex flex-col items-start justify-center text-darkgray">
        <div class="w-[200px] relative font-light inline-block">
          Lorem ipsum dolor sit amet, consectetur adipiscing.
        </div>
      </div>
    </div>
    <input
      class="m-0 absolute h-[11%] w-[0.87%] top-[44%] right-[97.16%] bottom-[45%] left-[1.97%] border-white border-[1px] border-solid box-border"
      type="checkbox"
    />
    <img
      class="absolute h-[22%] w-[1.73%] top-[39%] right-[6.46%] bottom-[39%] left-[91.8%] max-w-full overflow-hidden max-h-full"
      loading="lazy"
      alt=""
      src="/bitcoiniconseditfilled.svg"
    />
    <img
      class="absolute h-[22%] w-[1.73%] top-[39%] right-[3.94%] bottom-[39%] left-[94.33%] max-w-full overflow-hidden max-h-full"
      loading="lazy"
      alt=""
      src="/materialsymbolslightdelete.svg"
    />
    <img
      class="absolute h-[calc(100%_-_20px)] top-[10px] bottom-[10px] left-[calc(50%_-_578.5px)] rounded-7xs-2 max-h-full w-20 object-cover"
      loading="lazy"
      alt=""
      src="/rectangle-23839@2x.png"
    />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import type * as CSS from "csstype";

export default defineComponent({
  name: "FrameComponent1",
  props: {
    propAlignSelf: { type: String },
    propWidth: { type: [Object, Array, String, Number, Boolean] },
    propBackgroundColor: { type: String },
  },
  computed: {
    itemSeparatorStyle(): CSS.Properties {
      return {
        backgroundColor: this.propBackgroundColor,
      };
    },
  },
});
</script>
