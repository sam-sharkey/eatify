<template>
  <div
    class="relative p-[1.625rem] rounded-lg bg-antiquewhite flex flex-col items-start gap-[1rem] hover:bg-tasman"
  >
    <div
      v-if="item.tag"
      class="absolute top-2 left-2 bg-yellow m-2 py-1 px-2 rounded text-4 uppercase tracking-[1px]"
    >
      {{ item.tag }}
    </div>
    <img
      :src="item.image_src"
      :alt="item.name"
      class="w-full h-full object-cover rounded-lg"
    />
    <div class="w-full text-left text-[1.125rem]">
      <h3 class="leading-[1.5rem]">{{ item.name }}</h3>
      <p class="text-[0.931rem] leading-[1.375rem]">
        {{ item.description }}
      </p>
      <div
        class="mt-4 border border-darkslategray-100 py-[0.125rem] px-[0.5rem] rounded text-[0.669rem] uppercase tracking-[1px]"
      >
        ${{ item.price }} — {{ item.calories }} cal
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { MenuItem as MenuItemType } from "@eatify/shared/src/types";

export default defineComponent({
  name: "MenuItemComponent",
  props: {
    item: {
      type: Object as () => MenuItemType,
      required: true,
    },
  },
});
</script>
