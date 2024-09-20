<template>
  <div
    class="flex flex-col items-start justify-start p-4 relative gap-4 text-center text-white font-poppins max-w-full"
  >
    <!-- Background -->
    <div class="absolute inset-0 rounded bg-darkslategray-300"></div>

    <!-- Content Wrapper -->
    <div
      class="w-full flex flex-col gap-4 text-darkslategray-200 text-6xl relative z-10"
    >
      <!-- Separator Row -->
      <div class="flex w-full flex-row gap-3 mq450:flex-wrap relative z-10">
        <div class="flex items-center py-3 px-4 bg-green-300 rounded">
          <div class="font-medium mq450:text-xl">{{ separator }}</div>
        </div>
        <div class="flex-1 flex flex-col gap-4 text-left">
          <div class="flex justify-between gap-4">
            <div class="flex flex-col gap-1">
              <div class="font-medium">Watson Joyce</div>
              <a href="#" class="text-xs font-light">Order # 990</a>
            </div>
            <div
              class="flex flex-col items-end gap-1 text-xs text-darkslategray-200"
            >
              <div
                class="flex items-center gap-1 bg-honeydew py-1 px-2 rounded"
              >
                <img
                  class="w-3 h-3"
                  loading="lazy"
                  alt=""
                  src="/group-1000010348.svg"
                />
                <div class="font-light">{{ ready }}</div>
              </div>
              <div class="flex items-center gap-2">
                <div class="w-1.5 h-1.5 rounded-full bg-limegreen"></div>
                <div class="font-light">{{ readyToServe }}</div>
                <img class="w-3 h-3" alt="" src="/group-1171275328.svg" />
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Date and Time -->
      <div
        class="flex justify-between text-base text-white mq450:flex-wrap relative z-10"
      >
        <div class="font-light">Wednesday, 28, 2024</div>
        <div class="font-light">4:48 PM</div>
      </div>
    </div>

    <!-- Divider Image -->
    <img
      class="w-full max-h-full relative z-10"
      loading="lazy"
      alt=""
      :src="orderDivider"
    />

    <!-- Order Details -->
    <div class="flex flex-row gap-6 mq450:flex-wrap relative z-10">
      <div class="flex flex-col gap-2.5">
        <div class="text-gray-200 font-light">Qty</div>
        <div class="font-light">01</div>
        <div class="font-light">01</div>
        <div class="font-light">02</div>
        <div class="font-light">01</div>
      </div>
      <div class="flex-1 flex flex-col gap-2.5">
        <div class="text-gray-200 font-light">Items</div>
        <div class="font-light">Scrambled eggs with toast</div>
        <div class="font-light">Smoked Salmon Bagel</div>
        <div class="font-light">Belgian Waffles</div>
        <div class="font-light">Classic Lemonade</div>
      </div>
      <div class="w-16 flex flex-col items-end gap-2.5 text-right">
        <div class="text-gray-200 font-light">Price</div>
        <div class="font-light">$199</div>
        <div class="font-light">$120</div>
        <div class="font-light">$220</div>
        <div class="font-light">$110</div>
      </div>
    </div>

    <!-- Divider Image -->
    <img
      class="w-full max-h-full relative z-10"
      loading="lazy"
      alt=""
      :src="itemDivider"
    />

    <!-- Subtotal and Buttons -->
    <div class="w-full flex flex-col gap-6 relative z-10">
      <div class="flex justify-between">
        <div class="font-light">SubTotal</div>
        <div class="font-light">$649</div>
      </div>
      <div class="flex gap-4">
        <button
          class="flex-1 border border-green-300 py-4 px-6 rounded flex items-center justify-center"
        >
          <img
            class="h-6 w-6"
            loading="lazy"
            alt=""
            src="/group-1000010360.svg"
          />
        </button>
        <button
          class="flex-1 border border-green-300 py-4 px-6 rounded flex items-center justify-center"
        >
          <img
            class="h-6 w-6"
            loading="lazy"
            alt=""
            src="/group-1000010359.svg"
          />
        </button>
        <button
          class="flex-1 bg-green-300 py-4 px-10 rounded text-white font-medium"
        >
          Pay Bill
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "FrameComponent2",
  props: {
    separator: { type: String },
    ready: { type: String },
    readyToServe: { type: String },
    orderDivider: { type: String },
    itemDivider: { type: String },
  },
});
</script>
