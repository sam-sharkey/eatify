<template>
  <div class="w-full h-auto text-left text-sm text-white font-poppins pt-10">
    <!-- Table Header -->
    <div class="flex items-center justify-start px-6 bg-gray-800 text-white">
      <input class="mr-4 w-4 h-4 border border-white rounded" type="checkbox" />
      <span class="w-24 text-base text-white">Product</span>
      <span class="w-48 font-medium">Product Name</span>
      <span class="w-20 font-medium">Item ID</span>
      <span class="w-20 font-medium">Stock</span>
      <span class="w-28 font-medium text-right">Category</span>
      <span class="w-20 font-medium text-right">Price</span>
      <span class="w-24 font-medium text-right">Availability</span>
    </div>

    <!-- Table Rows -->
    <div class="divide-y divide-gray-600 pt-5">
      <FrameComponent1 propBackgroundColor="#3d4142" />
      <FrameComponent1 propBackgroundColor="#292c2d" />
      <FrameComponent1 propBackgroundColor="#3d4142" />
      <FrameComponent1 propBackgroundColor="#292c2d" />
      <FrameComponent1 propBackgroundColor="#3d4142" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import FrameComponent1 from "./FrameComponent1.vue";

export default defineComponent({
  name: "ProductTable",
  components: {
    FrameComponent1,
  },
});
</script>

<style scoped>
/* Add any scoped styles here, if necessary */
</style>
