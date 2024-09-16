<template>
  <div class="w-full h-full flex flex-row bg-antiquewhite flex flex-col">
    <!-- Sidebar Cart -->
    <div
      class="w-[400px] bg-oldlace border-l border-gray-200 flex flex-col justify-between px-8 py-6"
    >
      <!-- Location Information -->
      <section>
        <h3 class="text-lg font-semibold">Review your pickup order</h3>
        <div class="mt-4">
          <h4 class="text-sm font-medium">Meatpacking</h4>
          <p class="text-xs text-gray-500">
            32 Gansevoort St<br />
            New York, NY, 10014
          </p>
        </div>

        <!-- Rewards Section -->
        <div class="mt-6 border-t pt-4">
          <h4 class="text-sm font-medium">Your rewards</h4>
          <p class="text-xs text-gray-500 mt-2">
            Sign in to use your available rewards. Don't have an account? <br />
            <a href="#" class="underline text-green-700">Create one</a> and
            learn more about Rewards + Challenges.
          </p>
        </div>

        <!-- Order Summary -->
        <div class="mt-6 border-t pt-4">
          <h4 class="text-sm font-medium">Your order</h4>
          <div
            v-for="(item, index) in orderItems"
            :key="index"
            class="flex justify-between items-center mt-4"
          >
            <div class="flex items-center">
              <img
                :src="item.image_src"
                alt="item.name"
                class="w-16 h-16 rounded-md mr-4"
              />
              <div>
                <p class="text-sm font-semibold">{{ item.name }}</p>
                <p class="text-xs text-gray-500">{{ item.details }}</p>
              </div>
            </div>
            <div class="flex flex-col items-end">
              <span class="text-sm font-medium">{{ item.price }}</span>
              <div class="flex items-center mt-1">
                <span class="text-sm">{{ item.quantity }}x</span>
                <button
                  class="ml-2 text-gray-500 hover:text-red-600"
                  @click="removeItem(index)"
                >
                  <img src="/remove-icon.svg" alt="remove" class="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Great Additions Section -->
      <section class="mt-6">
        <h4 class="text-sm font-medium">Great additions</h4>
        <div class="flex mt-4 gap-4 overflow-x-auto no-scrollbar">
          <div v-for="(addition, index) in additions" :key="index" class="w-24">
            <img
              :src="addition.image"
              alt="addition.name"
              class="w-full h-24 object-cover rounded-md"
            />
            <p class="text-xs mt-2 text-center">{{ addition.name }}</p>
          </div>
        </div>
      </section>
    </div>
    <!-- Buttons Section -->
    <footer class="flex justify-between mt-6">
      <button
        @click="viewMenu"
        class="py-3 px-8 bg-transparent border border-gray-300 rounded-lg"
      >
        View menu
      </button>
      <button
        @click="checkout"
        class="py-3 px-8 bg-darkslategray-200 text-white rounded-lg"
      >
        Check out
      </button>
    </footer>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "CartPage",
  setup() {
    const router = useRouter();
    // Example data, this should be replaced with your dynamic order data
    const orderItems = ref([
      {
        name: "Steakhouse Chopped",
        details: "Dressing on the side",
        price: "$17.15",
        quantity: 1,
        image_src: "/images/steakhouse_chopped.png", // Use actual path
      },
      // Add more items as needed
    ]);

    const additions = ref([
      {
        name: "SG X Siete: Green Goddess Ranch Chips",
        image: "/images/chips_goddess_ranch.png",
      },
      {
        name: "Olipop Vintage Cola",
        image: "/images/olipop_vintage_cola.png",
      },
      {
        name: "OLIPOP Lemon Lime Soda",
        image: "/images/olipop_lemon_lime.png",
      },
      // Add more great additions
    ]);

    const viewMenu = () => {
      router.push({ name: "Menu" }); // Navigate to the OrderPage
    };

    const checkout = () => {
      // Logic for checkout
    };

    const removeItem = (index: number) => {
      orderItems.value.splice(index, 1); // Remove item from order
    };

    return {
      orderItems,
      additions,
      viewMenu,
      checkout,
      removeItem,
    };
  },
});
</script>

<style scoped>
/* You can add styling for the scrollbar here */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>
