<template>
  <div
    class="self-stretch flex flex-col items-start justify-center py-[0rem] px-[0.75rem] z-[2] text-left text-[1.125rem] text-gray-100 font-inter"
  >
    <div class="self-stretch flex flex-col items-start justify-center relative">
      <div class="self-stretch flex flex-col items-start justify-start">
        <div
          class="self-stretch rounded-lg bg-antiquewhite flex flex-col items-start justify-between py-[1.625rem] pl-[1.625rem] pr-[1.5rem] box-border min-h-[28.625rem] mq450:pt-[1.25rem] mq450:pb-[1.25rem] mq450:box-border"
        >
          <div
            class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1rem]"
          >
            <div class="self-stretch flex flex-col items-center justify-start">
              <img
                class="w-[16.875rem] h-[17.125rem] relative overflow-hidden shrink-0 object-cover"
                alt=""
                :src="container"
              />
            </div>
          </div>
          <div class="relative leading-[1.5rem]">
            {{ organicHibiscusBerryTea }}
          </div>
          <div
            class="flex flex-col items-start justify-start pt-[0.5rem] px-[0rem] pb-[0rem] text-[0.925rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div class="relative leading-[1.375rem]">
                <p class="m-0">{{ refreshingCrimsonCloverTea }}</p>
                <p class="m-0">{{ brightenedWithTangyHibiscus }}</p>
              </div>
            </div>
          </div>
          <div
            class="self-stretch flex flex-row items-start justify-start pt-[1rem] px-[0rem] pb-[0rem] text-center text-[0.681rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="rounded border-darkslategray-100 border-[1px] border-solid flex flex-col items-center justify-center py-[0.125rem] px-[0.437rem]"
              >
                <div
                  class="flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
                >
                  <div
                    class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[5.688rem]"
                  >
                    $3.75 — 0 cal
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="!m-[0] absolute right-[1.5rem] bottom-[1rem] flex flex-col items-start justify-start z-[1]"
      >
        <div
          class="w-[2.5rem] h-[2.5rem] rounded-81xl flex flex-col items-center justify-center"
        >
          <img class="w-[2.5rem] h-[2.5rem] relative" alt="" src="/svg-4.svg" />
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ListItem",
  props: {
    container: { type: String },
    organicHibiscusBerryTea: { type: String },
    refreshingCrimsonCloverTea: { type: String },
    brightenedWithTangyHibiscus: { type: String },
    propPadding: { type: [Object, Array, String, Number, Boolean] },
    propAlignSelf: { type: String },
    propAlignSelf1: { type: String },
  },
});
</script>
