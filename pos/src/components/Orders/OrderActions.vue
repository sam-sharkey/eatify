<template>
  <v-container>
    <!-- Subtotal and Buttons -->
    <div class="w-full flex flex-col gap-6 relative z-10">
      <div class="flex justify-between">
        <div class="font-light">SubTotal</div>
        <div class="font-light">${{ order.total_cost }}</div>
      </div>
      <div class="flex gap-4">
        <!-- Edit Button -->
        <v-btn
          color="darkslategray"
          class="flex-1"
          @click="showEditDialog = true"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>

        <!-- Delete Button -->
        <v-btn
          color="darkslategray"
          class="flex-1"
          @click="showDeleteDialog = true"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>

        <!-- Pay Bill Button -->
        <v-btn color="green" class="flex-1 text-white font-medium">
          Pay Bill
        </v-btn>
      </div>
    </div>

    <!-- Edit Dialog -->
    <v-dialog v-model="showEditDialog" max-width="500px">
      <v-card color="grey-darken-3">
        <v-card-title>Edit Order</v-card-title>
        <v-card-text>
          <!-- Edit form to update all order fields -->
          <v-form>
            <!-- Delivery Type -->
            <v-select
              v-model="editedOrder.delivery_type"
              :items="['pickup', 'delivery']"
              label="Delivery Type"
              required
            ></v-select>

            <!-- Store Location -->
            <v-text-field
              v-model="editedOrder.store_location"
              label="Store Location"
              required
            ></v-text-field>

            <!-- User Address -->
            <v-text-field
              v-model="editedOrder.user_address"
              label="User Address"
              required
            ></v-text-field>

            <!-- Total Cost -->
            <v-text-field
              v-model="editedOrder.total_cost"
              label="Total Cost"
              type="number"
              required
            ></v-text-field>

            <!-- Order Time -->
            <v-text-field
              v-model="editedOrder.order_time"
              label="Order Time"
              type="datetime-local"
              required
            ></v-text-field>

            <!-- Status -->
            <v-select
              v-model="editedOrder.status"
              :items="['not_started', 'in_progress', 'ready', 'delivered']"
              label="Status"
              required
            ></v-select>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn color="green" @click="saveOrder">Save</v-btn>
          <v-btn text @click="showEditDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Delete Confirmation Dialog -->
    <v-dialog v-model="showDeleteDialog" max-width="500px">
      <v-card color="grey-darken-3">
        <v-card-title>Confirm Delete</v-card-title>
        <v-card-text> Are you sure you want to delete this order? </v-card-text>
        <v-card-actions>
          <v-btn color="red" @click="deleteOrderOnClick">Delete</v-btn>
          <v-btn text @click="showDeleteDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { editOrder, deleteOrder } from "@eatify/shared/src/apiClient";
import Order from "@eatify/shared/src/types";

export default defineComponent({
  name: "OrderActions",
  props: {
    order: {
      type: Object as () => Order,
      required: true,
    },
  },
  setup(props, { emit }) {
    const showEditDialog = ref(false);
    const showDeleteDialog = ref(false);

    // Create a deep copy of the order to allow editing without modifying the original until saved
    const editedOrder = ref<Order>({ ...props.order });

    // Method to save the edited order
    const saveOrder = async () => {
      try {
        // Send the updated order to the backend
        const response = await editOrder(props.order.id, editedOrder.value);

        // Emit the udpated order to the parent component
        emit("order-updated", response);

        // Close the dialog after saving
        showEditDialog.value = false;
      } catch (error) {
        console.error("Error updating order:", error);
      }
    };

    // Method to delete the order
    const deleteOrderOnClick = async () => {
      try {
        // Send delete request to the backend
        await deleteOrder(props.order.id);

        // Emit an event to notify the parent that the order was deleted
        emit("order-deleted", props.order.id);

        // Close the dialog after deleting
        showDeleteDialog.value = false;
      } catch (error) {
        console.error("Error deleting order:", error);
      }
    };

    return {
      deleteOrderOnClick,
      showEditDialog,
      showDeleteDialog,
      editedOrder,
      saveOrder,
      deleteOrder,
    };
  },
});
</script>

<style scoped>
.v-btn {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
