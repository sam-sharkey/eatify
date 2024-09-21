<template>
  <div
    class="flex flex-row items-start justify-start gap-6 max-w-full text-left"
  >
    <HamburgerMenu v-if="smallScreen" :menuItems="combinedMenuItems" />
    <template v-else>
      <a
        v-for="item in leftHeaderItems"
        :key="item.name"
        :href="item.path"
        class="header-link"
      >
        {{ item.name }}
      </a>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import HamburgerMenu from "./HamburgerMenu.vue";
import { HamburgerMenuItem } from "@eatify/shared/src/types";

export default defineComponent({
  name: "HeaderLeft",
  components: { HamburgerMenu },
  props: {
    smallScreen: {
      type: Boolean,
      required: true,
    },
    leftHeaderItems: {
      type: Array as () => HamburgerMenuItem[],
      required: true,
    },
    rightHeaderItems: {
      type: Array as () => HamburgerMenuItem[],
      required: true,
    },
  },
  setup(props) {
    const combinedMenuItems = computed(() => [
      ...props.leftHeaderItems,
      ...props.rightHeaderItems,
    ]);

    return {
      combinedMenuItems,
    };
  },
});
</script>

<style scoped>
.header-link {
  text-decoration: none;
  text-transform: uppercase;
  color: var(--dark-text-color); /* Use CSS variable for color */
  font-size: 1rem; /* Equivalent to text-base */
  font-family: "Roboto", sans-serif; /* Use custom font */
}
</style>
