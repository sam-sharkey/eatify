<template>
  <div
    class="w-full min-h-screen bg-gray-100 px-8 py-10 flex flex-col gap-6 mq450:px-5 mq725:px-12"
  >
    <!-- Header -->
    <header
      class="flex flex-col lg:flex-row items-center justify-between w-full"
    >
      <div class="flex gap-4 items-center">
        <button
          class="bg-green-300 rounded-lg py-3 px-6 text-darkslategray-200 font-medium hover:bg-pink-300"
        >
          All
        </button>
        <nav class="hidden lg:flex gap-6 text-base text-white">
          <a href="#" class="hover:underline">In Process</a>
          <a href="#" class="hover:underline">Completed</a>
          <a href="#" class="hover:underline">Cancelled</a>
        </nav>
      </div>
      <div class="flex gap-4 mt-4 lg:mt-0">
        <button
          class="bg-green-300 rounded-lg py-3 px-6 text-darkslategray-200 font-medium hover:bg-pink-300"
        >
          Add New Order
        </button>
        <div
          class="flex items-center bg-darkslategray-100 rounded-lg p-4 gap-3 w-full max-w-md"
        >
          <input
            type="text"
            placeholder="Search a name, order, or etc."
            class="w-full bg-transparent border-none text-sm font-light text-white placeholder-white outline-none"
          />
          <img src="/group-1000010362.svg" alt="Search" class="w-5 h-5" />
        </div>
      </div>
    </header>

    <!-- Orders Section -->
    <section class="flex flex-col lg:flex-row gap-6 w-full">
      <FrameComponent2
        separator="01"
        ready="Ready"
        readyToServe="Ready to serve"
        orderDivider="/vector-147.svg"
        itemDivider="/vector-147.svg"
      />
      <FrameComponent2
        separator="02"
        ready="In Process"
        readyToServe="Cooking Now"
        quantityValueBackgroundColor="#ffedbe"
        totalHeaderBackgroundColor="#ffbc0f"
        orderDivider="/vector-147.svg"
        itemDivider="/vector-147.svg"
      />
      <FrameComponent2
        separator="03"
        ready="In Process"
        readyToServe="In the Kitchen"
        quantityValueBackgroundColor="#ffc4c4"
        totalHeaderBackgroundColor="#ff3a3a"
        orderDivider="/vector-147.svg"
        itemDivider="/vector-147.svg"
      />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FrameComponent2 from "../components/Orders/FrameComponent2.vue";

export default defineComponent({
  name: "Orders",
  components: {
    FrameComponent2,
  },
});
</script>

<style scoped>
/* Scoped styles or extra classes if needed */
</style>
