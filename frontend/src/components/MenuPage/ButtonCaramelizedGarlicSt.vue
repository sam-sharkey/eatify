<template>
  <div
    class="w-[20.125rem] rounded-lg bg-antiquewhite flex flex-col items-start justify-start p-[1.625rem] box-border gap-[1rem] min-w-[19.125rem] max-w-full text-center text-[0.594rem] text-gray-100 font-inter mq800:pt-[1.25rem] mq800:pb-[1.25rem] mq800:box-border"
  >
    <div
      class="self-stretch flex flex-row items-start justify-start pt-[0rem] px-[0rem] pb-[15.625rem] relative"
    >
      <div class="w-[2.75rem] flex flex-col items-start justify-start">
        <div
          class="self-stretch rounded bg-yellow flex flex-col items-center justify-center py-[0.218rem] px-[0.437rem]"
        >
          <div
            class="self-stretch flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
          >
            <div
              class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[1.813rem]"
            >
              {{ new1 }}
            </div>
          </div>
        </div>
      </div>
      <img
        class="h-full w-full absolute !m-[0] top-[0rem] right-[0rem] bottom-[0rem] left-[0rem] max-w-full overflow-hidden max-h-full object-cover z-[1]"
        alt=""
        :src="container"
      />
    </div>
    <div
      class="self-stretch flex flex-col items-start justify-start gap-[0.5rem] text-left text-[1.125rem]"
    >
      <div class="relative leading-[1.5rem]">{{ caramelizedGarlicSteak }}</div>
      <div
        class="self-stretch flex flex-col items-start justify-start text-[0.925rem]"
      >
        <div class="relative leading-[1.375rem]">
          <p class="m-0">{{ wildRiceSpicyBroccoliTomatoes }}</p>
          <p class="m-0">{{ warmRoastedSweetPotatoes }}</p>
          <p class="m-0">{{ caramelizedGarlicSteakPesto }}</p>
          <p class="m-0">{{ vinaigrette }}</p>
        </div>
        <div
          class="self-stretch flex flex-row items-start justify-start pt-[1rem] px-[0rem] pb-[0rem] text-center text-[0.681rem]"
        >
          <div class="flex flex-col items-start justify-start">
            <div
              class="rounded border-darkslategray-100 border-[1px] border-solid flex flex-col items-center justify-center py-[0.125rem] px-[0.5rem]"
            >
              <div
                class="flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
              >
                <div
                  class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[6.75rem]"
                >
                  {{ cal }}
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
  name: "ButtonCaramelizedGarlicSt",
  props: {
    new1: { type: String },
    container: { type: String },
    caramelizedGarlicSteak: { type: String },
    wildRiceSpicyBroccoliTomatoes: { type: String },
    warmRoastedSweetPotatoes: { type: String },
    caramelizedGarlicSteakPesto: { type: String },
    vinaigrette: { type: String },
    cal: { type: String },
    propWidth: { type: [Object, Array, String, Number, Boolean] },
    propMinWidth: { type: [Object, Array, String, Number, Boolean] },
    propFlex: { type: String },
    propWidth1: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf: { type: String },
    propAlignSelf1: { type: String },
    propMinWidth1: { type: [Object, Array, String, Number, Boolean] },
    propMinWidth2: { type: [Object, Array, String, Number, Boolean] },
  },
});
</script>
