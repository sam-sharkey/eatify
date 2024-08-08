<template>
  <div
    class="max-w-full overflow-hidden flex flex-col items-start justify-start leading-[normal] tracking-[normal]"
  >
    <section
      class="self-stretch flex flex-col items-start justify-end py-10 px-9 box-border relative bg-[url('/public/picturecontainer@3x.png')] bg-cover bg-no-repeat bg-[top] min-h-[828px] text-left text-base text-springwood font-roboto-regular-155"
    >
      <div class="self-stretch flex flex-col items-start justify-start gap-5">
        <div class="self-stretch flex flex-col items-start justify-start">
          <div class="self-stretch relative leading-[16px] uppercase">
            Grass-fed, pasture-raised
          </div>
        </div>
        <div
          class="self-stretch flex flex-col items-start justify-start gap-3 text-56xl-6"
        >
          <div
            class="self-stretch relative leading-[68px] mq450:text-[45px] mq450:leading-[41px] mq750:text-[60px] mq750:leading-[54px]"
          >
            <p class="m-0">Introducing Caramelized</p>
            <p class="m-0">Garlic Steak at Sweetgreen</p>
          </div>
          <GenericButton text="ORDER NOW" />
        </div>
      </div>
      <div
        class="w-8 h-8 !m-[0] absolute top-[36px] right-[29px] rounded-981xl bg-razzmatazz flex flex-row items-center justify-center pt-2 px-[7px] pb-1.5 box-border z-[1]"
      >
        <img
          class="h-[18px] w-[18px] relative object-cover"
          loading="lazy"
          alt=""
          src="/right-arrow@2x.png"
        />
      </div>
      <div
        class="w-8 h-8 !m-[0] absolute top-[36px] right-[79px] rounded-981xl bg-razzmatazz flex flex-row items-center justify-center pt-2 px-[7px] pb-1.5 box-border z-[1]"
      >
        <img
          class="h-[18px] w-[18px] relative object-contain"
          loading="lazy"
          alt=""
          src="/right-arrow-1@2x.png"
        />
      </div>
    </section>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "../Common/GenericButton.vue";

export default defineComponent({
  name: "HighlightsWidget",
  components: { GenericButton },
});
</script>
