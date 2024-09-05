<template>
  <div
    class="h-[175px] w-[153.3px] flex flex-col items-start justify-center pt-1 px-2 pb-0 box-border text-center text-smi text-gray-100 font-inter"
    :style="listitemStyle"
  >
    <div
      class="self-stretch flex-1 flex flex-col items-start justify-start relative"
    >
      <img
        class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
        alt=""
        :src="background"
      />
      <div
        class="self-stretch flex-1 rounded-2xl bg-honeydew flex flex-col items-center justify-start p-3 z-[1]"
      >
        <div class="flex flex-col items-start justify-center py-2 px-[22px]">
          <div
            class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[69.21px]"
          >
            <a
              class="[text-decoration:none] relative leading-[16px] text-[inherit] inline-block min-w-[66px]"
              :style="springMixStyle"
              >{{ springMix }}</a
            >
          </div>
        </div>
        <div
          class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2 relative text-left text-xs text-white"
        >
          <img
            class="w-full flex-1 relative max-w-[113.33px] overflow-hidden max-h-full object-cover"
            loading="lazy"
            alt=""
            :src="container"
          />
          <div
            class="w-[calc(100%_+_12.3px)] !m-[0] absolute right-[-6.15px] bottom-[-6px] left-[-6.15px] flex flex-row items-start justify-between gap-0 [row-gap:20px] z-[1]"
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
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ListItem1",
  props: {
    background: { type: String },
    springMix: { type: String },
    container: { type: String },
    springMixRemoveWidth: { type: [Object, Array, String, Number, Boolean] },
    propTextDecoration: { type: String },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
  },
});
</script>
