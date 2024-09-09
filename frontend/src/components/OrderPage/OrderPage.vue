<template>
  <div
    class="h-[828px] bg-antiquewhite max-w-full flex flex-row items-start justify-start pt-0 px-0.5 pb-0 box-border min-h-[828px] leading-[normal] tracking-[normal] text-left text-8xl-9 text-gray-100 font-inter mq450:h-auto mq1050:pl-5 mq1050:pr-5 mq1050:box-border"
  >
    <div
      class="w-[525px] bg-oldlace border-gray-100 border-r-[1px] border-solid box-border flex flex-col items-start justify-start max-w-[525px] shrink-0 mq1050:hidden mq750:max-w-full"
    >
      <div
        class="self-stretch h-[894px] overflow-y-auto shrink-0 flex flex-col items-start justify-start pt-0 px-0 pb-[764px] box-border max-w-full lg:pb-[497px] lg:box-border mq450:h-auto mq750:pb-[323px] mq750:box-border"
      >
        <div
          class="self-stretch flex flex-col items-center justify-start shrink-0"
        >
          <div
            class="w-full bg-oldlace flex flex-col items-start justify-start pt-0 px-10 pb-6 box-border max-w-[1520px]"
          >
            <div
              class="self-stretch flex flex-col items-start justify-start pt-10 px-0 pb-0"
            >
              <div
                class="self-stretch flex flex-row items-center justify-between min-h-[36px] gap-5 mq450:flex-wrap"
              >
                <div
                  class="flex flex-col items-start justify-start py-0 pl-0 pr-3"
                >
                  <a
                    class="[text-decoration:none] relative tracking-[1px] leading-[36px] text-[inherit] mq450:text-3xl mq450:leading-[29px]"
                    >Create Your Own</a
                  >
                </div>
                <div
                  class="h-8 w-8 rounded-81xl flex flex-col items-center justify-center"
                >
                  <img
                    class="w-8 h-8 relative"
                    loading="lazy"
                    alt=""
                    src="/svg1.svg"
                  />
                </div>
              </div>
              <div
                class="self-stretch flex flex-col items-start justify-start pt-2 px-0 pb-0 text-[14.1px]"
              >
                <div class="self-stretch relative leading-[22px]">
                  $19.70 - 915 cal
                </div>
              </div>
            </div>
          </div>
        </div>
        <SelectedIngredients />
      </div>
      <div
        class="self-stretch flex flex-col items-center justify-start max-w-full text-center text-mini"
      >
        <div
          class="w-full bg-oldlace border-gray-100 border-t-[1px] border-solid box-border flex flex-row items-start justify-start pt-[15px] px-7 pb-4 max-w-[1520px]"
        >
          <div
            class="w-[456px] flex flex-col items-start justify-start py-0 px-0 box-border max-w-full"
          >
            <div
              class="flex flex-row items-start justify-start flex-wrap content-start py-0 pl-0 pr-0.5 box-border max-w-[103%] shrink-0"
            >
              <div
                class="flex flex-col items-start justify-start py-0 pl-3 pr-[11px]"
              >
                <div class="flex flex-col items-start justify-start">
                  <div
                    class="rounded-81xl border-gray-100 border-[1px] border-solid flex flex-row items-center justify-center py-[11px] px-[79px]"
                  >
                    <div class="flex flex-col items-center justify-start">
                      <div
                        class="relative leading-[22px] inline-block min-w-[50px]"
                      >
                        Cancel
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="flex flex-col items-start justify-start py-0 pl-3 pr-[11px] ml-[-2px] text-mini-5 text-white"
              >
                <div class="flex flex-col items-start justify-start">
                  <div
                    class="rounded-81xl bg-darkslategray-200 flex flex-row items-center justify-center py-[13px] px-[74px]"
                  >
                    <div
                      class="flex flex-col items-center justify-start py-0 px-px"
                    >
                      <div
                        class="relative leading-[22px] inline-block min-w-[60px]"
                      >
                        I'm done
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

    <section
      class="w-[841px] bg-oldlace flex flex-col items-start justify-start pt-0 px-[45px] pb-4 box-border shrink-0 text-left text-[22.1px] text-gray-100 font-inter mq1050:pl-[22px] mq1050:pr-[22px] mq1050:box-border mq1050:max-w-full"
    >
      <MenuCategoriesHeader :categories="categories" activeCategory="Bases" />
      <div
        class="w-full flex flex-col items-start justify-start max-w-[750px] mq750:max-w-full"
      >
        <div class="w-full max-w-2xl flex flex-col gap-4">
          <!-- Section Header -->
          <div class="border-b border-gainsboro-200 pb-6">
            <h2 class="text-xl font-semibold tracking-wide">Bases</h2>
          </div>

          <!-- Items List -->
          <div
            class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8"
          >
            <!-- Product Cards -->
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Chopped Romaine"
              containerImage="/container-91@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Arugula"
              containerImage="/container-101@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Baby Spinach"
              containerImage="/container-111@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Spring Mix"
              containerImage="/container1@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Shredded Kale"
              containerImage="/container-131@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Herbed Quinoa"
              containerImage="/container-141@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="White Rice"
              containerImage="/container-141@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Wild Rice"
              containerImage="/container-141@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Spring Mix"
              containerImage="/container1@2x.png"
            />
          </div>
        </div>
        <div
          class="w-full border-b border-gainsboro-200 py-10 lg:py-6 px-0 gap-4 text-xl font-medium text-gray-700"
        >
          <!-- Section Header -->
          <h2 class="tracking-wide">Premiums</h2>
          <div
            class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8"
          >
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Crispy Onions"
              containerImage="/container-151@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Pickled Onions"
              containerImage="/container-171@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Basil"
              containerImage="/container-191@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Raw Carrots"
              containerImage="/container-201@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Chickpeas"
              containerImage="/container-211@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Cilantro"
              containerImage="/container-221@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Cucumbers"
              containerImage="/container-231@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Roasted Sweet Potatoes"
              containerImage="/container-241@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Shredded Cabbage"
              containerImage="/container-251@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Spicy Broccoli"
              containerImage="/container-261@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Tomatoes"
              containerImage="/container-271@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Crispy Rice"
              containerImage="/container-281@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Roasted Almonds"
              containerImage="/container-291@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Tortilla Chips"
              containerImage="/container-301@2x.png"
            />
          </div>
        </div>
        <div
          class="w-full border-b border-gainsboro-200 py-10 lg:py-6 px-0 gap-4 text-xl font-medium text-gray-700"
        >
          <!-- Section Header -->
          <h2 class="tracking-wide">Premiums</h2>

          <!-- Product Grid -->
          <div
            class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-8 w-full max-w-4xl mx-auto"
          >
            <!-- Premium Items -->
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Caramelized Garlic Steak"
              containerImage="/container-311@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Goat Cheese"
              containerImage="/container-321@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Avocado"
              containerImage="/container-331@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Veg Slaw"
              containerImage="/container-341@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Shaved Parmesan"
              containerImage="/container-351@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Roasted Tofu"
              containerImage="/container-361@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Miso Glazed Salmon"
              containerImage="/container-371@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Parmesan Crisps"
              containerImage="/container-381@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Warm Portobello Mix"
              containerImage="/container-391@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Hummus"
              containerImage="/container-401@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Warm Roasted Sweet Potatoes"
              containerImage="/container-411@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Roasted Chicken"
              containerImage="/container-45@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Hard Boiled Egg"
              containerImage="/container-441@2x.png"
            />
          </div>
        </div>
        <div
          class="w-full border-b border-gainsboro-200 py-10 lg:py-6 px-0 gap-4 text-xl font-normal text-gray-700"
        >
          <!-- Section Header -->
          <h2 class="tracking-wide">Dressings</h2>

          <!-- Product Grid -->
          <div
            class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-6 w-full max-w-4xl mx-auto"
          >
            <!-- Dressing Items -->
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Red Wine Vinaigrette"
              containerImage="/container-46@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Caesar"
              containerImage="/container-47@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Spicy Cashew"
              containerImage="/container-48@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Lemon Squeeze"
              containerImage="/container-49@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Honey BBQ Sauce"
              containerImage="/container-50@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Extra Virgin Olive Oil"
              containerImage="/container-511@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Sweetgreen Hot Sauce"
              containerImage="/container-52@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Crushed Red Pepper"
              containerImage="/container-53@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Green Goddess Ranch"
              containerImage="/container-54@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Lime Cilantro Jalapeno Vinaigrette"
              containerImage="/container-55@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Hot Honey Mustard Sauce"
              containerImage="/container-56@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Miso Sesame Ginger"
              containerImage="/container-58@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Umami Seasoning"
              containerImage="/container-59@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Balsamic Vinegar"
              containerImage="/container-60@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Pesto Vinaigrette"
              containerImage="/container-611@2x.png"
            />
            <ProductCard
              backgroundImage="/background-10.svg"
              itemName="Lime Squeeze"
              containerImage="/container-62@2x.png"
            />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import SelectedIngredients from "./SelectedIngredients.vue";
import ProductCard from "./ProductCard.vue";
import MenuCategoriesHeader from "../MenuPage/MenuCategoriesHeader.vue";

export default defineComponent({
  name: "CustomOrder",
  components: {
    SelectedIngredients,
    MenuCategoriesHeader,
    ProductCard,
  },
  setup() {
    const categories = ["Bases", "Toppings", "Premiums", "Dressings"];
    return { categories };
  },
});
</script>
