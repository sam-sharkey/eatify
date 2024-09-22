<template>
  <div
    class="flex flex-col text-base items-center w-[180px] h-full bg-darkslategray-300 text-white font-poppins rounded-tr-11xl rounded-br-11xl"
  >
    <!-- Header with Logo -->
    <div class="flex flex-col items-center pt-4">
      <h1 class="text-2xl font-semibold text-green-300">EATIFY</h1>
    </div>

    <!-- Dashboard -->
    <div
      class="flex flex-col items-center p-4 rounded-xl"
      @click="navigateTo('/dashboard', 'dashboard')"
      :class="
        selected === 'dashboard'
          ? 'bg-green-300 text-black'
          : 'bg-darkslategray-300 text-white'
      "
    >
      <img src="/magedashboardfill.svg" alt="Dashboard" class="w-8 h-8 mb-2" />
      <span>Dashboard</span>
    </div>

    <!-- Navigation Items -->
    <div class="flex flex-col space-y-4 mt-4 w-3/4">
      <!-- Menu Item -->
      <div
        class="flex flex-col items-center p-4 rounded-xl"
        @click="navigateTo('/menu', 'menu')"
        :class="
          selected === 'menu'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
      >
        <img src="/group-1000010111.svg" alt="Menu" class="w-8 h-8 mb-2" />
        <span>Menu</span>
      </div>

      <!-- Staff -->
      <div
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl"
        @click="navigateTo('/staff', 'staff')"
        :class="
          selected === 'staff'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
      >
        <img src="/group-1000010114.svg" alt="Staff" class="w-8 h-8 mb-2" />
        <span>Staff</span>
      </div>

      <!-- Inventory -->
      <div
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl"
        @click="navigateTo('/inventory', 'inventory')"
        :class="
          selected === 'inventory'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
      >
        <img src="/group-1000010130.svg" alt="Inventory" class="w-8 h-8 mb-2" />
        <span>Inventory</span>
      </div>

      <!-- Order/Table -->
      <div
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl"
        @click="navigateTo('/orders', 'orders')"
        :class="
          selected === 'orders'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
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
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl"
        @click="navigateTo('/reservation', 'reservation')"
        :class="
          selected === 'reservation'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
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
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl"
        @click="navigateTo('/reports', 'reports')"
        :class="
          selected === 'reports'
            ? 'bg-green-300 text-black'
            : 'bg-darkslategray-300 text-white'
        "
      >
        <img src="/group-1000010123.svg" alt="Reports" class="w-8 h-8 mb-2" />
        <span>Reports</span>
      </div>

      <!-- Logout -->
      <div
        class="flex flex-col items-center p-4 bg-darkslategray-300 rounded-xl mt-auto"
      >
        <img src="/group-1000010086.svg" alt="Logout" class="w-8 h-8 mb-2" />
        <span>Logout</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "SidebarNavigation",
  setup() {
    const router = useRouter();

    // State to track the currently selected item, defaulting to 'menu'
    const selected = ref("menu");

    onMounted(() => {
      router.push("/menu");
    });

    // Function to navigate to the specified route and update the selected item
    const navigateTo = (path: string, item: string) => {
      selected.value = item;
      router.push(path);
    };

    return {
      selected,
      navigateTo,
    };
  },
});
</script>
