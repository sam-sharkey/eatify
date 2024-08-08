<template>
  <div
    class="header-container max-w-full flex flex-row items-center justify-between p-6 gap-6 mq1150:flex-wrap"
  >
    <HeaderLeft
      :smallScreen="smallScreen"
      :leftHeaderItems="leftHeaderItems"
      :rightHeaderItems="rightHeaderItems"
    />
    <img class="h-6" loading="lazy" alt="Logo" src="/logo.svg" />
    <HeaderRight
      :smallScreen="smallScreen"
      :rightHeaderItems="rightHeaderItems"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from "vue";
import HeaderLeft from "./HeaderLeft.vue";
import HeaderRight from "./HeaderRight.vue";

export default defineComponent({
  name: "PageHeader",
  components: { HeaderLeft, HeaderRight },
  setup() {
    const smallScreen = ref(window.innerWidth < 1280);

    const updateScreenSize = () => {
      smallScreen.value = window.innerWidth < 1280;
    };

    onMounted(() => {
      window.addEventListener("resize", updateScreenSize);
    });

    onUnmounted(() => {
      window.removeEventListener("resize", updateScreenSize);
    });

    return {
      smallScreen,
    };
  },
  data() {
    return {
      leftHeaderItems: [
        { name: "locations", path: "/locations" },
        { name: "Our Menu", path: "/menu" },
        { name: "The Market", path: "/market" },
      ],
      rightHeaderItems: [
        { name: "Outpost", path: "/outpost" },
        { name: "Our Mission", path: "/mission" },
        { name: "Catering", path: "/catering" },
      ],
    };
  },
});
</script>

<style scoped>
.header-container {
  background-color: var(--color-springwood); /* Extracted background color */
}
</style>
