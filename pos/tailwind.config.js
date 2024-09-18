/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx,vue}"],
  theme: {
    extend: {
      colors: {
        gray: "#111315",
        white: "#fff",
        darkgray: "#adadad",
        pink: {
          "100": "#fac1d9",
          "200": "#f8c0d7",
          "300": "#e0a8bf",
        },
        darkslategray: {
          "100": "#3d4142",
          "200": "#333",
          "300": "#292c2d",
        },
      },
      spacing: {},
      fontFamily: {
        poppins: "Poppins",
      },
      borderRadius: {
        "7xs-2": "5.2px",
        "5xs-5": "7.5px",
        "5xs-4": "7.4px",
        "11xl": "30px",
        "3xs": "10px",
      },
    },
    fontSize: {
      sm: "14px",
      base: "16px",
      "xl-1": "20.1px",
      "6xl": "25px",
      xl: "20px",
      inherit: "inherit",
    },
    screens: {
      mq1125: {
        raw: "screen and (max-width: 1125px)",
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
};
