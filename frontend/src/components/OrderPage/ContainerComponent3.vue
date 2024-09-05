<template>
  <div
    class="flex-1 flex flex-row items-start justify-start relative text-center text-sm text-gray-100 font-inter"
    :style="container8Style"
  >
    <img
      class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
      alt=""
      :src="background"
    />
    <div
      class="flex-1 rounded-2xl bg-honeydew flex flex-col items-start justify-start p-3 z-[1]"
    >
      <div
        class="w-full overflow-hidden flex flex-col items-end justify-start py-0 px-[22px] box-border max-w-[113.33px]"
      >
        <div class="flex flex-row items-start justify-end py-0 pl-[7px] pr-0.5">
          <div class="relative leading-[16px] inline-block min-w-[60px]">
            Balsamic
          </div>
        </div>
        <div
          class="self-stretch relative text-sm-2 leading-[16px] inline-block min-w-[68.4px]"
        >
          Vinaigrette
        </div>
      </div>
      <div class="self-stretch h-[115px] relative">
        <img
          class="absolute w-[calc(100%_-_23.3px)] top-[calc(50%_-_57.5px)] right-[11.6px] left-[11.7px] max-w-[113.33px] overflow-hidden h-[107px] object-cover"
          alt=""
          :src="container"
          :style="containerIconStyle"
        />
        <div
          class="absolute top-[89px] left-[-6px] rounded-13xl bg-oldlace border-honeydew border-[2px] border-solid box-border w-8 h-8 flex flex-col items-center justify-center py-1 px-0.5 z-[1]"
        >
          <img
            class="w-6 h-6 relative"
            alt=""
            src="/button--remove-spring-mix--svg.svg"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ContainerComponent3",
  props: {
    background: { type: String },
    container: { type: String },
    propFlex: { type: String },
    propAlignSelf: { type: String },
    propWidth: { type: [Object, Array, String, Number, Boolean] },
  },
});
</script>
