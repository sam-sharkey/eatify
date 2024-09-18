<template>
  <section
    class="absolute top-[121px] left-[208px] flex flex-col items-start justify-start gap-[25px] max-w-full text-left text-6xl text-white font-poppins"
  >
    <div
      class="self-stretch flex flex-row items-center justify-start py-0 pl-0 pr-0.5 gap-[847px] mq1125:flex-wrap"
    >
      <a
        class="[text-decoration:none] relative font-medium text-[inherit] mq450:text-xl"
        >Categories</a
      >
      <button
        class="cursor-pointer [border:none] py-[14.1px] px-[22px] bg-pink-100 rounded-5xs-5 flex flex-row items-center justify-center hover:bg-pink-300"
      >
        <a
          class="[text-decoration:none] relative text-base font-medium font-poppins text-darkslategray-200 text-center"
          >Add New Category</a
        >
      </button>
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
        propWidth="63px"
        items="15 items"
        propMinWidth="63px"
        pizza="Burger"
        propMinWidth1="54px"
        group1000010171="/group-1000010172.svg"
      /><SpecialMenuItemPair
        propWidth="66px"
        items="10 items"
        propMinWidth="63px"
        pizza="Chicken"
        propMinWidth1="66px"
        group1000010171="/group-1000010174.svg"
      /><SpecialMenuItemPair
        propWidth="63px"
        items="18 items"
        propMinWidth="63px"
        pizza="Bakery"
        propMinWidth1="56px"
        group1000010171="/group-1000010173.svg"
      /><SpecialMenuItemPair
        propWidth="77px"
        items="12 items"
        propMinWidth="63px"
        pizza="Beverage"
        propMinWidth1="77px"
        group1000010171="/group-1000010175.svg"
      /><SpecialMenuItemPair
        propWidth="67px"
        items="16 items"
        propMinWidth="63px"
        pizza="Seafood"
        propMinWidth1="67px"
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
