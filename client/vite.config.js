import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

import dotenv from "dotenv";
dotenv.config();

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/chatbot": {
        target: process.env.VITE_AZURE_WEB_APP_URL,
        changeOrigin: true,
        secure: false, // Set this to true if you want to verify the SSL certificate
      },
    },
  },
});
