<template>
  <footer
    class="self-stretch bg-gainsboro flex flex-row items-start justify-start py-[2.5rem] px-[0rem] box-border max-w-full text-left text-[0.938rem] text-gray-100 font-inter"
  >
    <div
      class="flex-1 flex flex-row items-start justify-start py-[0rem] px-[1.75rem] box-border max-w-[95rem] [row-gap:20px] mq1350:flex-wrap"
    >
      <div
        class="w-[14.419rem] flex flex-col items-start justify-start pt-[0rem] px-[0.75rem] pb-[1.375rem] box-border text-[0.963rem]"
      >
        <div
          class="self-stretch flex flex-col items-start justify-start py-[0rem] px-[0rem]"
        >
          <div
            class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1rem]"
          >
            <div class="self-stretch flex flex-col items-start justify-start">
              <div class="self-stretch relative leading-[1.375rem] uppercase">
                Support + Services
              </div>
            </div>
          </div>
          <div
            class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.913rem]"
          >
            <div
              class="flex flex-col items-start justify-start cursor-pointer"
              @click="onLinkContainerClick"
            >
              <a
                class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[7.188rem]"
                href="https://www.sweetgreen.com/"
                target="_blank"
                >sweetgreen.com</a
              >
            </div>
          </div>
          <div
            class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.925rem]"
          >
            <div
              class="flex flex-col items-start justify-start cursor-pointer"
              @click="onLinkContainerClick1"
            >
              <a
                class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[7.688rem]"
                href="https://shop.sweetgreen.com/"
                target="_blank"
                >sweetgreen Shop</a
              >
            </div>
          </div>
          <div
            class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.944rem]"
          >
            <div
              class="flex flex-col items-start justify-start cursor-pointer"
              @click="onLinkContainerClick2"
            >
              <a
                class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[3.875rem]"
                href="https://www.sweetgreen.com/catering"
                target="_blank"
                >Catering</a
              >
            </div>
          </div>
          <div
            class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[0.25rem] text-[0.938rem]"
          >
            <div class="self-stretch flex flex-row items-start justify-start">
              <div class="flex flex-col items-start justify-start">
                <div
                  class="relative leading-[1.375rem] inline-block min-w-[5rem]"
                >
                  Contact Us
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="flex-1 flex flex-row items-start justify-start min-w-[18.75rem] max-w-full [row-gap:20px] mq450:flex-wrap mq1350:flex-1"
      >
        <div
          class="flex-1 flex flex-col items-start justify-start py-[0rem] px-[0.75rem] box-border min-w-[9.375rem]"
        >
          <div class="self-stretch flex flex-col items-start justify-start">
            <div
              class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1rem] text-[0.956rem]"
            >
              <div class="self-stretch flex flex-col items-start justify-start">
                <div class="self-stretch relative leading-[1.375rem] uppercase">
                  Social Media
                </div>
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick3"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[4.438rem]"
                  href="https://www.instagram.com/sweetgreen/"
                  target="_blank"
                  >Instagram</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.963rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick4"
              >
                <a
                  class="[text-decoration:none] relative leading-[1.375rem] text-[inherit] inline-block min-w-[3.188rem]"
                  >Twitter</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick5"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[2.75rem]"
                  href="https://www.tiktok.com/@sweetgreen"
                  target="_blank"
                  >Tiktok</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.975rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick6"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[3.313rem]"
                  href="https://open.spotify.com/user/1224421164"
                  target="_blank"
                  >Spotify</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.913rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick7"
              >
                <a
                  class="[text-decoration:none] relative leading-[1.375rem] text-[inherit] inline-block min-w-[4.25rem]"
                  >Facebook</a
                >
              </div>
            </div>
          </div>
        </div>
        <div
          class="flex-1 flex flex-col items-start justify-start pt-[0rem] px-[0.75rem] pb-[3rem] box-border min-w-[9.375rem] min-h-[9.875rem] z-[1] ml-[-0.007rem] text-[0.944rem] mq450:ml-0"
        >
          <div class="self-stretch flex flex-col items-start justify-start">
            <div
              class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1rem]"
            >
              <div class="self-stretch flex flex-col items-start justify-start">
                <a
                  class="[text-decoration:none] self-stretch relative leading-[1.375rem] uppercase text-[inherit]"
                  >Terms + Conditions</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.938rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick8"
              >
                <a
                  class="[text-decoration:none] relative leading-[1.375rem] text-[inherit] inline-block min-w-[6.25rem]"
                  >Privacy Policy</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.931rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick9"
              >
                <a
                  class="[text-decoration:none] relative leading-[1.375rem] text-[inherit]"
                  >Terms and Conditions</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0rem] pl-[0rem] pr-[1.312rem] box-border gap-[0.375rem] min-h-[1.5rem] text-[0.925rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick10"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] [text-decoration:none]"
                  href="https://www.sweetgreen.com/privacy-policy/ca-data-opt-out"
                  target="_blank"
                  >Your privacy choices</a
                >
              </div>
              <img
                class="self-stretch w-[2rem] relative max-h-full overflow-hidden shrink-0 min-h-[1.5rem]"
                alt=""
                src="/container-43.svg"
              />
            </div>
          </div>
        </div>
      </div>
      <div
        class="flex-1 flex flex-col items-start justify-start min-w-[18.75rem] max-w-full mq1350:flex-1"
      >
        <div
          class="w-[14.419rem] h-[9.875rem] flex flex-col items-start justify-start py-[0rem] px-[0.75rem] box-border"
        >
          <div class="self-stretch flex flex-col items-start justify-start">
            <div
              class="self-stretch flex flex-col items-start justify-start pt-[0rem] px-[0rem] pb-[1rem]"
            >
              <div class="self-stretch flex flex-col items-start justify-start">
                <div class="self-stretch relative leading-[1.375rem] uppercase">
                  Download the App
                </div>
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.975rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick11"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[1.625rem]"
                  href="https://apps.apple.com/us/app/sweetgreen/id594329490"
                  target="_blank"
                  >iOS</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex flex-row items-center justify-start py-[0.062rem] px-[0rem] box-border min-h-[1.5rem] text-[0.931rem]"
            >
              <div
                class="flex flex-col items-start justify-start cursor-pointer"
                @click="onLinkContainerClick12"
              >
                <a
                  class="relative leading-[1.375rem] text-[inherit] inline-block [text-decoration:none] min-w-[3.5rem]"
                  href="https://play.google.com/store/apps/details"
                  target="_blank"
                  >Android</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-[9.875rem] w-[14.419rem] flex flex-col items-start justify-start py-[0rem] px-[0.75rem] box-border text-right text-[0.906rem]"
      >
        <div class="self-stretch flex flex-col items-start justify-start">
          <div class="self-stretch flex flex-col items-end justify-start">
            <div class="self-stretch relative leading-[1.375rem]">
              ©sweetgreen 2024
            </div>
          </div>
          <div
            class="self-stretch flex flex-col items-end justify-start text-[0.894rem]"
          >
            <div class="self-stretch relative leading-[1.375rem]">v6.223.1</div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "FooterWidget",
  methods: {
    onLinkContainerClick() {
      window.open("https://www.sweetgreen.com/");
    },
    onLinkContainerClick1() {
      window.open("https://shop.sweetgreen.com/");
    },
    onLinkContainerClick2() {
      window.open("https://www.sweetgreen.com/catering");
    },
    onLinkContainerClick3() {
      window.open("https://www.instagram.com/sweetgreen/");
    },
    onLinkContainerClick4() {
      window.open("https://twitter.com/sweetgreen");
    },
    onLinkContainerClick5() {
      window.open("https://www.tiktok.com/@sweetgreen");
    },
    onLinkContainerClick6() {
      window.open("https://open.spotify.com/user/1224421164");
    },
    onLinkContainerClick7() {
      window.open("https://www.facebook.com/sweetgreen");
    },
    onLinkContainerClick8() {
      window.open("https://www.sweetgreen.com/privacy-policy");
    },
    onLinkContainerClick9() {
      window.open("https://www.sweetgreen.com/terms");
    },
    onLinkContainerClick10() {
      window.open("https://www.sweetgreen.com/privacy-policy/ca-data-opt-out");
    },
    onLinkContainerClick11() {
      window.open("https://apps.apple.com/us/app/sweetgreen/id594329490");
    },
    onLinkContainerClick12() {
      window.open("https://play.google.com/store/apps/details");
    },
  },
});
</script>
