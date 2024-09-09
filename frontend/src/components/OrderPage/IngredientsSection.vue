<template>
  <div
    class="w-full flex flex-col items-start justify-start pt-10 px-0 pb-10 gap-4 max-w-full text-center text-2xl text-gray-700 font-inter"
  >
    <!-- Title -->
    <div class="w-full text-left tracking-wider leading-7">Toppings</div>

    <!-- Toppings Grid -->
    <div
      class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8"
    >
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Crispy Onions"
        containerImage="/container-151@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Pickled Onions"
        containerImage="/container-171@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Basil"
        containerImage="/container-191@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Raw Carrots"
        containerImage="/container-201@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Chickpeas"
        containerImage="/container-211@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Cilantro"
        containerImage="/container-221@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Cucumbers"
        containerImage="/container-231@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Roasted Sweet Potatoes"
        containerImage="/container-241@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Shredded Cabbage"
        containerImage="/container-251@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Spicy Broccoli"
        containerImage="/container-261@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Tomatoes"
        containerImage="/container-271@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Crispy Rice"
        containerImage="/container-281@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Roasted Almonds"
        containerImage="/container-291@2x.png"
      />
      <ProductCard
        backgroundImage="/background-10.svg"
        itemName="Tortilla Chips"
        containerImage="/container-301@2x.png"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ProductCard from "./ProductCard.vue"; // Import the ProductCard component

export default defineComponent({
  name: "IngredientsSection",
  components: { ProductCard },
});
</script>

<style scoped>
/* Additional custom styles can be added here */
</style>
