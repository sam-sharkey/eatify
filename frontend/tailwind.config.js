/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        springwood: "#f4f3e7",
        aquadeep: "#00473c",
        razzmatazz: "#e6ff55",
        huntergreen: "#0e150e",
        tasman: "#d8e5d6",
        teal: "#337a70",
        oldlace: "#f4f3e7",
        black: "#000",
        yellowgreen: "#cce63b",
        darkslategray: {
          100: "#333",
          200: "rgba(51, 51, 51, 0.09)",
        },
        bitter: "#8c8c82",
        starkwhite: "#e8dcc6",
      },
      spacing: {},
      fontFamily: {
        "roboto-regular-1588-upper": "Roboto",
        "georgia-regular-48-title": "Georgia",
      },
      borderRadius: {
        "981xl": "1000px",
        "3xs": "10px",
        "2xs": "11px",
        xl: "20px",
      },
    },
    fontSize: {
      base: "16px",
      "base-8": "15.8px",
      "base-9": "15.9px",
      "4xl-3": "23.3px",
      "base-6": "15.6px",
      "base-4": "15.4px",
      lgi: "19px",
      "4xl-4": "23.4px",
      "46xl-4": "65.4px",
      "56xl-6": "75.6px",
      "41xl": "60px",
      "lgi-2": "19.2px",
      "mid-6": "17.6px",
      "5xl": "24px",
      "29xl": "48px",
      "10xl": "29px",
      "19xl": "38px",
      "base-5": "15.5px",
      inherit: "inherit",
    },
    screens: {
      lg: {
        max: "1200px",
      },
      mq1450: {
        raw: "screen and (max-width: 1450px)",
      },
      mq1150: {
        raw: "screen and (max-width: 1150px)",
      },
      mq825: {
        raw: "screen and (max-width: 825px)",
      },
      mq750: {
        raw: "screen and (max-width: 750px)",
      },
      mq450: {
        raw: "screen and (max-width: 450px)",
      },
    },
  },
  corePlugins: {
    preflight: false,
  },
  plugins: [],
};
