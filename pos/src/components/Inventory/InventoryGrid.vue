<template>
  <v-container class="pt-1" fluid>
    <!-- Table Header -->
    <v-row class="bg-gray-800 text-white align-center">
      <v-col cols="1">
        <v-checkbox hide-details class="text-white" />
      </v-col>
      <v-col cols="1" class="text-base text-white"> Product </v-col>
      <v-col cols="2" class="font-medium"> Product Name </v-col>
      <v-col cols="1" class="font-medium"> Quantity </v-col>
      <v-col cols="1" class="font-medium text-left"> Low Alert </v-col>
      <v-col cols="1" class="font-medium text-left"> Category </v-col>
      <v-col cols="1" class="font-medium text-left"> Price </v-col>
      <v-col cols="2" class="font-medium text-left"> Availability </v-col>
      <v-col cols="2" class="font-medium text-left"> Actions </v-col>
    </v-row>

    <!-- Table Rows -->
    <v-divider class="mb-3"></v-divider>
    <v-row
      v-for="(inventory, index) in inventoryItems"
      :key="index"
      :class="index % 2 === 0 ? 'bg-darkslategray-300' : 'bg-darkslategray-400'"
      class="align-center text-white"
    >
      <v-col cols="1">
        <v-checkbox hide-details />
      </v-col>
      <v-col cols="1">
        <v-img
          :src="getImageUrl(inventory.item_option.image_src)"
          alt="menu icon"
          width="40"
          height="40"
        ></v-img>
      </v-col>
      <v-col cols="2">{{ inventory.item_option.name }}</v-col>
      <v-col cols="1">{{ inventory.quantity }}</v-col>
      <v-col cols="1" class="text-left">{{
        inventory.low_quantity_threshold
      }}</v-col>
      <v-col cols="1" class="text-left">{{
        inventory.item_option.classification
      }}</v-col>
      <v-col cols="1" class="text-left"
        >${{ inventory.item_option.cost }}</v-col
      >
      <v-col cols="2" class="text-left">
        {{ inventory.item_option.is_in_stock ? "Available" : "Out of Stock" }}
      </v-col>
      <v-col cols="2" class="text-left">
        <v-btn color="primary" @click="openUpdateDialog(inventory)"
          >Update</v-btn
        >
      </v-col>
    </v-row>

    <!-- Update Inventory Dialog -->
    <v-dialog
      v-model="showUpdateDialog"
      color="grey-darken-3"
      max-width="500px"
    >
      <v-card color="grey-darken-3">
        <v-card-title class="headline">Update Inventory</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Quantity"
              v-model="selectedInventory.quantity"
              type="number"
              required
            ></v-text-field>

            <v-text-field
              label="Low Quantity Threshold"
              v-model="selectedInventory.low_quantity_threshold"
              type="number"
              required
            ></v-text-field>
            <v-select
              v-model="selectedInventory.item_option.is_in_stock"
              :items="['Available', 'Out of Stock']"
              label="Availability"
            ></v-select>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn color="green" @click="saveInventory">Save</v-btn>
          <v-btn color="red" @click="showUpdateDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { Inventory } from "@eatify/shared/src/types"; // Assuming types are defined
import { updateInventory } from "@eatify/shared/src/apiClient";

export default defineComponent({
  name: "InventoryGrid",
  props: {
    inventoryItems: {
      type: Array as () => Inventory[],
      required: true,
    },
  },
  setup(_, { emit }) {
    const showUpdateDialog = ref(false);
    const selectedInventory = ref<Inventory | null>(null);

    // Function to open the update dialog
    const openUpdateDialog = (inventory: Inventory) => {
      selectedInventory.value = { ...inventory }; // Clone the inventory item for editing
      showUpdateDialog.value = true;
    };

    // Function to save the updated inventory
    const saveInventory = async () => {
      if (!selectedInventory.value) return;

      try {
        // Assuming you have an API function to update the inventory
        const response = await updateInventory(selectedInventory.value);
        emit("inventory-updated", response);
        showUpdateDialog.value = false;
      } catch (error) {
        console.error("Failed to update inventory", error);
      }
    };

    const getImageUrl = (url: string) => {
      if (url.startsWith("http")) {
        return url;
      } else {
        return "http://localhost:8000".concat(url);
      }
    };

    return {
      showUpdateDialog,
      selectedInventory,
      openUpdateDialog,
      saveInventory,
      getImageUrl,
    };
  },
});
</script>
