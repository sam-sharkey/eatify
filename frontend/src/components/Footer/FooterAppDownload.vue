<template>
  <div
    :class="['footer-appdownload-container']"
    :style="computedStyle"
    class="flex-1 border-huntergreen border-l-[1px] border-solid flex flex-col pt-9 px-[17px] relative gap-2 max-w-full text-left text-base-9 text-huntergreen font-roboto-regular-1575 mq1150:flex-1"
  >
    <div
      class="self-stretch flex flex-row items-start justify-start py-0 pl-0 pr-px box-border max-w-full shrink-0"
    >
      <div
        class="flex-1 relative leading-[16px] uppercase inline-block max-w-full"
      >
        Download the app
      </div>
    </div>
    <div
      class="self-stretch flex flex-col items-start justify-center py-0 pl-0 pr-px gap-6 text-center text-5xl"
    >
      <div
        class="self-stretch overflow-hidden flex flex-row items-center justify-between py-0 pl-0 gap-5 mq750:flex-wrap mq750:box-border mq450:pr-5 mq450:box-border"
      >
        <GenericButton
          Text="iOS"
          propMinWidth="37px"
          rightArrow="/right-arrow@2x.png"
        />
        <div class="flex flex-col items-start justify-start">
          <img
            class="w-[42.3px] h-[42.1px] relative overflow-hidden shrink-0 object-cover max-w-[42.3px]"
            loading="lazy"
            alt=""
            src="/pickup1png@2x.png"
          />
        </div>
      </div>
      <div
        class="self-stretch overflow-hidden flex flex-row items-center justify-between py-0 pl-0 gap-5 mq750:flex-wrap mq750:justify-center mq750:box-border mq450:pr-5 mq450:box-border"
      >
        <GenericButton Text="Android" rightArrow="/right-arrow1@2x.png" />
        <div class="flex flex-col items-start justify-start">
          <img
            class="w-[42.3px] h-[42.1px] relative overflow-hidden shrink-0 object-cover max-w-[42.3px]"
            loading="lazy"
            alt=""
            src="/pickup1png1@2x.png"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent, computed } from "vue";
import GenericButton from "../Common/GenericButton.vue";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "FooterAppDownload",
  components: { GenericButton },
  setup() {
    const styleStore = useStyleStore();

    const defaultStyles = `
      .footer-appdownload-container {
        background-color: var(--base-color);
      }
    `;

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
