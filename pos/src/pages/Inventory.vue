<template>
  <v-container fluid>
    <v-row>
      <!-- Left Sidebar for Filtering -->
      <v-col cols="3">
        <v-card class="pa-4 bg-gray-800 text-white" outlined>
          <v-card-title class="headline font-weight-bold"
            >{{ totalProducts }} total products</v-card-title
          >

          <!-- Product Status -->
          <v-row class="mt-4">
            <v-col cols="12">
              <p class="font-weight-bold">Product Status</p>
              <v-chip-group active-class="text-green" column>
                <v-chip class="ma-2" outlined @click="filterByStatus('all')"
                  >All
                  <span class="ml-2 text-green"
                    >({{ totalProducts }})</span
                  ></v-chip
                >
                <v-chip class="ma-2" outlined @click="filterByStatus('active')"
                  >Active
                  <span class="ml-2">({{ activeProducts }})</span></v-chip
                >
                <v-chip
                  class="ma-2"
                  outlined
                  @click="filterByStatus('inactive')"
                  >Inactive
                  <span class="ml-2">({{ inactiveProducts }})</span></v-chip
                >
              </v-chip-group>
            </v-col>
          </v-row>

          <!-- Category Filter -->
          <v-row class="mt-4">
            <v-col cols="12">
              <p class="font-weight-bold">Category</p>
              <v-select
                :items="categories"
                v-model="selectedCategory"
                label="All"
                filled
                class="text-white"
              ></v-select>
            </v-col>
          </v-row>

          <!-- Low Stock Filter -->
          <v-row class="mt-4">
            <v-col cols="12">
              <p class="font-weight-bold">Low in Stock</p>
              <v-checkbox
                v-model="showLowStock"
                label="Low Stock"
                class="text-white"
              ></v-checkbox>
            </v-col>
          </v-row>

          <v-btn class="ml-4 mb-4 bg-green-300" large @click="addNewInventory"
            >Add New Inventory</v-btn
          >
          <v-btn class="ml-4 mb-4 bg-green-300" large @click="sortByQuantity"
            >Sort by Quantity</v-btn
          >

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
      <v-col cols="9">
        <InventoryGrid
          :inventoryItems="filteredInventory"
          @inventory-updated="onInventoryUpdate"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, watch, onMounted } from "vue";
import InventoryGrid from "../components/Inventory/InventoryGrid.vue";
import { fetchInventory } from "@eatify/shared/src/apiClient";
import { Inventory } from "@eatify/shared/src/types";

export default defineComponent({
  name: "Inventory",
  components: {
    InventoryGrid,
  },
  setup() {
    const restaurantId = 1; // Example restaurant ID
    const totalProducts = ref(0);
    const activeProducts = ref(0);
    const inactiveProducts = ref(0);
    const filteredInventory = ref<Inventory[]>([]);
    const inventory = ref<Inventory[]>([]); // All inventory items
    const categories = ref<string[]>(["All"]);
    const selectedCategory = ref("All");
    const showLowStock = ref(false);
    const sortByAscQuantity = ref(true);

    // Fetch and display inventory for the restaurant
    const loadInventory = async () => {
      try {
        const inv = await fetchInventory(restaurantId);
        inventory.value = inv;
        totalProducts.value = inv.length;
        activeProducts.value = inv.filter(
          (item) => item.item_option.is_in_stock
        ).length;
        inactiveProducts.value = totalProducts.value - activeProducts.value;

        // Dynamically set categories based on inventory items
        const uniqueCategories = new Set(
          inv.map((item) => item.item_option.classification)
        );
        categories.value = ["All", ...uniqueCategories];

        applyFilters(); // Apply filters to initialize display
      } catch (error) {
        console.error("Error fetching inventory:", error);
      }
    };

    // Apply filters based on category, low stock, and stock status
    const applyFilters = () => {
      let filtered = [...inventory.value];

      // Filter by category
      if (selectedCategory.value !== "All") {
        filtered = filtered.filter(
          (item) => item.item_option.classification === selectedCategory.value
        );
      }

      // Filter by "low stock"
      if (showLowStock.value) {
        filtered = filtered.filter(
          (item) => item.quantity < item.low_quantity_threshold
        );
      }

      filteredInventory.value = filtered;
    };

    // Sort the inventory by quantity
    const sortByQuantity = () => {
      filteredInventory.value.sort((a, b) => {
        return sortByAscQuantity.value
          ? a.quantity - b.quantity
          : b.quantity - a.quantity;
      });
      sortByAscQuantity.value = !sortByAscQuantity.value; // Toggle sort direction
    };

    // Reset all filters
    const resetFilters = () => {
      selectedCategory.value = "All";
      showLowStock.value = false;
      applyFilters();
    };

    // Fetch inventory when component mounts
    onMounted(() => {
      loadInventory();
    });

    const addNewInventory = () => {
      // Logic to add new inventory
    };

    const filterByStatus = (status: string) => {
      // Logic to filter by active/inactive status
      if (status === "active") {
        filteredInventory.value = inventory.value.filter(
          (item) => item.item_option.is_in_stock
        );
      } else if (status === "inactive") {
        filteredInventory.value = inventory.value.filter(
          (item) => !item.item_option.is_in_stock
        );
      } else {
        applyFilters();
      }
    };

    const onInventoryUpdate = (updatedInventory: Inventory) => {
      const index = inventory.value.findIndex(
        (inventory) => inventory.id === updatedInventory.id
      );
      if (index !== -1) {
        inventory.value[index] = updatedInventory;
      }
      applyFilters();
    };

    watch(selectedCategory, () => {
      applyFilters();
    });

    watch(showLowStock, () => {
      applyFilters();
    });

    return {
      categories,
      selectedCategory,
      showLowStock,
      totalProducts,
      activeProducts,
      inactiveProducts,
      filteredInventory,
      resetFilters,
      addNewInventory,
      sortByQuantity,
      filterByStatus,
      onInventoryUpdate,
    };
  },
});
</script>

<style scoped>
.text-white {
  color: white !important;
}

.bg-gray-800 {
  background-color: #212121 !important;
}

.pink--text {
  color: #ff7ca3 !important;
}
</style>
