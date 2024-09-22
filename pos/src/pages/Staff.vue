<template>
  <v-container fluid class="pt-1">
    <!-- Header with Add and Sort Buttons -->
    <v-row>
      <v-col>
        <h2 class="text-white">Staff ({{ totalStaff }})</h2>
      </v-col>
      <v-col class="text-right">
        <v-btn color="green" class="mx-2" @click="openAddStaffDialog"
          >Add Staff</v-btn
        >
        <v-btn color="green" outlined>Sort by</v-btn>
      </v-col>
    </v-row>

    <!-- Tabs for Staff Management and Attendance -->
    <v-tabs v-model="activeTab" class="text-white">
      <v-tab>Staff Management</v-tab>
      <v-tab>Attendance</v-tab>
    </v-tabs>

    <v-divider class="my-4"></v-divider>

    <!-- Staff Table -->
    <v-row>
      <v-col>
        <v-data-table
          :headers="headers"
          :items="staff"
          item-value="id"
          class="elevation-1 text-white bg-darkslategray-300"
        >
          <template v-slot:item.actions="{ item }">
            <v-btn icon @click="editStaff(item)">
              <v-icon color="green">mdi-pencil</v-icon>
            </v-btn>
            <v-btn icon @click="deleteStaff(item)">
              <v-icon color="red">mdi-delete</v-icon>
            </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>

    <!-- Add/Edit Staff Dialog -->
    <v-dialog v-model="showStaffDialog" max-width="500px">
      <v-card color="grey-darken-3">
        <v-card-title>
          <span class="headline">{{
            isEdit ? "Edit Staff" : "Add Staff"
          }}</span>
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="staffForm.name"
              label="Name"
              required
            ></v-text-field>
            <v-text-field
              v-model="staffForm.position"
              label="Position"
              required
            ></v-text-field>
            <v-text-field
              v-model="staffForm.email"
              label="Email"
              required
            ></v-text-field>
            <v-text-field
              v-model="staffForm.phone"
              label="Phone"
              required
            ></v-text-field>
            <v-text-field
              v-model="staffForm.age"
              label="Age"
              required
              type="number"
            ></v-text-field>
            <v-text-field
              v-model="staffForm.salary"
              label="Salary"
              required
              type="number"
            ></v-text-field>
            <v-text-field
              v-model="staffForm.timings"
              label="Timings"
              required
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn color="green" @click="saveStaff">Save</v-btn>
          <v-btn @click="showStaffDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import {
  fetchStaff,
  createStaff,
  updateStaff,
  deleteStaff,
} from "@eatify/shared/src/apiClient"; // Assuming you have the apiClient functions set up

export default defineComponent({
  setup() {
    const totalStaff = ref(0);
    const staff = ref([]);
    const showStaffDialog = ref(false);
    const isEdit = ref(false);
    const staffForm = ref({
      name: "",
      position: "",
      email: "",
      phone: "",
      age: 0,
      salary: 0,
      timings: "",
    });
    const activeTab = ref(0);
    const headers = ref([
      { text: "ID", value: "staff_id" },
      { text: "Name", value: "name" },
      { text: "Email", value: "email" },
      { text: "Phone", value: "phone" },
      { text: "Age", value: "age" },
      { text: "Salary", value: "salary" },
      { text: "Timings", value: "timings" },
      { text: "Actions", value: "actions", sortable: false },
    ]);

    const loadStaff = async () => {
      try {
        const data = await fetchStaff();
        staff.value = data;
        totalStaff.value = data.length;
      } catch (error) {
        console.error("Failed to fetch staff:", error);
      }
    };

    const openAddStaffDialog = () => {
      staffForm.value = {
        name: "",
        position: "",
        email: "",
        phone: "",
        age: 0,
        salary: 0,
        timings: "",
      };
      isEdit.value = false;
      showStaffDialog.value = true;
    };

    const editStaff = (item) => {
      staffForm.value = { ...item };
      isEdit.value = true;
      showStaffDialog.value = true;
    };

    const saveStaff = async () => {
      try {
        if (isEdit.value) {
          await updateStaff(staffForm.value);
        } else {
          await createStaff(staffForm.value);
        }
        showStaffDialog.value = false;
        loadStaff();
      } catch (error) {
        console.error("Failed to save staff:", error);
      }
    };

    const deleteStaff = async (item) => {
      try {
        await deleteStaff(item.id);
        loadStaff();
      } catch (error) {
        console.error("Failed to delete staff:", error);
      }
    };

    onMounted(() => {
      loadStaff();
    });

    return {
      totalStaff,
      staff,
      showStaffDialog,
      staffForm,
      isEdit,
      headers,
      activeTab,
      openAddStaffDialog,
      saveStaff,
      editStaff,
      deleteStaff,
    };
  },
});
</script>
