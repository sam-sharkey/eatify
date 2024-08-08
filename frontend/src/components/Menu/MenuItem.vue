<template>
  <div
    class="menu-item-container flex flex-col items-start justify-start gap-2 max-w-full text-left"
  >
    <div
      class="self-stretch max-h-[448px] aspect-square flex flex-col items-start justify-start pt-0 px-0 pb-4 box-border"
    >
      <img
        class="w-full aspect-square flex-1 relative rounded-xl max-w-[432px] overflow-hidden max-h-full object-cover mq450:max-w-full"
        loading="lazy"
        alt=""
        :src="imageSrc"
      />
    </div>
    <div
      class="self-stretch flex flex-col items-start justify-start pt-0 pb-1 pl-0 pr-4"
    >
      <h3
        class="menu-item-header m-0 relative tracking-[0.72px] leading-[29px] uppercase font-normal mq450:leading-[23px]"
      >
        {{ header }}
      </h3>
    </div>
    <div
      class="flex flex-col items-start justify-start pt-0 px-0 pb-2 text-mid-6"
    >
      <div class="relative leading-[24px]">
        <p class="m-0">{{ description }}</p>
      </div>
    </div>
    <GenericButton
      :Text="buttonText"
      propMinWidth="96px"
      rightArrow="/right-arrow4@2x.png"
      TextTextDecoration="unset"
      TextFontSize="16px"
      TextColor="#000"
      TextTextTransform="uppercase"
      rightArrowIconMinHeight="18px"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "../Common/GenericButton.vue";

export default defineComponent({
  name: "MenuItem",
  components: { GenericButton },
  props: {
    header: { type: String, default: "Buffalo Chicken" },
    imageSrc: {
      type: String,
      default: "/picture--sg-web-image-salad-buffalo-chickenpng2@2x.png",
    },
    description: {
      type: String,
      default:
        "Blackened chicken, pickled onions, tomatoes, raw carrots, cilantro, blue cheese, za’atar breadcrumbs, shredded kale, chopped romaine, sweetgreen hot sauce, caesar",
    },
    buttonText: { type: String, default: "Order Now" },
  },
});
</script>

<style scoped>
.menu-item-container {
  font-size: 1.5rem; /* Equivalent to text-5xl */
  color: var(--color-huntergreen); /* Custom Tailwind color */
  font-family: "Roboto", sans-serif; /* Custom Tailwind font */
}

.menu-item-header {
  font-size: 1.5rem;
  color: var(
    --color-huntergreen
  ); /* Ensure it inherits the color from container */
  font-family: "Roboto", sans-serif; /* Ensure it inherits the font from container */
}
</style>
