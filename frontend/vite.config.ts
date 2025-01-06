import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  server: {
    host: "0.0.0.0", // Bind to all interfaces so Docker can expose it
    port: 5173, // Default port for Vite
    strictPort: true, // Fail if the port is already in use
    watch: {
      usePolling: true, // Fix for file changes not being detected in Docker
    },
    hmr: {
      clientPort: 5173, // Ensure HMR uses the correct port
    },
  },
  plugins: [react()],
});
