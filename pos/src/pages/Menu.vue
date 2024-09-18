<template>
  <div
    class="relative w-full min-h-screen bg-gray text-left text-white font-poppins px-4"
  >
    <!-- Top Bar with Menu -->
    <div class="flex items-center space-x-4 p-4">
      <img
        src="/group-1000010089@2x.png"
        alt="Menu Icon"
        class="w-8 h-8 object-contain"
        loading="lazy"
      />
      <a href="#" class="text-xl font-medium text-white [text-decoration:none]"
        >Menu</a
      >
    </div>

    <!-- User Profile Section -->
    <div class="absolute top-4 right-8 flex flex-col items-center space-y-2">
      <div
        class="relative flex items-center justify-center bg-pink-100 rounded-full w-10 h-10"
      >
        <span class="text-darkslategray-200 text-sm">01</span>
      </div>
      <img
        src="/ellipse-1@2x.png"
        alt="User Profile"
        class="w-10 h-10 rounded-full object-cover"
        loading="lazy"
      />
    </div>

    <!-- Sidebar -->
    <RightSidebar class="h-full w-full" />

    <!-- Product Table Section -->
    <section class="pt-64 px-4 max-w-7xl mx-auto">
      <ProductTable />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RightSidebar from "../components/RightSidebar.vue";
import ProductTable from "../components/ProductTable.vue";

export default defineComponent({
  name: "Menu",
  components: { RightSidebar, ProductTable },
});
</script>

<style scoped>
/* You can include additional styling here if needed */
</style>
