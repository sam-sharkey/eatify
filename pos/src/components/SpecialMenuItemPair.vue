<template>
  <div
    class="min-h-28 relative flex-1 p-4 text-left text-base text-white font-poppins bg-darkslategray-300 rounded-md"
  >
    <!-- Item Info -->
    <div class="flex flex-col justify-end h-full">
      <span class="text-lg font-medium">{{ name }}</span>
      <span class="text-sm font-light">{{ items }}</span>
    </div>

    <!-- Icon -->
    <img
      :src="groupIcon"
      alt="menu icon"
      class="absolute top-4 right-4 w-10 h-10"
      loading="lazy"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SpecialMenuItemPair",
  props: {
    items: {
      type: String,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
    groupIcon: {
      type: String,
      required: true,
    },
  },
});
</script>

<style scoped>
/* Additional styles can be added here if necessary */
</style>
