import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

const ccode = require("vite-raw-plugin");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), ccode({ fileRegex: /\.c$/ })],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
