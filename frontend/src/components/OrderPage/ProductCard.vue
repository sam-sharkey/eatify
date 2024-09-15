<template>
  <div
    class="h-48 w-24 flex flex-col items-center justify-center p-2 text-center text-sm text-gray-700 font-inter cursor-pointer"
    @click="addItem"
  >
    <div
      class="relative flex-1 rounded-xl p-3 z-10 flex flex-col items-center justify-start"
      :class="quantity > 0 ? 'bg-honeydew' : 'bg-antiquewhite'"
    >
      <!-- Item Name -->
      <div class="w-24 py-2 px-5 text-center">
        <div class="leading-4 overflow-hidden">
          <span class="inline-block">{{ itemName }}</span>
        </div>
      </div>
      <!-- Container Image -->
      <div
        class="w-full flex flex-col items-center justify-center py-2 text-xs text-white"
      >
        <img
          class="w-full max-w-28 object-cover"
          alt="container image"
          :src="containerImage"
        />
        <!-- Controls: Visible only when selected -->
        <div
          v-if="quantity > 0"
          class="bottom-[-0.5rem] flex flex-row items-center justify-between px-4 z-20"
        >
          <!-- Remove Button -->
          <button
            class="absolute left-4 h-8 w-8 rounded-full bg-oldlace border border-honeydew flex items-center justify-center"
            @click.stop="removeItem"
          >
            <img
              class="w-6 h-6"
              alt="remove item"
              src="/button--remove-spring-mix--svg.svg"
            />
          </button>
          <!-- Quantity Display -->
          <div
            class="absolute right-4 rounded-full bg-darkslategray-200 border border-honeydew flex items-center justify-center px-2 py-1"
            @click="addItem"
          >
            <span class="text-sm">{{ quantity }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useItemStore } from "@/stores/itemStore"; // Import the store

export default defineComponent({
  name: "ProductCard",
  props: {
    itemName: { type: String, required: true }, // Name of the item
    containerImage: { type: String, required: true }, // Container image URL
    itemId: { type: String, required: true }, // Item ID for tracking quantity
  },
  setup(props) {
    const itemStore = useItemStore(); // Get the current quantity from the store
    const quantity = computed(() => itemStore.getItemQuantity(props.itemId));

    const addItem = () => {
      itemStore.addItem(props.itemId);
    };

    const removeItem = () => {
      itemStore.removeItem(props.itemId);
    };

    return {
      quantity,
      addItem,
      removeItem,
    };
  },
});
</script>

<style scoped>
/* Additional styles can be added here if needed */
</style>
