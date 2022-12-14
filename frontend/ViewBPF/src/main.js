import { createApp } from "vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import App from "./App.vue";
import "element-plus/theme-chalk/dark/css-vars.css";

import "./assets/main.css";
import router from "./router";

const app = createApp(App);

app.use(router);
app.use(ElementPlus);
app.mount("#app");
