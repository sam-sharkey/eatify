<template>
  <div
    class="flex flex-col items-center justify-center w-full h-screen bg-oldlace"
  >
    <!-- Order Confirmation Header -->
    <div class="text-center mb-8">
      <h1 class="text-4xl font-semibold text-darkslategray-200">
        Order Confirmed!
      </h1>
      <p class="text-lg text-gray-600 mt-2">Thank you for your order</p>
    </div>

    <!-- Order Details Section -->
    <div
      v-if="order"
      class="bg-white p-8 rounded-lg shadow-md w-full max-w-4xl"
    >
      <!-- Pickup/Delivery Information -->
      <div class="mb-6">
        <h2 class="text-xl font-medium text-darkslategray-200">
          Your order details
        </h2>
        <div class="mt-4">
          <p class="text-md text-gray-700">
            <strong>Order ID:</strong> {{ order.id }}
          </p>
          <p class="text-md text-gray-700">
            <strong>Pickup Location:</strong> {{ order.store_location }}
          </p>
          <p class="text-md text-gray-700">
            <strong>Pickup Time:</strong> {{ order.time }}
          </p>
        </div>
      </div>

      <!-- Ordered Items -->
      <div class="mb-6">
        <h3 class="text-lg font-medium text-darkslategray-200">Your Items</h3>
        <div class="mt-4">
          <ul>
            <li
              v-for="item in order.item_options"
              :key="item.id"
              class="border-b border-gray-200 py-2 flex justify-between"
            >
              <span class="text-md text-gray-700"
                >{{ item.item_name }} x {{ item.quantity }}</span
              >
              <span class="text-md text-gray-700"
                >${{ (item.item_price * item.quantity).toFixed(2) }}</span
              >
            </li>
          </ul>
        </div>
      </div>

      <!-- Price Summary -->
      <div class="mt-6 border-t border-gray-100 pt-4">
        <div class="flex justify-between text-lg font-semibold">
          <p>Total:</p>
          <p>${{ order.total_cost }}</p>
        </div>
      </div>
    </div>

    <!-- Button to go back to home -->
    <div class="mt-8">
      <button
        @click="goToHomePage"
        class="py-4 px-16 bg-darkslategray-200 text-white rounded-2xl shadow-md hover:bg-darkslategray-300"
      >
        Return to Home
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, onMounted, defineComponent } from "vue";
import { useRouter } from "vue-router";
import { getOrders } from "@/services/apiClient";

export default defineComponent({
  name: "OrderConfirmationPage",
  props: {
    orderId: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const order = ref(null); // The order details
    const router = useRouter(); // Use vue-router

    // Function to load order details
    const loadOrderDetails = async () => {
      try {
        const orderData = await getOrders(props.orderId, null); // API call to get the order details
        order.value = orderData[0];
      } catch (error) {
        console.error("Failed to load order:", error);
      }
    };

    // Load order details when the component mounts
    onMounted(() => {
      loadOrderDetails();
    });

    // Function to go back to the home page
    const goToHomePage = () => {
      router.push({ name: "Home" });
    };

    return {
      order,
      goToHomePage,
    };
  },
});
</script>

<style scoped>
/* You can add global styles here or move to a separate CSS/SCSS file for better organization */
</style>
