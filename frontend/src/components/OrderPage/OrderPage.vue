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
      class="w-[841px] bg-oldlace flex flex-col items-start justify-start pt-0 px-[45px] pb-4 box-border max-w-[calc(100%_-_525px)] shrink-0 text-left text-[22.1px] text-gray-100 font-inter mq1050:pl-[22px] mq1050:pr-[22px] mq1050:box-border mq1050:max-w-full"
    >
      <header
        class="ml-[-82.5px] w-[915px] border-gray-300 border-b-[1px] border-solid box-border flex flex-row items-start justify-start py-0 px-10 top-[0] z-[99] sticky max-w-[122%] shrink-0 text-left text-base-8 text-gray-200 font-inter"
      >
        <div
          class="w-[385px] flex flex-row items-start justify-start relative max-w-full"
        >
          <div
            class="flex flex-row items-start justify-start text-base-9 text-darkslategray-200"
          >
            <div class="flex flex-col items-start justify-start py-3 px-0">
              <div class="flex flex-col items-start justify-start">
                <a
                  class="[text-decoration:none] relative leading-[22px] text-[inherit] inline-block min-w-[46px] whitespace-nowrap"
                  >Bases</a
                >
              </div>
            </div>
          </div>
          <div
            class="flex-1 flex flex-row items-start justify-end py-0 pl-10 pr-0"
          >
            <div class="flex flex-col items-start justify-start py-3 px-0">
              <div class="flex flex-col items-start justify-start">
                <a
                  class="[text-decoration:none] relative leading-[22px] text-[inherit] inline-block min-w-[69px]"
                  >Toppings</a
                >
              </div>
            </div>
          </div>
          <div
            class="flex-1 flex flex-row items-start justify-start py-0 pl-[39px] pr-0 text-base-2"
          >
            <div class="flex flex-col items-start justify-start py-3 px-0">
              <div class="flex flex-col items-start justify-start">
                <a
                  class="[text-decoration:none] relative leading-[22px] text-[inherit] inline-block min-w-[77px] whitespace-nowrap"
                  >Premiums</a
                >
              </div>
            </div>
          </div>
          <div
            class="flex-1 flex flex-row items-start justify-start py-0 pl-[39px] pr-0"
          >
            <div class="flex flex-col items-start justify-start py-3 px-0">
              <div class="flex flex-col items-start justify-start">
                <a
                  class="[text-decoration:none] relative leading-[22px] text-[inherit] inline-block min-w-[75px]"
                  >Dressings</a
                >
              </div>
            </div>
          </div>
          <div
            class="w-[85.5px] !m-[0] absolute bottom-[0px] left-[-40px] flex flex-row items-start justify-end z-[1]"
          >
            <div class="h-px w-[45px] relative bg-darkslategray-200" />
          </div>
        </div>
      </header>
      <div
        class="w-full flex flex-col items-start justify-start max-w-[750px] mq750:max-w-full"
      >
        <div
          class="self-stretch border-gainsboro-200 border-b-[1px] border-solid box-border flex flex-col items-start justify-start pt-10 pb-[39px] px-0 gap-4 max-w-full mq750:pt-[26px] mq750:pb-[25px] mq750:box-border"
        >
          <div
            class="self-stretch relative tracking-[1px] leading-[28px] mq450:text-lg mq450:leading-[22px]"
          >
            Bases
          </div>
          <div
            class="self-stretch flex flex-col items-start justify-start gap-4 max-w-full text-center text-sm-1"
          >
            <div
              class="self-stretch flex flex-row items-start justify-center [row-gap:20px] mq750:flex-wrap"
            >
              <div
                class="flex-1 flex flex-col items-start justify-start py-0 pl-0 pr-2 box-border min-w-[142px] max-w-[145px] text-sm-8"
              >
                <div
                  class="self-stretch flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="w-full overflow-hidden flex flex-col items-start justify-start py-0 pl-7 pr-6 box-border max-w-[113.2px]"
                    >
                      <a
                        class="[text-decoration:none] self-stretch relative leading-[16px] text-[inherit] inline-block min-w-[60.1px]"
                        >Chopped
                      </a>
                      <div
                        class="flex flex-row items-start justify-start py-0 pl-px pr-1.5 text-sm-2"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[54px]"
                        >
                          Romaine
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-91@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="flex-[0.9449] flex flex-col items-start justify-center py-0 px-2 box-border min-w-[150px] max-w-[153px] mq450:flex-1"
              >
                <div
                  class="self-stretch h-[171px] flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="w-[91px] flex flex-col items-start justify-center py-2 px-5 box-border"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start max-w-[51.51px]"
                      >
                        <a
                          class="[text-decoration:none] relative leading-[16px] text-[inherit] inline-block min-w-[49px]"
                          >Arugula</a
                        >
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-101@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="flex-[0.9449] flex flex-col items-start justify-center py-0 px-2 box-border min-w-[150px] max-w-[153px] mq450:flex-1"
              >
                <div
                  class="self-stretch h-[171px] flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="self-stretch flex flex-col items-start justify-center py-2 px-3"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[88.77px]"
                      >
                        <a
                          class="[text-decoration:none] relative leading-[16px] text-[inherit] inline-block min-w-[85px]"
                          >Baby Spinach</a
                        >
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-111@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <ListItem3
                background="/background-10.svg"
                springMix="Spring Mix"
                container="/container1@2x.png"
              />
              <div
                class="flex-[0.9449] flex flex-col items-start justify-center py-0 px-2 box-border min-w-[150px] max-w-[153px] text-smi-9 mq450:flex-1"
              >
                <div
                  class="self-stretch h-[171px] flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-[9px]"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[93.41px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[90px]"
                        >
                          Shredded Kale
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-131@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="w-[451.6px] grid flex-row items-start justify-start gap-2 max-w-full grid-cols-[repeat(3,_minmax(115px,_1fr))] text-smi-8 mq450:justify-center mq450:grid-cols-[minmax(115px,_1fr)]"
            >
              <div
                class="flex flex-col items-start justify-start py-0 pl-0 pr-[7px]"
              >
                <ContainerComponent
                  propFlex="unset"
                  propMinWidth="unset"
                  propAlignSelf="stretch"
                  background="/background-10.svg"
                  propPadding="unset"
                />
              </div>
              <div
                class="h-[171px] flex flex-row items-start justify-start relative"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="self-stretch rounded-2xl bg-antiquewhite flex flex-row items-start justify-start p-5 z-[1]"
                >
                  <div
                    class="overflow-hidden flex flex-row items-start justify-start py-0 px-px box-border max-w-[95.7px]"
                  >
                    <div
                      class="relative leading-[16px] inline-block min-w-[92px]"
                    >
                      Herbed Quinoa
                    </div>
                  </div>
                  <div class="h-[115px] flex-1 relative hidden" />
                </div>
              </div>
              <div
                class="h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border text-sm-1"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="self-stretch flex flex-col items-start justify-center py-2 px-[21px]"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start py-0 pl-px pr-0 box-border max-w-[69.94px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[67px]"
                        >
                          White Rice
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-141@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <IngredientsSection />
        <div
          class="self-stretch border-gainsboro-200 border-b-[1px] border-solid box-border flex flex-col items-start justify-start pt-10 px-0 pb-[39px] gap-4 max-w-full text-2xl-8 mq750:pt-[26px] mq750:pb-[25px] mq750:box-border"
        >
          <div
            class="self-stretch relative tracking-[1px] leading-[28px] mq450:text-mid mq450:leading-[22px]"
          >
            Premiums
          </div>
          <div
            class="ml-[-8px] w-[766px] flex flex-row items-start justify-center flex-wrap content-start max-w-[103%] shrink-0 text-center text-sm-2"
          >
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[150px] max-w-[153px] text-sm-5"
            >
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="overflow-hidden flex flex-col items-start justify-start py-0 pl-[18px] pr-3.5 box-border max-w-[113.2px]"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[80px]"
                      >
                        Caramelized
                      </div>
                      <div
                        class="relative text-sm-1 leading-[16px] inline-block min-w-[75px]"
                      >
                        Garlic Steak
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-311@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border text-smi"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-3.5"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-0.5 box-border max-w-[84.19px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[80px]"
                        >
                          Goat Cheese
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-321@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border text-smi-8"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="w-24 flex flex-col items-start justify-center py-2 px-5 box-border"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[56.38px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[53px]"
                        >
                          Avocado
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-331@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[150px] max-w-[153px] text-[13.9px]"
            >
              <ListItem4
                background="/background-10.svg"
                vegSlaw="Veg Slaw"
                container="/container-341@2x.png"
              />
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-end justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="w-full overflow-hidden flex flex-col items-end justify-start py-0 px-[25px] box-border max-w-[113.2px]"
                    >
                      <div
                        class="self-stretch flex flex-row items-start justify-end py-0 pl-[9px] pr-[5px]"
                      >
                        <div
                          class="flex-1 relative leading-[16px] inline-block min-w-[49.2px]"
                        >
                          Shaved
                        </div>
                      </div>
                      <div
                        class="relative text-smi leading-[16px] inline-block min-w-[62px]"
                      >
                        Parmesan
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-end py-0 pl-3 pr-[11px]"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-351@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border z-[1] text-smi"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-[13px]"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 pl-px pr-0.5 box-border max-w-[85.89px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[82px]"
                        >
                          Roasted Tofu
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-361@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[150px] max-w-[153px]"
            >
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="overflow-hidden flex flex-col items-start justify-start py-0 pl-[19px] pr-[15px] box-border max-w-[113.2px]"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[78px]"
                      >
                        Miso Glazed
                      </div>
                      <div
                        class="flex flex-row items-start justify-start py-0 pl-[13px] pr-5 text-sm-3"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[47px]"
                        >
                          Salmon
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-371@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <ListItem3
                propFlex="unset"
                propMinWidth="unset"
                propAlignSelf="stretch"
                propHeight="171px"
                propHeight1="unset"
                propFlex1="1"
                background="/background-10.svg"
                springMix="Parmesan Crisps"
                propMinWidth1="105px"
                container="/container-381@2x.png"
              />
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2 text-sm-3"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="w-full overflow-hidden flex flex-col items-start justify-start py-0 pl-[5px] pr-0.5 box-border max-w-[113.2px]"
                    >
                      <div
                        class="self-stretch relative leading-[16px] inline-block min-w-[105.3px]"
                      >
                        Warm Portobello
                      </div>
                      <div
                        class="flex flex-row items-start justify-start py-0 pl-10 pr-11 text-smi-9"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[22px]"
                        >
                          Mix
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-391@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[150px] max-w-[153px]"
            >
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-5"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[59.01px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[56px]"
                        >
                          Hummus
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-401@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2 text-sm-5"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="w-full overflow-hidden flex flex-col items-end justify-start py-0 px-[7px] box-border max-w-[113.2px]"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[93px]"
                      >
                        Warm Roasted
                      </div>
                      <div
                        class="self-stretch relative text-smi leading-[16px] inline-block min-w-[97.8px]"
                      >
                        Sweet Potatoes
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-411@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-row items-start justify-start py-0 px-2 box-border"
              >
                <ContainerComponent2
                  propMinWidth="unset"
                  propAlignSelf="stretch"
                  background="/background-10.svg"
                  propHeight="unset"
                  propAlignSelf1="stretch"
                  container="/container-421@2x.png"
                />
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[150px] max-w-[153px] text-smi"
            >
              <ListItem3
                propFlex="unset"
                propMinWidth="unset"
                propAlignSelf="stretch"
                propHeight="171px"
                propHeight1="unset"
                propFlex1="1"
                background="/background-10.svg"
                springMix="Blue Cheese"
                propMinWidth1="78px"
                container="/container-431@2x.png"
              /><ListItem4
                background="/background-10.svg"
                propWidth="unset"
                propPadding="0px 1px"
                vegSlaw="Hard Boiled Egg"
                propMinWidth="98px"
                container="/container-441@2x.png"
              />
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-0.5"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[107.71px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[104px]"
                        >
                          Roasted Chicken
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-45@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div
          class="self-stretch border-gainsboro-200 border-b-[1px] border-solid box-border flex flex-col items-start justify-start pt-10 px-0 pb-[39px] gap-4 max-w-full text-2xl mq750:pt-[26px] mq750:pb-[25px] mq750:box-border"
        >
          <h2
            class="m-0 self-stretch relative text-inherit tracking-[1px] leading-[28px] font-normal font-[inherit] mq450:text-mid mq450:leading-[22px]"
          >
            Dressings
          </h2>
          <div
            class="ml-[-8px] w-[766px] flex flex-row items-start justify-center gap-2 max-w-[103%] shrink-0 text-center text-smi-9 mq750:flex-wrap"
          >
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[99px]"
            >
              <div
                class="self-stretch flex flex-row items-start justify-start py-0 px-2 text-sm-7"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start relative"
                >
                  <img
                    class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                  >
                    <div
                      class="w-full overflow-hidden flex flex-col items-end justify-start py-0 px-[22px] box-border max-w-[113.2px]"
                    >
                      <div
                        class="flex flex-row items-start justify-end py-0 pl-1.5 pr-px"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[62px]"
                        >
                          Red Wine
                        </div>
                      </div>
                      <div
                        class="self-stretch relative text-sm-2 leading-[16px] inline-block min-w-[68.4px]"
                      >
                        Vinaigrette
                      </div>
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                    >
                      <img
                        class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                        alt=""
                        src="/container-46@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border text-smi"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="w-[87px] flex flex-col items-start justify-center py-2 px-5 box-border"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[47.34px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[44px]"
                        >
                          Caesar
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-47@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-[11px]"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[90.54px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[87px]"
                        >
                          Spicy Cashew
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-48@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-[5px]"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[102.38px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[99px]"
                        >
                          Lemon Squeeze
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-49@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="flex-[0.9449] flex flex-col items-start justify-start py-0 pl-0 pr-2 box-border gap-4 min-w-[94px] text-sm-7 mq450:flex-1"
            >
              <div
                class="self-stretch flex flex-row items-start justify-start relative"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-end justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="overflow-hidden flex flex-col items-start justify-start py-0 pl-[21px] pr-4 box-border max-w-[113.2px]"
                  >
                    <div
                      class="relative leading-[16px] inline-block min-w-[75px]"
                    >
                      Honey BBQ
                    </div>
                    <div
                      class="flex flex-row items-start justify-start py-0 pl-4 pr-[21px] text-sm-2"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[39px]"
                      >
                        Sauce
                      </div>
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-end py-0 pl-3 pr-[11px]"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-50@2x.png"
                    />
                  </div>
                </div>
              </div>
              <div
                class="self-stretch flex flex-row items-start justify-start relative text-sm-3"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-end justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="w-full overflow-hidden flex flex-col items-start justify-start py-0 pl-1 pr-0 box-border max-w-[113.2px]"
                  >
                    <div
                      class="self-stretch relative leading-[16px] inline-block min-w-[108.1px]"
                    >
                      Extra Virgin Olive
                    </div>
                    <div
                      class="flex flex-row items-start justify-start py-0 pl-11 pr-12 text-sm-5"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[17px]"
                      >
                        Oil
                      </div>
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-end py-0 pl-3 pr-[11px]"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-511@2x.png"
                    />
                  </div>
                </div>
              </div>
              <ContainerComponent4
                background="/background-10.svg"
                sweetgreenHot="Sweetgreen Hot "
                sauce="Sauce"
                container="/container-52@2x.png"
              /><ContainerComponent5
                noriSesame="Crushed Red "
                seasoning="Pepper"
                container="/container-53@2x.png"
                propTextDecoration="unset"
                propMinWidth="45px"
              />
            </div>
            <div
              class="flex-[0.9449] flex flex-col items-start justify-start py-0 pl-0 pr-2 box-border gap-4 min-w-[94px] text-sm-8 mq450:flex-1"
            >
              <ContainerComponent4
                background="/background-10.svg"
                sweetgreenHot="Green Goddess "
                propMinWidth="98.4px"
                propAlignSelf="stretch"
                sauce="Ranch"
                propFlex="1"
                container="/container-54@2x.png"
              />
              <div
                class="self-stretch flex flex-row items-start justify-start relative"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="w-full h-8 overflow-hidden shrink-0 flex flex-col items-end justify-start py-0 px-[11px] box-border max-w-[113.2px]"
                  >
                    <div
                      class="relative leading-[16px] inline-block min-w-[86px] shrink-0"
                    >
                      Lime Cilantro
                    </div>
                    <div
                      class="flex flex-row items-start justify-end py-0 px-[5px] text-xs"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[66px] shrink-0"
                      >
                        Jalapeno …
                      </div>
                    </div>
                    <div
                      class="self-stretch h-4 flex flex-row items-start justify-end py-0 pl-3 pr-2.5 box-border shrink-0 text-sm-2"
                    >
                      <div
                        class="self-stretch flex-1 relative leading-[16px] flex items-center justify-center shrink-0"
                      >
                        Vinaigrette
                      </div>
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-55@2x.png"
                    />
                  </div>
                </div>
              </div>
              <div
                class="self-stretch flex flex-row items-start justify-start relative text-sm-5"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="overflow-hidden flex flex-col items-end justify-start py-0 px-[9px] box-border max-w-[113.2px]"
                  >
                    <div
                      class="flex flex-row items-start justify-end py-0 pl-4 pr-[11px]"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[68px]"
                      >
                        Hot Honey
                      </div>
                    </div>
                    <div
                      class="relative text-smi leading-[16px] inline-block min-w-[93px]"
                    >
                      Mustard Sauce
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-56@2x.png"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div
              class="w-[137.2px] flex flex-col items-start justify-start gap-4 text-sm-5"
            >
              <ContainerComponent3
                propFlex="unset"
                propAlignSelf="stretch"
                background="/background-10.svg"
                container="/container-81@2x.png"
                propWidth="calc(100% - 23.2px)"
              />
              <div
                class="self-stretch flex flex-row items-start justify-start relative"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="w-full overflow-hidden flex flex-col items-start justify-start py-0 pl-[15px] pr-[11px] box-border max-w-[113.2px]"
                  >
                    <div
                      class="relative leading-[16px] inline-block min-w-[86px]"
                    >
                      Miso Sesame
                    </div>
                    <div
                      class="self-stretch flex flex-row items-start justify-start py-0 pl-5 pr-[26px] text-smi"
                    >
                      <div
                        class="flex-1 relative leading-[16px] inline-block min-w-[41.4px]"
                      >
                        Ginger
                      </div>
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-58@2x.png"
                    />
                  </div>
                </div>
              </div>
              <div
                class="self-stretch flex flex-row items-start justify-start relative text-sm"
              >
                <img
                  class="h-full w-full absolute !m-[0] right-[0px] bottom-[-3px] left-[0px] rounded-xl max-w-full overflow-hidden"
                  alt=""
                  src="/background-10.svg"
                />
                <div
                  class="flex-1 rounded-2xl bg-antiquewhite flex flex-col items-start justify-start pt-3 px-3 pb-5 z-[1]"
                >
                  <div
                    class="overflow-hidden flex flex-col items-end justify-start py-0 px-[23px] box-border max-w-[113.2px]"
                  >
                    <div
                      class="flex flex-row items-start justify-end py-0 pl-[13px] pr-[7px]"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[47px]"
                      >
                        Umami
                      </div>
                    </div>
                    <div
                      class="relative text-sm-1 leading-[16px] inline-block min-w-[65px]"
                    >
                      Seasoning
                    </div>
                  </div>
                  <div
                    class="self-stretch flex flex-row items-start justify-start py-0 pl-[11px] pr-3"
                  >
                    <img
                      class="h-[107px] flex-1 relative max-w-[113.2px] overflow-hidden object-cover"
                      alt=""
                      src="/container-59@2x.png"
                    />
                  </div>
                </div>
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-start justify-start gap-4 min-w-[99px] text-smi"
            >
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-px"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[110.09px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[107px]"
                        >
                          Balsamic Vinegar
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-60@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border text-sm-1"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="self-stretch flex flex-col items-start justify-center py-2 px-px"
                    >
                      <div
                        class="w-full overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[110.8px]"
                      >
                        <div
                          class="self-stretch relative leading-[16px] inline-block min-w-[107px]"
                        >
                          Pesto Vinaigrette
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-611@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="self-stretch h-[171px] flex flex-col items-start justify-center py-0 px-2 box-border"
              >
                <div
                  class="self-stretch flex-1 flex flex-col items-start justify-start relative"
                >
                  <img
                    class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
                    alt=""
                    src="/background-10.svg"
                  />
                  <div
                    class="self-stretch flex-1 rounded-2xl bg-antiquewhite flex flex-col items-center justify-start p-3 z-[1]"
                  >
                    <div
                      class="flex flex-col items-start justify-center py-2 px-[11px]"
                    >
                      <div
                        class="overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[90.63px]"
                      >
                        <div
                          class="relative leading-[16px] inline-block min-w-[87px]"
                        >
                          Lime Squeeze
                        </div>
                      </div>
                    </div>
                    <div
                      class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2"
                    >
                      <img
                        class="w-full flex-1 relative max-w-[113.2px] overflow-hidden max-h-full object-cover"
                        alt=""
                        src="/container-62@2x.png"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import SelectedIngredients from "./SelectedIngredients.vue";
import ListItem3 from "./ListItem3.vue";
import ContainerComponent from "./ContainerComponent.vue";
import IngredientsSection from "./IngredientsSection.vue";
import ListItem4 from "./ListItem4.vue";
import ContainerComponent2 from "./ContainerComponent2.vue";
import ContainerComponent4 from "./ContainerComponent4.vue";
import ContainerComponent5 from "./ContainerComponent5.vue";
import ContainerComponent3 from "./ContainerComponent3.vue";

export default defineComponent({
  name: "CustomOrder",
  components: {
    SelectedIngredients,
    ListItem3,
    ContainerComponent,
    IngredientsSection,
    ListItem4,
    ContainerComponent2,
    ContainerComponent4,
    ContainerComponent5,
    ContainerComponent3,
  },
});
</script>
