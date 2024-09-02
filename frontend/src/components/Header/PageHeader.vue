<template>
  <div
    :class="['header-container']"
    :style="computedStyle"
    class="max-w-full flex flex-row items-center justify-between p-6 gap-6 mq1150:flex-wrap"
  >
    <HeaderLeft
      :smallScreen="smallScreen"
      :leftHeaderItems="formattedLeftHeaderItems"
      :rightHeaderItems="formattedRightHeaderItems"
    />
    <a href="/" class="header-link">
      {{ restaurantName }}
    </a>
    <!--img class="h-6" loading="lazy" alt="Logo" :src="restaurantLogo" /-->
    <HeaderRight
      :smallScreen="smallScreen"
      :rightHeaderItems="formattedRightHeaderItems"
    />
  </div>
</template>

<script lang="ts">
import {
  defineComponent,
  ref,
  onMounted,
  onUnmounted,
  computed,
  PropType,
} from "vue";
import HeaderLeft from "./HeaderLeft.vue";
import HeaderRight from "./HeaderRight.vue";
import { useStyleStore } from "../../stores/styleStore";
import { useRestaurantStore } from "../../stores/restaurant";

export default defineComponent({
  name: "PageHeader",
  components: { HeaderLeft, HeaderRight },
  props: {
    leftHeaderItems: {
      type: Array as PropType<string[]>,
      default: () => ["Locations", "Our Menu", "The Market"],
    },
    rightHeaderItems: {
      type: Array as PropType<string[]>,
      default: () => ["Outpost", "Our Mission", "Catering"],
    },
  },
  setup(props) {
    const smallScreen = ref(window.innerWidth < 1280);
    const styleStore = useStyleStore();
    const restaurantStore = useRestaurantStore();
    const restaurantLogo = restaurantStore.getRestaurant.logo_src;
    const restaurantName = restaurantStore.getRestaurant.name;

    const updateScreenSize = () => {
      smallScreen.value = window.innerWidth < 1280;
    };

    onMounted(() => {
      window.addEventListener("resize", updateScreenSize);
    });

    onUnmounted(() => {
      window.removeEventListener("resize", updateScreenSize);
    });

    const defaultStyles = `
      .header-container {
        background-color: var(--base-color);
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.innerHTML = defaultStyles + styleStore.headerCss;
      document.head.appendChild(styleElement);
      return "";
    });

    // Function to create paths from names
    const createPathFromName = (name: string): string => {
      const words = name.split(" ");
      return `/${words[words.length - 1].toLowerCase()}`;
    };

    const formattedLeftHeaderItems = computed(() =>
      props.leftHeaderItems.map((name) => ({
        name,
        path: createPathFromName(name),
      }))
    );

    const formattedRightHeaderItems = computed(() =>
      props.rightHeaderItems.map((name) => ({
        name,
        path: createPathFromName(name),
      }))
    );

    return {
      smallScreen,
      computedStyle,
      formattedLeftHeaderItems,
      formattedRightHeaderItems,
      restaurantLogo,
      restaurantName,
    };
  },
});
</script>

<style scoped>
.header-link {
  text-decoration: none;
  text-transform: uppercase;
  color: var(--dark-text-color); /* Use CSS variable for color */
  font-size: 1.5rem; /* Equivalent to text-base */
  font-family: "Roboto", sans-serif; /* Use custom font */
}
</style>
