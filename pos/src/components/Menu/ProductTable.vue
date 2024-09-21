<template>
  <v-container class="pt-10" fluid>
    <!-- Table Header -->
    <v-row class="bg-gray-800 text-white align-center">
      <v-col cols="1">
        <v-checkbox hide-details class="white--text" />
      </v-col>
      <v-col cols="1" class="text-base white--text"> Product </v-col>
      <v-col cols="2" class="font-medium"> Product Name </v-col>
      <v-col cols="1" class="font-medium"> Item ID </v-col>
      <v-col cols="1" class="font-medium"> Stock </v-col>
      <v-col cols="1" class="font-medium text-left"> Category </v-col>
      <v-col cols="1" class="font-medium text-left"> Price </v-col>
      <v-col cols="2" class="font-medium text-left"> Availability </v-col>
    </v-row>

    <!-- Table Rows -->
    <v-divider class="mb-3"></v-divider>
    <v-row
      v-for="(item, index) in categoryItems"
      :key="index"
      :class="index % 2 === 0 ? 'bg-darkslategray-300' : 'bg-darkslategray-400'"
      class="align-center"
    >
      <v-col cols="1">
        <v-checkbox hide-details />
      </v-col>
      <v-col cols="1">
        <v-img
          :src="item.image_src"
          alt="menu icon"
          width="40"
          height="40"
        ></v-img>
      </v-col>
      <v-col cols="2">{{ item.name }}</v-col>
      <v-col cols="1">{{ item.id }}</v-col>
      <v-col cols="1">{{ item.stock || "N/A" }}</v-col>
      <v-col cols="1" class="text-left">{{ item.classification }}</v-col>
      <v-col cols="1" class="text-left">${{ item.price }}</v-col>
      <v-col cols="2" class="text-left">
        {{ item.is_in_stock ? "Available" : "Out of Stock" }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "ProductTable",
  props: {
    categoryItems: {
      type: Array as PropType<
        Array<{
          name: string;
          id: number;
          classification: string;
          stock: number;
          price: number;
          is_in_stock: boolean;
          image_src: string;
        }>
      >,
      required: true,
    },
  },
});
</script>

<style scoped>
/* Add any scoped styles here, if necessary */
</style>
