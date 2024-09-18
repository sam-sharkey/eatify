<template>
  <section
    class="absolute top-[111px] left-[25px] flex flex-col items-start justify-start gap-[25px] w-full text-left text-6xl text-white font-poppins"
  >
    <div
      class="self-stretch flex flex-row items-center justify-start py-0 pl-0 pr-0.5 mq1125:flex-wrap"
    >
      <a
        class="[text-decoration:none] relative font-medium text-[inherit] mq450:text-xl"
        >Categories</a
      >
    </div>
    <nav
      class="m-0 self-stretch flex flex-row items-start justify-start flex-wrap content-start gap-5 text-left text-base text-darkslategray-200 font-poppins"
    >
      <div
        class="h-[146px] flex-1 relative rounded-3xs bg-pink-100 max-w-[152px]"
      >
        <div
          class="absolute bottom-[15px] left-[15px] font-light inline-block min-w-[68px]"
        >
          116 items
        </div>
        <div
          class="absolute top-[83px] left-[15px] font-medium inline-block min-w-[20px]"
        >
          All
        </div>
        <img
          class="absolute top-[15px] right-[15px] w-10 h-10 overflow-hidden"
          alt=""
          src="/magedashboardfill.svg"
        />
      </div>
      <SpecialMenuItemPair
        items="20 items"
        pizza="Pizza"
        group1000010171="/group-1000010171.svg"
      /><SpecialMenuItemPair
        items="15 items"
        pizza="Burger"
        group1000010171="/group-1000010172.svg"
      /><SpecialMenuItemPair
        items="10 items"
        pizza="Chicken"
        group1000010171="/group-1000010174.svg"
      /><SpecialMenuItemPair
        items="18 items"
        pizza="Bakery"
        group1000010171="/group-1000010173.svg"
      /><SpecialMenuItemPair
        items="12 items"
        pizza="Beverage"
        group1000010171="/group-1000010175.svg"
      /><SpecialMenuItemPair
        items="16 items"
        pizza="Seafood"
        group1000010171="/group-1000010176.svg"
      />
    </nav>
  </section>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import SpecialMenuItemPair from "./SpecialMenuItemPair.vue";

export default defineComponent({
  name: "RightSidebar",
  components: { SpecialMenuItemPair },
});
</script>
