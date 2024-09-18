<template>
  <div
    class="w-full h-[1165px] relative bg-gray overflow-hidden leading-[normal] tracking-[normal] text-left text-6xl text-white font-poppins mq1125:h-auto mq1125:min-h-[1165]"
  >
    <div class="absolute top-[43px] left-[208px] w-[116.8px] h-[38px]">
      <a
        class="[text-decoration:none] absolute top-[0px] left-[46.8px] font-medium text-[inherit] inline-block min-w-[70px] mq450:text-xl"
        >Menu</a
      >
      <img
        class="absolute top-[1px] left-[0px] w-[35.7px] h-[35.7px] object-contain"
        loading="lazy"
        alt=""
        src="/group-1000010089@2x.png"
      />
    </div>
    <div
      class="absolute h-[3.18%] w-[6.81%] top-[3.51%] right-[3.47%] bottom-[93.3%] left-[89.72%] text-center text-[5.9px] text-darkslategray-200"
    >
      <div
        class="absolute h-[53.64%] w-[16.62%] top-[23.99%] right-[83.38%] bottom-[22.37%] left-[0%]"
      >
        <img
          class="absolute h-[78.39%] w-[90.18%] top-[22.11%] right-[9.82%] bottom-[-0.5%] left-[0%] max-w-full overflow-hidden max-h-full"
          alt=""
          src="/vector.svg"
        />
        <div
          class="absolute h-[52.26%] w-[63.8%] top-[0%] right-[0%] bottom-[47.74%] left-[36.2%]"
        >
          <div
            class="absolute h-full w-full top-[0%] right-[0%] bottom-[0%] left-[0%] rounded-[50%] bg-pink-100"
          />
          <div
            class="absolute top-[0.8px] left-[calc(50%_-_2.9px)] inline-block min-w-[6px]"
          >
            01
          </div>
        </div>
      </div>
      <img
        class="absolute top-[7.4px] left-[38.6px] w-[0.7px] h-[22.3px]"
        alt=""
        src="/vector-139.svg"
      />
      <img
        class="absolute top-[0px] left-[60.9px] rounded-[50%] w-[37.1px] h-[37.1px] object-cover"
        loading="lazy"
        alt=""
        src="/ellipse-1@2x.png"
      />
    </div>
    <RightSidebar />
    <h2
      class="m-0 absolute top-[411.3px] left-[215px] text-inherit font-medium font-[inherit] mq450:text-xl"
    >
      Special menu all items
    </h2>
    <GroupComponent1 />
    <section
      class="absolute top-[475px] left-[171px] flex flex-col items-center justify-start gap-[25px] max-w-full"
    >
      <FrameComponent /><ProductTable />
    </section>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import RightSidebar from "../components/RightSidebar.vue";
  import GroupComponent1 from "../components/GroupComponent1.vue";
  import FrameComponent from "../components/FrameComponent.vue";
  import ProductTable from "../components/ProductTable.vue";

  export default defineComponent({
    name: "Menu",
    components: { RightSidebar, GroupComponent1, FrameComponent, ProductTable },
  });
</script>
