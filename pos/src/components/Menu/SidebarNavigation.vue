<template>
  <div
    class="flex flex-col text-base items-center w-[180px] h-full bg-darkslategray-300 text-white font-poppins rounded-tr-11xl rounded-br-11xl"
  >
    <!-- Header with Logo -->
    <div class="flex flex-col items-center py-4">
      <h1 class="text-2xl font-semibold text-green-300">EATIFY</h1>
    </div>

    <!-- Dashboard -->
    <div class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl">
      <img src="/magedashboardfill.svg" alt="Dashboard" class="w-8 h-8 mb-2" />
      <span>Dashboard</span>
    </div>

    <!-- Navigation Items -->
    <div class="flex flex-col space-y-4 mt-4 w-3/4">
      <!-- Menu Item -->
      <button class="flex flex-col items-center p-4 bg-green-300 rounded-xl">
        <img src="/group-1000010111.svg" alt="Menu" class="w-8 h-8 mb-2" />
        <span class="text-darkslategray-200">Menu</span>
      </button>

      <!-- Staff -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl"
      >
        <img src="/group-1000010114.svg" alt="Staff" class="w-8 h-8 mb-2" />
        <span>Staff</span>
      </div>

      <!-- Inventory -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl"
      >
        <img src="/group-1000010130.svg" alt="Inventory" class="w-8 h-8 mb-2" />
        <span>Inventory</span>
      </div>

      <!-- Order/Table -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl"
      >
        <img
          src="/group-1000010123.svg"
          alt="Order/Table"
          class="w-8 h-8 mb-2"
        />
        <span>Order/Table</span>
      </div>

      <!-- Reservation -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl"
      >
        <img
          src="/group-1000010118.svg"
          alt="Reservation"
          class="w-8 h-8 mb-2"
        />
        <span>Reservation</span>
      </div>

      <!-- Reports -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl"
      >
        <img src="/group-1000010123.svg" alt="Reports" class="w-8 h-8 mb-2" />
        <span>Reports</span>
      </div>

      <!-- Logout -->
      <div
        class="flex flex-col items-center p-2 bg-darkslategray-300 rounded-xl mt-auto"
      >
        <img src="/group-1000010086.svg" alt="Logout" class="w-8 h-8 mb-2" />
        <span>Logout</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SidebarNavigation",
});
</script>
