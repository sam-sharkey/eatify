<template>
  <section
    class="w-[86.5rem] flex flex-row items-start justify-start py-[0rem] px-[0.75rem] box-border max-w-full text-left text-[1.744rem] text-gray-100 font-inter"
  >
    <div
      class="flex-1 flex flex-col items-start justify-start gap-[1rem] max-w-full"
    >
      <div
        class="self-stretch relative tracking-[1px] leading-[2.25rem] mq450:text-[1.375rem] mq450:leading-[1.813rem]"
      >
        Protein Platess
      </div>
      <div
        class="w-[41.75rem] flex flex-row items-start justify-start flex-wrap content-start gap-[1.5rem] max-w-full text-center text-[0.594rem]"
      >
        <ButtonCaramelizedGarlicSt
          propWidth="unset"
          propMinWidth="18.125rem"
          propFlex="1"
          propWidth1="unset"
          propAlignSelf="unset"
          propAlignSelf1="unset"
          new1="HIGH PROTEIN"
          propMinWidth1="5rem"
          container="/container-4@2x.png"
          caramelizedGarlicSteak="Hot Honey Chicken"
          wildRiceSpicyBroccoliTomatoes="Herbed quinoa, crispy onions, "
          warmRoastedSweetPotatoes="blackened chicken, warm roasted "
          caramelizedGarlicSteakPesto="sweet potatoes, veg slaw, hot honey "
          vinaigrette="mustard sauce"
          cal="$15.45 — 835 cal"
          propMinWidth2="7rem"
        />
        <div
          class="flex-1 rounded-lg bg-antiquewhite flex flex-col items-start justify-start p-[1.625rem] box-border gap-[1rem] min-w-[18.125rem] max-w-full mq800:pt-[1.25rem] mq800:pb-[1.25rem] mq800:box-border"
        >
          <div
            class="self-stretch flex flex-row items-start justify-start pt-[0rem] px-[0rem] pb-[15.625rem] relative"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="rounded bg-yellow flex flex-col items-center justify-center py-[0.218rem] px-[0.437rem]"
              >
                <div
                  class="flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
                >
                  <div
                    class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[5rem]"
                  >
                    HIGH PROTEIN
                  </div>
                </div>
              </div>
            </div>
            <img
              class="h-full w-full absolute !m-[0] top-[0rem] right-[0rem] bottom-[0rem] left-[0rem] max-w-full overflow-hidden max-h-full object-cover z-[1]"
              alt=""
              src="/container-5@2x.png"
            />
          </div>
          <div
            class="self-stretch flex flex-col items-start justify-start gap-[0.5rem] text-left text-[1.125rem]"
          >
            <div class="relative leading-[1.5rem]">Miso Glazed Salmon</div>
            <div
              class="self-stretch flex flex-col items-start justify-start text-[0.913rem]"
            >
              <div class="relative leading-[1.375rem]">
                <p class="m-0">White rice, cucumbers, nori sesame</p>
                <p class="m-0">seasoning, crispy onions, pickled</p>
                <p class="m-0">onions, avocado, miso glazed salmon,</p>
                <p class="m-0">spicy cashew</p>
              </div>
              <div
                class="self-stretch flex flex-row items-start justify-start pt-[1rem] px-[0rem] pb-[0rem] text-center text-[0.694rem]"
              >
                <div class="flex flex-col items-start justify-start">
                  <div
                    class="rounded border-darkslategray-100 border-[1px] border-solid flex flex-col items-center justify-center py-[0.125rem] px-[0.5rem]"
                  >
                    <div
                      class="flex flex-col items-center justify-start pt-[0.062rem] px-[0rem] pb-[0rem]"
                    >
                      <div
                        class="relative tracking-[1px] leading-[1rem] uppercase inline-block min-w-[7.125rem]"
                      >
                        $16.95 — 930 cal
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ButtonCaramelizedGarlicSt from "./ButtonCaramelizedGarlicSt.vue";

export default defineComponent({
  name: "FrameComponent1",
  components: { ButtonCaramelizedGarlicSt },
});
</script>
