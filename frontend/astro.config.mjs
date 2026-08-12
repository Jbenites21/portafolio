// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  integrations: [react()],

  vite: {
    plugins: [tailwindcss()],
    server: {
      allowedHosts: ['alb-proyecto-1459454180.us-east-1.elb.amazonaws.com']
    }
  },

  //configuracion explicitamente para que el servidor escuche en todas las interfaces de red y en el puerto 4321
  server: {
    host: "0.0.0.0",
    port: 4321
  }
});