<template>
  <div
    class="flex flex-col items-center justify-center min-h-screen bg-antiquewhite"
  >
    <h2 class="text-3xl font-semibold mb-8">Finish up your pickup order</h2>
    <div class="w-full max-w-6xl grid grid-cols-1 md:grid-cols-3 gap-8">
      <!-- Left Section (Pickup Details + Payment Method) -->
      <div class="col-span-2 grid grid-cols-1 gap-8">
        <!-- Pickup Details -->
        <div class="p-6 bg-white rounded-md shadow-lg">
          <h3 class="text-lg font-medium mb-4">Pickup details</h3>
          <div class="flex flex-col space-y-4">
            <!-- Pickup Time -->
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2">
                <img
                  src="/icons/clock.svg"
                  alt="Pickup time icon"
                  class="w-6 h-6"
                />
                <p>Pickup Time</p>
              </div>
              <p class="text-gray-600">ASAP - Today, 2:15 PM</p>
            </div>
            <!-- Location -->
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2">
                <img
                  src="/icons/location.svg"
                  alt="Location icon"
                  class="w-6 h-6"
                />
                <p>Meatpacking</p>
              </div>
              <p class="text-gray-600">32 Gansevoort St, New York, NY 10014</p>
            </div>
            <!-- Contact Information -->
            <div class="flex items-center justify-between">
              <div class="flex items-center space-x-2">
                <img src="/icons/phone.svg" alt="Phone icon" class="w-6 h-6" />
                <p>Sam</p>
              </div>
              <p class="text-gray-600">(574) 807-1068</p>
            </div>
          </div>
        </div>

        <!-- Payment Method -->
        <div class="p-6 bg-white rounded-md shadow-lg">
          <h3 class="text-lg font-medium mb-4">Payment method</h3>
          <div class="flex flex-col space-y-4">
            <!-- Payment Method Selector -->
            <div
              class="border rounded-md p-4 flex items-center justify-between"
            >
              <p>Select payment method</p>
              <img
                src="/icons/arrow-right.svg"
                alt="Arrow right"
                class="w-4 h-4"
              />
            </div>
            <!-- Add Gift Card -->
            <div class="border rounded-md p-4">
              <p>Add gift card</p>
            </div>
            <!-- Enter Promo Code -->
            <div class="border rounded-md p-4">
              <p>Enter promo code</p>
              <p class="text-gray-600 text-sm">
                Some promo codes will generate new rewards that can only be
                applied to an active order in your bag.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Section (Order Summary) -->
      <div class="p-6 bg-white rounded-md shadow-lg">
        <h3 class="text-lg font-medium mb-4">Your order</h3>
        <div class="flex flex-col space-y-4">
          <!-- Order Item -->
          <div class="flex justify-between items-center">
            <img
              src="/menu_images/steakhouse_chopped.png"
              alt="Order image"
              class="w-20 h-20 rounded-md"
            />
            <div class="text-sm">
              <p class="font-medium">Steakhouse Chopped</p>
              <p class="text-gray-500">Dressing on the side</p>
            </div>
            <div class="text-right">
              <p class="font-medium">$17.15</p>
              <p class="text-gray-500 text-sm">1x</p>
            </div>
          </div>

          <!-- Subtotal, Tax, Total -->
          <div class="border-t border-gray-200 pt-4">
            <div class="flex justify-between">
              <p>Subtotal</p>
              <p>$17.15</p>
            </div>
            <div class="flex justify-between">
              <p>Tax</p>
              <p>$1.52</p>
            </div>
            <div class="flex justify-between font-semibold">
              <p>Total</p>
              <p>$18.67</p>
            </div>
          </div>

          <!-- Allergens + Cancelation Disclaimer -->
          <div class="text-sm text-gray-600">
            <p>Allergens Disclaimer</p>
            <p>
              At sweetgreen, we use all major allergens in our kitchens, so we
              cannot guarantee that our food is completely free of any allergen.
            </p>
            <p class="mt-2">Cancellation Policy</p>
            <p>No changes to the order can be made after placing your order.</p>
          </div>

          <!-- Place Order Button -->
          <button
            class="w-full py-4 bg-darkslategray-200 text-white rounded-lg font-semibold"
            @click="placeOrderOnClick"
          >
            Place order
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useItemStore } from "@/stores/itemStore"; // Assuming the pinia store for item management
//import { useUserStore } from "@/stores/userStore"; // Assuming user store for address, user info
import { useRestaurantStore } from "@/stores/restaurant"; // Assuming restaurant store for location
import { placeOrder } from "@/services/apiClient";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "CompleteOrderPage",
  setup() {
    const itemStore = useItemStore(); // Store for selected items
    //const userStore = useUserStore(); // Store for user info (address)
    const restaurantStore = useRestaurantStore(); // Store for restaurant location
    const router = useRouter();

    // Prepare the order data
    const prepareOrderData = () => {
      const total_cost = Object.values(itemStore.selectedItems).reduce(
        (total, selectedItem) => {
          return total + selectedItem.item_option.cost * selectedItem.quantity;
        },
        0
      );

      const orderData = {
        item_options: Object.values(itemStore.selectedItems),
        delivery_type: "pickup", // or "delivery" based on user selection
        store_location: "London", //restaurantStore.location.name,
        user_address: "London", //userStore.address,
        total_cost: total_cost, // assuming total_cost is computed in itemStore
        order_time: new Date().toISOString(),
      };

      return orderData;
    };

    // Function to handle placing the order
    const placeOrderOnClick = async () => {
      const orderData = prepareOrderData();

      const orderId = await placeOrder(
        restaurantStore.restaurant.id,
        orderData
      );
      if (orderId) {
        // Route to CompleteOrderPage and pass orderId
        router.push({
          name: "OrderConfirmation",
          params: { orderId: orderId.message },
        });
      }
    };

    return {
      placeOrderOnClick,
    };
  },
});
</script>

<style scoped>
/* You can add scoped CSS here */
</style>
