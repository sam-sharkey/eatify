<template>
  <div
    class="w-full flex flex-col items-start justify-start pt-0 px-8 pb-6 gap-4 max-w-[1520px] text-center text-gray-700 font-inter"
  >
    <!-- First Row of Items -->
    <div class="w-full grid grid-cols-3 gap-2 justify-center pb-4">
      <ProductCard
        initialQuantity="1"
        itemName="Spring Mix"
        containerImage="/container1@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Wild Rice"
        containerImage="/container-110@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Apples"
        containerImage="/container-110@2x.png"
      />
    </div>

    <!-- Second Row of Items -->
    <div class="w-full grid grid-cols-3 gap-2 justify-center pb-4">
      <ProductCard
        initialQuantity="1"
        itemName="Za'atar Breadcrumbs"
        containerImage="/container-25@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Veg Slaw"
        containerImage="/container-310@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Blackened Chicken"
        containerImage="/container-44@2x.png"
      />
    </div>

    <!-- Third Row of Items (Grid) -->
    <div class="w-full grid grid-cols-3 gap-2 justify-center pb-4">
      <ProductCard
        initialQuantity="1"
        itemName="Blue Cheese"
        containerImage="/container-51@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Hard Boiled Egg"
        containerImage="/container-61@2x.png"
      />
      <ProductCard
        initialQuantity="1"
        itemName="Parmesan Crisps"
        containerImage="/container-71@2x.png"
      />
    </div>

    <!-- Last Item Row -->
    <div class="w-[153.3px] flex items-start justify-start pb-2">
      <ProductCard
        initialQuantity="1"
        itemName="Balsamic Vinaigrette"
        containerImage="/container-81@2x.png"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ProductCard from "./ProductCard.vue"; // Replaced ListItem2 with the modern ProductCard component

export default defineComponent({
  name: "SelectedIngredients",
  components: {
    ProductCard,
  },
});
</script>
