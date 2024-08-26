<template>
  <div
    class="w-full relative bg-oldlace flex flex-col items-start justify-start leading-[normal] tracking-[normal] text-left text-[0.994rem] text-gray-200 font-inter"
  >
    <NavigationNavigationBarFo /><RestaurantInfo />
    <div
      class="self-stretch border-gray-300 border-b-[1px] border-solid box-border flex flex-row items-start justify-center py-[0rem] px-[1.25rem] max-w-full"
    >
      <div
        class="flex flex-row items-start justify-center max-w-full [row-gap:20px] mq1150:flex-wrap"
      >
        <div class="flex flex-row items-start justify-start">
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[4.188rem]"
              >
                Featured
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[6.563rem]"
              >
                Protein Plates
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-start py-[0rem] pl-[2.437rem] pr-[0rem] text-[0.981rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[2.813rem]"
              >
                Bowls
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[3.188rem]"
              >
                Salads
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem] text-[1.013rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[3.75rem]"
              >
                Custom
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-start py-[0rem] pl-[2.437rem] pr-[0rem] text-[0.944rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[5.188rem]"
              >
                Kid's Meals
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem] text-[1.006rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[2.625rem]"
              >
                Sides
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem]"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[3.688rem]"
              >
                Dessert
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex flex-row items-start justify-end py-[0rem] pl-[2.5rem] pr-[0rem] text-[0.981rem] text-darkslategray-200"
        >
          <div
            class="flex flex-col items-start justify-start py-[0.75rem] px-[0rem]"
          >
            <div class="flex flex-col items-start justify-start">
              <div
                class="relative leading-[1.375rem] inline-block min-w-[4.938rem]"
              >
                Beverages
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <main
      class="w-full flex flex-col items-start justify-start pt-[4rem] pb-[0rem] pl-[1.75rem] pr-[1rem] box-border gap-[4rem] max-w-[95rem] mq450:gap-[1rem] mq800:gap-[2rem] mq1350:pt-[1.25rem] mq1350:box-border"
    >
      <FrameComponent /><FrameComponent1 /><FrameComponent2 /><MenuListComponent /><CustomSaladsParent /><FrameComponent3 /><BeverageContainer />
    </main>
    <FooterWidget />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import NavigationNavigationBarFo from "./NavigationNavigationBarFo.vue";
import RestaurantInfo from "./RestaurantInfo.vue";
import FrameComponent from "./FrameComponent.vue";
import FrameComponent1 from "./FrameComponent1.vue";
import FrameComponent2 from "./FrameComponent2.vue";
import MenuListComponent from "./MenuListComponent.vue";
import CustomSaladsParent from "./CustomSaladsParent.vue";
import FrameComponent3 from "./FrameComponent3.vue";
import BeverageContainer from "./BeverageContainer.vue";
import FooterWidget from "./FooterWidget.vue";

export default defineComponent({
  name: "OrderMenuPage",
  components: {
    NavigationNavigationBarFo,
    RestaurantInfo,
    FrameComponent,
    FrameComponent1,
    FrameComponent2,
    MenuListComponent,
    CustomSaladsParent,
    FrameComponent3,
    BeverageContainer,
    FooterWidget,
  },
});
</script>
