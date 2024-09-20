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
          <div class="font-medium mq450:text-xl">
            {{ order.id }}
          </div>
        </div>
        <div class="flex-1 flex flex-col gap-4 text-left">
          <div class="flex justify-between gap-4">
            <div class="flex flex-col gap-1">
              <div class="font-medium text-white">{{ order.user_address }}</div>
              <div class="flex flex-col-2 gap-6">
                <div class="text-sm text-white font-light">
                  Order # {{ order.id }}
                </div>
                <div class="text-sm text-white font-light">
                  {{ order.delivery_type.toUpperCase() }}
                </div>
              </div>
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
                <div class="font-light text-base text-white">
                  {{ order.status }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Date and Time -->
      <div
        class="flex justify-between text-base text-white mq450:flex-wrap relative z-10"
      >
        <div class="font-light">{{ formatDate(order.order_time) }}</div>
        <div class="font-light">{{ formatTime(order.order_time) }}</div>
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
        <div
          v-for="item in order.items"
          :key="item.item_name"
          class="font-light"
        >
          {{ item.quantity }}
        </div>
      </div>
      <div class="flex-1 flex flex-col gap-2.5">
        <div class="text-gray-200 font-light">Items</div>
        <div
          v-for="item in order.items"
          :key="item.item_name"
          class="font-light"
        >
          {{ item.item_name }}
        </div>
      </div>
      <div class="w-16 flex flex-col items-end gap-2.5 text-right">
        <div class="text-gray-200 font-light">Price</div>
        <div
          v-for="item in order.items"
          :key="item.item_name"
          class="font-light"
        >
          ${{ item.item_price }}
        </div>
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
        <div class="font-light">${{ order.total_cost }}</div>
      </div>
      <div class="flex gap-4">
        <button
          class="flex-1 border border-green-300 py-4 px-6 rounded flex items-center justify-center bg-darkslategray-200"
        >
          <img
            class="h-6 w-6"
            loading="lazy"
            alt=""
            src="/group-1000010360.svg"
          />
        </button>
        <button
          class="flex-1 border border-green-300 py-4 px-6 rounded flex items-center justify-center bg-darkslategray-200"
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
  name: "OrderComponent",
  props: {
    order: {
      type: Object,
      required: true,
    },
    orderDivider: {
      type: String,
      required: true,
    },
    itemDivider: {
      type: String,
      required: true,
    },
  },
  methods: {
    formatDate(dateString: string) {
      const date = new Date(dateString);
      return date.toLocaleDateString(undefined, {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    formatTime(dateString: string) {
      const date = new Date(dateString);
      return date.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      });
    },
  },
});
</script>
