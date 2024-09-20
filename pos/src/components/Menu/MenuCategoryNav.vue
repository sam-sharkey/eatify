<template>
  <section
    class="pr-6 flex flex-col items-start w-full text-left text-white font-poppins"
  >
    <!-- Categories Header -->
    <div class="flex items-center">
      <h2 class="font-medium">Categories</h2>
    </div>

    <!-- Categories Navigation -->
    <nav class="flex flex-row flex-wrap gap-5 w-full">
      <!-- Special Menu Items -->
      <SpecialMenuItemPair
        v-for="(item, index) in menuItems"
        :key="index"
        :items="item.items"
        :name="item.name"
        :groupIcon="item.groupIcon"
        :class="
          selectedItem === index ? 'bg-green-300' : 'bg-darkslategray-300'
        "
        @click="handleSelect(index, item.name)"
      />
    </nav>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import SpecialMenuItemPair from "./SpecialMenuItemPair.vue";

export default defineComponent({
  name: "MenuCategoryNav",
  components: { SpecialMenuItemPair },
  props: {
    menuItems: {
      type: Array,
      required: true,
    },
  },
  setup(_, { emit }) {
    const selectedItem = ref<number | null>(null);

    const handleSelect = (index: number, category: string) => {
      selectedItem.value = index;
      emit("select-category", category);
    };

    return {
      selectedItem,
      handleSelect,
    };
  },
});
</script>

<style scoped>
/* Add any specific styles if necessary */
</style>
