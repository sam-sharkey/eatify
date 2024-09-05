<template>
  <div
    class="flex-1 flex flex-row items-start justify-start relative min-w-[89px] text-center text-smi text-gray-100 font-inter"
    :style="container4Style"
  >
    <img
      class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
      alt=""
      :src="background"
    />
    <div
      class="flex-1 rounded-2xl bg-honeydew flex flex-col items-end justify-start pt-5 px-1.5 pb-1.5 gap-[97px] z-[1]"
    >
      <div class="flex flex-row items-start justify-end py-0 px-8">
        <div
          class="overflow-hidden flex flex-row items-start justify-start py-0 pl-0 pr-[3px] box-border max-w-[60.63px]"
        >
          <div
            class="relative leading-[16px] inline-block min-w-[58px] whitespace-nowrap"
          >
            Wild Rice
          </div>
        </div>
      </div>
      <div
        class="self-stretch flex flex-row items-start justify-between gap-0 [row-gap:20px] text-left text-xs text-white"
      >
        <div
          class="h-8 w-8 rounded-13xl bg-oldlace border-honeydew border-[2px] border-solid box-border flex flex-col items-center justify-center py-1 px-0.5"
        >
          <img
            class="w-6 h-6 relative"
            loading="lazy"
            alt=""
            src="/button--remove-spring-mix--svg.svg"
          />
        </div>
        <div
          class="w-[93.3px] flex flex-col items-end justify-start py-0 px-0 box-border min-w-[32px]"
          :style="margin2Style"
        >
          <div
            class="w-8 rounded-13xl bg-darkslategray-200 border-honeydew border-[2px] border-solid box-border flex flex-col items-center justify-center py-[5px] px-[7px]"
          >
            <div class="flex flex-col items-start justify-start py-0 px-1">
              <div class="relative leading-[16px] inline-block min-w-[6px]">
                1
              </div>
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
  name: "ContainerComponent",
  props: {
    background: { type: String },
    propFlex: { type: String },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf: { type: String },
    propPadding: { type: [Object, Array, String, Number, Boolean] },
  },
});
</script>
