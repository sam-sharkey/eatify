<template>
  <div
    class="w-full flex flex-row items-center justify-center py-[0rem] px-[2.5rem] box-border max-w-[95rem] [row-gap:20px] text-left text-[2.906rem] text-gray-100 font-inter mq1350:flex-wrap"
  >
    <div
      class="w-[26.669rem] flex flex-col items-start justify-start py-[4rem] pl-[0rem] pr-[6rem] box-border max-w-full mq450:pr-[1.25rem] mq450:box-border"
    >
      <div
        class="relative tracking-[-2px] leading-[3rem] mq450:text-[1.75rem] mq450:leading-[1.813rem] mq800:text-[2.313rem] mq800:leading-[2.375rem]"
      >
        Ordering from
      </div>
      <div
        class="flex flex-col items-start justify-start z-[1] text-[2.863rem] text-darkslategray-200"
      >
        <div class="flex flex-col items-start justify-start">
          <div
            class="relative [text-decoration:underline] tracking-[-2px] leading-[3rem] mq450:text-[1.688rem] mq450:leading-[1.813rem] mq800:text-[2.313rem] mq800:leading-[2.375rem]"
          >
            Meatpacking
          </div>
        </div>
      </div>
      <div
        class="self-stretch flex flex-col items-start justify-start pt-[1.5rem] px-[0rem] pb-[0rem] text-[0.8rem]"
      >
        <div
          class="self-stretch rounded bg-honeydew flex flex-row items-start justify-start p-[1rem]"
        >
          <div class="flex-1 flex flex-row items-center justify-start">
            <div
              class="flex flex-col items-start justify-start py-[0rem] pl-[0rem] pr-[0.5rem]"
            >
              <img class="w-[1rem] h-[1rem] relative" alt="" src="/svg-2.svg" />
            </div>
            <div class="relative leading-[1.125rem]">
              Store is open for dining, pick-up and delivery.
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="flex-[0.9143] flex flex-col items-end justify-start pt-[5.5rem] pb-[7.5rem] pl-[2.5rem] pr-[0rem] box-border min-w-[19rem] min-h-[18.625rem] max-w-full text-[0.925rem] mq1350:flex-1"
    >
      <div
        class="w-[26.669rem] flex flex-col items-start justify-start max-w-full"
      >
        <div
          class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[0.25rem] text-[0.9rem]"
        >
          <div class="self-stretch flex flex-col items-start justify-start">
            <div class="self-stretch relative leading-[1.375rem]">
              32 Gansevoort St, New York, NY 10014
            </div>
          </div>
        </div>
        <div class="self-stretch flex flex-col items-start justify-start">
          <div class="self-stretch relative leading-[1.375rem]">
            646-891-5100
          </div>
        </div>
        <div
          class="self-stretch flex flex-col items-start justify-start pt-[1rem] px-[0rem] pb-[0.25rem]"
        >
          <div class="self-stretch flex flex-col items-start justify-start">
            <div
              class="self-stretch relative leading-[1.375rem] whitespace-nowrap"
            >
              Mon - Sun 10:30am - 10:00pm
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="flex-1 flex flex-col items-end justify-center py-[1.812rem] px-[0rem] box-border min-w-[19rem] max-w-full z-[1] mq1350:flex-1"
    >
      <img
        class="w-[15rem] h-[15rem] relative overflow-hidden shrink-0 object-cover"
        loading="lazy"
        alt=""
        src="/container@2x.png"
      />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RestaurantInfo",
});
</script>
