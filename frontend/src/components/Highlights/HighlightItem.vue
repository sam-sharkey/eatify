<!-- HighlightItem.vue -->
<template>
  <section
    class="self-stretch h-full flex flex-col items-start justify-end py-10 px-9 box-border relative bg-cover bg-no-repeat bg-top text-left text-base text-springwood font-roboto-regular-155"
    :style="{ backgroundImage: `url(${backgroundImage})` }"
  >
    <div class="self-stretch flex flex-col items-start justify-start gap-5">
      <div class="self-stretch flex flex-col items-start justify-start">
        <div class="self-stretch relative leading-[16px] uppercase">
          {{ body }}
        </div>
      </div>
      <div
        class="self-stretch flex flex-col items-start justify-start gap-3 text-56xl-6"
      >
        <div
          class="self-stretch relative leading-[68px] mq450:text-[45px] mq450:leading-[41px] mq750:text-[60px] mq750:leading-[54px]"
        >
          <p class="m-0">{{ headerLine }}</p>
        </div>
        <GenericButton text="ORDER NOW" />
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "../Common/GenericButton.vue";

export default defineComponent({
  name: "HighlightItem",
  components: { GenericButton },
  props: {
    headerLine: {
      type: String,
      required: true,
    },
    body: {
      type: String,
      required: true,
    },
    backgroundImage: {
      type: String,
      required: true,
    },
  },
});
</script>

<style scoped>
.highlight-item {
  position: relative;
  background-size: cover;
  background-position: center;
}
</style>
