<template>
  <v-container fluid class="pa-0">
    <v-row>
      <!-- Left Sidebar for Filtering -->
      <v-col cols="3" class="pa-0">
        <v-card class="pa-4 bg-gray-800 white--text" outlined>
          <v-card-title class="headline font-weight-bold"
            >{{ totalProducts }} total products</v-card-title
          >

          <!-- Product Status -->
          <v-row class="mt-4">
            <v-col cols="12">
              <p class="font-weight-bold">Product Status</p>
              <v-chip-group active-class="pink--text" column>
                <v-chip class="ma-2" outlined
                  >All
                  <span class="ml-2 pink--text"
                    >({{ totalProducts }})</span
                  ></v-chip
                >
                <v-chip class="ma-2" outlined
                  >Active
                  <span class="ml-2">({{ activeProducts }})</span></v-chip
                >
                <v-chip class="ma-2" outlined
                  >Inactive
                  <span class="ml-2">({{ inactiveProducts }})</span></v-chip
                >
                <v-chip class="ma-2" outlined
                  >Draft <span class="ml-2">({{ draftProducts }})</span></v-chip
                >
              </v-chip-group>
            </v-col>
          </v-row>

          <!-- Other Filters (category, stock, etc.) -->
          <!-- Same as previously implemented -->

          <!-- Reset Button -->
          <v-row class="mt-4">
            <v-col cols="12">
              <v-btn color="pink" block large @click="resetFilters"
                >Reset Filters</v-btn
              >
            </v-col>
          </v-row>
        </v-card>
      </v-col>

      <!-- Right Inventory List -->
      <v-col cols="9" class="pa-0">
        <v-btn class="ml-4 mb-4 pink lighten-3" large @click="addNewInventory"
          >Add New Inventory</v-btn
        >
        <ProductTable :categoryItems="filteredInventory" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import ProductTable from "../components/Menu/ProductTable.vue"; // Assuming ProductTable is your existing component
import { fetchItemOptions, fetchInventory } from "@eatify/shared/src/apiClient"; // The function you provided
import { Inventory } from "@eatify/shared/src/types"; // Assuming types are declared

export default defineComponent({
  name: "Inventory",
  components: {
    ProductTable,
  },
  setup() {
    const restaurantId = 1; // For example purposes, assuming restaurant ID is 1
    const totalProducts = ref(0);
    const activeProducts = ref(0);
    const inactiveProducts = ref(0);
    const draftProducts = ref(0);
    const filteredInventory = ref<Inventory[]>([]);

    // Fetch and display inventory and item options for a restaurant
    const loadInventory = async () => {
      try {
        const inventory = await fetchInventory(restaurantId);
        filteredInventory.value = inventory;
        totalProducts.value = inventory.length;
        activeProducts.value = inventory.filter(
          (item) => item.item_option.is_in_stock
        ).length;
        inactiveProducts.value = totalProducts.value - activeProducts.value;
      } catch (error) {
        console.error("Error fetching inventory:", error);
      }
    };

    // Fetch Item Options (if needed for other features)
    const loadItemOptions = async () => {
      try {
        const itemOptions = await fetchItemOptions(restaurantId);
        console.log(itemOptions);
      } catch (error) {
        console.error("Error fetching item options:", error);
      }
    };

    onMounted(() => {
      loadInventory();
      loadItemOptions(); // If you need to load item options for additional features
    });

    const resetFilters = () => {
      // Reset all filters
    };

    const addNewInventory = () => {
      // Logic to add new inventory
    };

    return {
      totalProducts,
      activeProducts,
      inactiveProducts,
      draftProducts,
      filteredInventory,
      resetFilters,
      addNewInventory,
    };
  },
});
</script>

<style scoped>
.white--text {
  color: white !important;
}

.bg-gray-800 {
  background-color: #212121 !important;
}

.pink--text {
  color: #ff7ca3 !important;
}
</style>
