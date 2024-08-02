<template>
  <div
    class="menu-nav-container flex flex-row items-start justify-center gap-8 max-w-full text-center text-bitter mq825:flex-wrap"
  >
    <div
      v-for="(item, index) in menuItems"
      :key="index"
      class="flex flex-row items-center justify-center"
    >
      <div>
        <p
          class="menu-item mx-8 my-0 relative tracking-tight leading-12 capitalize font-normal flex items-center justify-center cursor-pointer"
          @mouseover="hoverIndex = index"
          @mouseleave="hoverIndex = null"
          @click="clickedIndex = index"
          :class="{
            hovered: hoverIndex === index,
            clicked: clickedIndex === index,
          }"
        >
          {{ item }}
        </p>
        <img
          v-if="clickedIndex === index"
          class="w-[18px] h-[18px] relative object-cover"
          loading="lazy"
          alt=""
          src="/full-stop@2x.png"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "MenuNav",
  props: {
    menuItems: {
      type: Array as () => string[],
      required: true,
    },
  },
  data() {
    return {
      hoverIndex: null as number | null,
      clickedIndex: null as number | null,
    };
  },
});
</script>

<style scoped>
.menu-nav-container {
  color: var(--color-bitter); /* Custom Tailwind color */
  font-family: "Georgia", serif; /* Custom Tailwind font */
}

.menu-item {
  font-size: 3rem; /* Equivalent to text-29xl */
  color: inherit; /* Ensures it inherits the parent color */
  transition: color 0.3s;
}

.hovered {
  color: black; /* Replaces text-black when hovered */
}

.clicked {
  color: black; /* Replaces text-black when clicked */
}
</style>
