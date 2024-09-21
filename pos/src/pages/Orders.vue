<template>
  <div
    class="w-full min-h-screen bg-gray-100 px-8 py-10 flex flex-col gap-6 mq450:px-5 mq725:px-12"
  >
    <!-- Header -->
    <header
      class="flex flex-col lg:flex-row items-center justify-between w-full"
    >
      <nav class="flex gap-6 text-base text-white">
        <button
          @click="filterOrders('all')"
          :class="[
            'py-3 px-6 rounded-lg font-medium',
            selectedStatus === 'all'
              ? 'bg-green-300 text-darkslategray-200'
              : 'hover:bg-green-600',
          ]"
        >
          All
        </button>
        <button
          @click="filterOrders('not_started')"
          :class="[
            'py-3 px-6 rounded-lg font-medium',
            selectedStatus === 'not_started'
              ? 'bg-green-300 text-darkslategray-200'
              : 'hover:bg-green-600',
          ]"
        >
          Not Started
        </button>
        <button
          @click="filterOrders('in_progress')"
          :class="[
            'py-3 px-6 rounded-lg font-medium',
            selectedStatus === 'in_progress'
              ? 'bg-green-300 text-darkslategray-200'
              : 'hover:bg-green-600',
          ]"
        >
          In Progress
        </button>
        <button
          @click="filterOrders('ready')"
          :class="[
            'py-3 px-6 rounded-lg font-medium',
            selectedStatus === 'ready'
              ? 'bg-green-300 text-darkslategray-200'
              : 'hover:bg-green-600',
          ]"
        >
          Ready
        </button>
        <button
          @click="filterOrders('delivered')"
          :class="[
            'py-3 px-6 rounded-lg font-medium',
            selectedStatus === 'delivered'
              ? 'bg-green-300 text-darkslategray-200'
              : 'hover:bg-green-600',
          ]"
        >
          Delivered
        </button>
      </nav>
      <div class="flex gap-4 mt-4 lg:mt-0">
        <button
          class="bg-green-300 rounded-lg py-3 px-6 text-darkslategray-200 font-medium hover:bg-green-600"
        >
          Add New Order
        </button>
        <div
          class="flex items-center bg-darkslategray-100 rounded-lg p-4 gap-3 w-full max-w-md"
        >
          <input
            type="text"
            placeholder="Search a name, order, or etc."
            class="w-full bg-transparent border-none text-sm font-light text-white placeholder-white outline-none"
            v-model="searchQuery"
          />
          <img src="/group-1000010362.svg" alt="Search" class="w-5 h-5" />
        </div>
      </div>
    </header>

    <!-- Orders Section -->
    <section class="grid grid-cols-1 lg:grid-cols-3 gap-6 w-full">
      <div
        v-for="order in filteredOrders"
        :key="order.id"
        class="rounded-lg shadow-md"
      >
        <OrderComponent
          :order="order"
          :separator="order.id"
          :ready="order.status"
          :readyToServe="order.statusDetails"
          orderDivider="/vector-147.svg"
          itemDivider="/vector-147.svg"
        />
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, computed } from "vue";
import OrderComponent from "../components/Orders/OrderComponent.vue";
import { getOrders } from "../services/apiClient"; // Make sure the apiClient is correctly imported

export default defineComponent({
  name: "Orders",
  components: {
    OrderComponent,
  },
  setup() {
    const orders = ref([]); // Store fetched orders
    const selectedStatus = ref(""); // To filter by status
    const searchQuery = ref(""); // To filter by search query

    // Fetch orders from the API on mount
    onMounted(async () => {
      try {
        const response = await getOrders(null, 1); // Assuming this returns all orders
        orders.value = response;
      } catch (error) {
        console.error("Error fetching orders:", error);
      }
    });

    // Computed property to filter orders by status
    const filteredOrders = computed(() => {
      return orders.value.filter((order) => {
        // Filter by selectedStatus if provided
        const matchesStatus =
          (selectedStatus.value
            ? order.status === selectedStatus.value
            : true) || selectedStatus.value == "all";

        // Filter by search query if provided
        const matchesSearch = true; //order.name
        // .toLowerCase()
        //.includes(searchQuery.value.toLowerCase());

        return matchesStatus && matchesSearch;
      });
    });

    // Function to set selected status for filtering
    const filterOrders = (status: string) => {
      selectedStatus.value = status;
    };

    return {
      orders,
      selectedStatus,
      searchQuery,
      filteredOrders,
      filterOrders,
    };
  },
});
</script>

<style scoped>
/* Scoped styles or extra classes if needed */
</style>
