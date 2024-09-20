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
      <div
        v-for="(item, index) in categoryItems"
        :key="index"
        class="flex items-center justify-start px-6 py-3"
        :class="
          index % 2 === 0 ? 'bg-darkslategray-300' : 'bg-darkslategray-400'
        "
      >
        <input
          class="mr-4 w-4 h-4 border border-white rounded"
          type="checkbox"
        />
        <span>
          <img
            :src="item.image_src"
            alt="menu icon"
            class="w-10 h-10 mr-14"
            loading="lazy"
        /></span>
        <span class="w-48">{{ item.name }}</span>
        <span class="w-20">{{ item.id }}</span>
        <span class="w-20">{{ item.stock || "N/A" }}</span>
        <span class="w-28 text-right">{{ item.classification }}</span>
        <span class="w-20 text-right">${{ item.price }}</span>
        <span class="w-24 text-right">{{
          item.is_in_stock ? "Available" : "Out of Stock"
        }}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "ProductTable",
  props: {
    categoryItems: {
      type: Array as PropType<
        Array<{
          name: string;
          id: number;
          classification: string;
          stock: number;
          price: number;
          is_in_stock: boolean;
        }>
      >,
      required: true,
    },
  },
});
</script>

<style scoped>
/* Add any scoped styles here, if necessary */
</style>
