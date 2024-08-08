<template>
  <div
    class="flex flex-row items-center justify-start gap-6 max-w-full text-left"
  >
    <template v-if="smallScreen">
      <GenericButton />
    </template>
    <template v-else>
      <a
        v-for="item in rightHeaderItems"
        :key="item.name"
        :href="item.path"
        class="header-link"
      >
        {{ item.name }}
      </a>
      <GenericButton />
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "../Common/GenericButton.vue";
import { HamburgerMenuItem } from "../types";

export default defineComponent({
  name: "HeaderRight",
  components: { GenericButton },
  props: {
    smallScreen: {
      type: Boolean,
      required: true,
    },
    rightHeaderItems: {
      type: Array as () => HamburgerMenuItem[],
      required: true,
    },
  },
});
</script>

<style scoped>
.header-link {
  text-decoration: none;
  text-transform: uppercase;
  color: var(--color-huntergreen); /* Use CSS variable for color */
  font-size: 1rem; /* Equivalent to text-base */
  font-family: "Roboto", sans-serif; /* Use custom font */
}
</style>
