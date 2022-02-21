import { defineConfig } from "windicss/helpers";

export default defineConfig({
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
      fancy: ["Lobster", "cursive"],
    },
    fontWeight: {
      thin: "100",
      light: "300",
      normal: "400",
      medium: "500",
      bold: "700",
      black: "900",
    },
  },
});
