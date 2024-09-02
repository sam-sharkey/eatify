<template>
  <div :class="['footer-container']" :style="computedStyle">
    <section class="flex flex-row items-start max-w-full mq1150:flex-wrap">
      <FooterNewsletter />
      <FooterAppDownload />
    </section>
    <FooterLinks />
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import FooterNewsletter from "./FooterNewsletter.vue";
import FooterAppDownload from "./FooterAppDownload.vue";
import FooterLinks from "./FooterLinks.vue";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "PageFooter",
  components: { FooterNewsletter, FooterAppDownload, FooterLinks },
  setup() {
    const defaultStyles = `
      .footer-container {
        background-color: var(--base-color);
      }
    `;
    const styleStore = useStyleStore();

    const computedStyle = computed(() => {
      const styleElement = document.createElement("style");
      styleElement.type = "text/css";
      styleElement.innerHTML = defaultStyles + styleStore.footerCss;
      document.head.appendChild(styleElement);
      return "";
    });

    return {
      computedStyle,
    };
  },
});
</script>
