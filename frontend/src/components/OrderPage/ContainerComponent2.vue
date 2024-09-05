<template>
  <div
    class="flex-1 flex flex-row items-start justify-start relative min-w-[89px] text-center text-sm-6 text-gray-100 font-inter mq450:flex-1"
    :style="container7Style"
  >
    <img
      class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
      alt=""
      :src="background"
    />
    <div
      class="h-[171px] flex-1 rounded-2xl bg-honeydew flex flex-col items-start justify-start p-3 box-border z-[1]"
      :style="buttonBlackenedChickenPoStyle"
    >
      <div
        class="overflow-hidden flex flex-col items-start justify-start py-0 pl-6 pr-[21px] box-border max-w-[113.33px]"
      >
        <div class="relative leading-[16px] inline-block min-w-[67px]">
          Blackened
        </div>
        <div
          class="flex flex-row items-start justify-start py-0 pl-[7px] pr-[11px] text-smi"
        >
          <div class="relative leading-[16px] inline-block min-w-[50px]">
            Chicken
          </div>
        </div>
      </div>
      <div
        class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2 relative text-left text-xs text-white"
      >
        <img
          class="w-full flex-1 relative max-w-[113.33px] overflow-hidden max-h-full object-cover"
          alt=""
          :src="container"
        />
        <div
          class="w-[calc(100%_+_12px)] !m-[0] absolute right-[-6px] bottom-[-6px] left-[-6px] flex flex-row items-start justify-between gap-0 [row-gap:20px] z-[1]"
        >
          <div
            class="h-8 w-8 rounded-13xl bg-oldlace border-honeydew border-[2px] border-solid box-border flex flex-col items-center justify-center py-1 px-0.5"
          >
            <img
              class="w-6 h-6 relative"
              alt=""
              src="/button--remove-spring-mix--svg.svg"
            />
          </div>
          <div
            class="w-[93.3px] flex flex-col items-end justify-start min-w-[32px]"
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
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ContainerComponent2",
  props: {
    background: { type: String },
    container: { type: String },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf: { type: String },
    propHeight: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf1: { type: String },
  },
});
</script>
