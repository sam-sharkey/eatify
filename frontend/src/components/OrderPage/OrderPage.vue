<template>
  <div class="max-h-[calc(100vh-150px)] flex flex-row bg-oldlace">
    <!-- Sidebar -->
    <div
      class="w-[525px] max-w-full bg-oldlace border-r border-gray-100 overflow-auto shrink-0"
    >
      <!-- Header -->
      <header class="p-6">
        <div class="flex justify-between items-center mb-2">
          <h1 class="text-3xl font-semibold">Create Your Own</h1>
          <img src="/svg1.svg" alt="Logo" class="w-8 h-8" loading="lazy" />
        </div>
        <p class="text-sm text-gray-600">$19.70 - 915 cal</p>
      </header>

      <!-- Selected Ingredients -->
      <SelectedIngredients class="overflow-y-auto max-h-[calc(100vh-150px)]" />

      <!-- Footer -->
      <!--footer class="p-4 border-t border-gray-100">
        <div class="flex justify-between">
          <button class="py-2 px-8 border border-gray-100 rounded-lg">
            Cancel
          </button>
          <button class="py-2 px-8 bg-darkslategray-200 text-white rounded-lg">
            I'm done
          </button>
        </div>
      </footer-->
    </div>

    <!-- Options Menu -->
    <div class="flex-1 overflow-hidden">
      <!-- Scrollable container -->
      <div class="flex-1 overflow-auto max-h-[calc(100vh-150px)]">
        <OptionsMenu class="h-full w-full" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SelectedIngredients from "./SelectedIngredients.vue";
import OptionsMenu from "./OptionsMenu.vue";

export default defineComponent({
  name: "CustomOrder",
  components: {
    SelectedIngredients,
    OptionsMenu,
  },
});
</script>

<style scoped>
/* You can add global styles here or move to a separate CSS/SCSS file for better organization. */
</style>
