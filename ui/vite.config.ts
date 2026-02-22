import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    lib: {
      entry: 'src/index.tsx',
      name: 'OpenSquadPluginUI',
      fileName: 'index',
      formats: ['es'],
    },
    // Output directly to ui/ so the backend can serve it at
    // /api/plugins/static/{plugin_id}/ui/index.js
    outDir: './',
    emptyOutDir: false, // Never delete src/, package.json, etc.
    rollupOptions: {
      // Bundle react/react-dom into the plugin so it's self-contained.
      // The plugin is loaded as a remote ESM module in the browser;
      // bare specifiers like 'react' won't resolve without an importmap.
    },
  },
});
