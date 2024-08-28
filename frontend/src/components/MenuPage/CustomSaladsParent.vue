<template>
  <section
    class="self-stretch flex flex-row items-start justify-start py-[0rem] pl-[0.75rem] pr-[0rem] box-border max-w-full text-left text-[3.75rem] text-white font-inter"
  >
    <div class="flex-1 flex flex-col items-start justify-start max-w-full">
      <div
        class="self-stretch flex flex-row items-start justify-start flex-wrap content-start py-[0rem] px-[0.75rem] box-border max-w-full"
      >
        <div
          class="h-[27rem] flex-1 rounded-2xl bg-darkslategray-200 overflow-hidden flex flex-row items-start justify-start relative min-h-[27rem] max-w-full"
        >
          <div
            class="w-full !m-[0] absolute h-full top-[0rem] right-[0rem] bottom-[0rem] left-[0rem] flex flex-row items-start justify-start py-[5.125rem] px-[0rem] box-border max-w-full"
          >
            <div
              class="h-full w-full absolute !m-[0] top-[0rem] right-[0rem] bottom-[0rem] left-[0rem]"
            >
              <img
                class="absolute top-[0rem] left-[0rem] w-full h-full overflow-hidden object-cover"
                alt=""
                src="/create-your-own@2x.png"
              />
              <div
                class="w-full h-full absolute top-[0rem] left-[0rem] bg-gray-400"
              />
            </div>
            <div
              class="flex-1 flex flex-row items-center justify-center max-w-full z-[2]"
            >
              <div
                class="flex-1 flex flex-col items-start justify-start py-[2.5rem] pl-[7.5rem] pr-[33.562rem] box-border max-w-full mq450:pr-[1.25rem] mq450:box-border mq800:pl-[1.875rem] mq800:pr-[8.375rem] mq800:box-border mq1350:pl-[3.75rem] mq1350:pr-[16.75rem] mq1350:box-border"
              >
                <div
                  class="flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1.5rem] box-border max-w-full"
                >
                  <h1
                    class="m-0 relative text-inherit tracking-[-3px] leading-[4rem] font-normal font-[inherit] mq450:text-[2.25rem] mq450:leading-[2.375rem] mq800:text-[3rem] mq800:leading-[3.188rem]"
                  >
                    Create Your Own
                  </h1>
                </div>
                <div
                  class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1.5rem] text-[1.363rem]"
                >
                  <div
                    class="relative leading-[1.75rem] mq450:text-[1.063rem] mq450:leading-[1.375rem]"
                  >
                    Be your own chef and build your perfect salad, bowl or
                    protein plate.
                  </div>
                </div>
                <button
                  class="cursor-pointer [border:none] p-0 bg-[transparent] w-[10rem] flex flex-col items-start justify-start"
                >
                  <div
                    class="self-stretch rounded-81xl bg-white flex flex-row items-center justify-center py-[0.75rem] px-[1.5rem]"
                  >
                    <div
                      class="flex-1 flex flex-col items-center justify-start"
                    >
                      <div
                        class="self-stretch relative text-[0.956rem] leading-[1.375rem] font-inter text-gray-100 text-center inline-block min-w-[5.25rem] whitespace-nowrap"
                      >
                        Get Started
                      </div>
                    </div>
                    <div
                      class="flex flex-col items-start justify-start py-[0rem] pl-[0.25rem] pr-[0rem]"
                    >
                      <div class="flex flex-row items-center justify-center">
                        <img
                          class="h-[1.5rem] w-[1.5rem] relative"
                          alt=""
                          src="/svg-3.svg"
                        />
                      </div>
                    </div>
                  </div>
                </button>
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

export default defineComponent({
  name: "CustomSaladsParent",
});
</script>
