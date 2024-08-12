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
    <img class="h-6" loading="lazy" alt="Logo" src="/logo.svg" />
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
    customCss: {
      type: String,
      default: "",
    },
  },
  setup(props) {
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

    const defaultStyles = `
      .header-container {
        background-color: var(--color-springwood);
      }
    `;

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.innerHTML = defaultStyles + props.customCss;
      console.log(defaultStyles + props.customCss);
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
    };
  },
});
</script>
