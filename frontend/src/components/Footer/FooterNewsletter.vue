<template>
  <div
    :class="['footer-newsletter-container']"
    :style="computedStyle"
    class="flex-[0.9809] overflow-hidden flex flex-col items-start justify-start pt-9 px-6 pb-[55.1px] box-border gap-4 min-w-[465px] max-w-full text-left text-base text-huntergreen font-roboto-regular-1575 mq750:min-w-full mq1150:flex-1"
  >
    <div class="self-stretch relative leading-[16px] uppercase shrink-0">
      Join Our Newsletter
    </div>
    <div
      class="self-stretch flex flex-row items-start justify-start max-w-full text-lgi-2"
    >
      <div
        class="flex-1 rounded-3xs border-huntergreen border-[1px] border-solid box-border flex flex-row items-start justify-between pt-2.5 px-4 pb-1.5 max-w-full gap-5"
      >
        <div class="relative inline-block min-w-[123px]">Email Address</div>
        <div
          class="h-[30px] w-6 rounded-tl-none rounded-tr-2xs rounded-br-2xs rounded-bl-none flex flex-col items-center justify-center py-0 px-0 box-border text-center text-5xl"
        >
          <h3
            class="m-0 self-stretch relative text-inherit leading-[53px] uppercase font-normal font-[inherit] mq450:text-lgi mq450:leading-[42px]"
          >
            →
          </h3>
        </div>
      </div>
    </div>
    <div
      class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-[0.9px] shrink-0 text-4xl-3"
    >
      <div
        class="self-stretch relative leading-[28.8px] mq450:text-lgi mq450:leading-[23px]"
      >
        Sign up for exclusive promos, new menu drops, store openings, and more.
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useStyleStore } from "../../stores/styleStore";

export default defineComponent({
  name: "FooterNewsletter",
  setup() {
    const styleStore = useStyleStore();

    const defaultStyles = `
      .footer-newsletter-container {
        background-color: var(--color-oldlace);
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
