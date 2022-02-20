// vite.config.ts
import { defineConfig } from "vite";
import solid from "solid-start";
var vite_config_default = defineConfig({
  plugins: [
    {
      ...(await import("@mdx-js/rollup")).default({
        jsx: true,
        jsxImportSource: "solid-js",
        providerImportSource: "solid-mdx"
      }),
      enforce: "pre"
    },
    solid({
      extensions: [".mdx", ".md"]
    })
  ]
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImltcG9ydCB7IGRlZmluZUNvbmZpZyB9IGZyb20gXCJ2aXRlXCI7XG5pbXBvcnQgc29saWQgZnJvbSBcInNvbGlkLXN0YXJ0XCI7XG5cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIHBsdWdpbnM6IFtcbiAgICB7XG4gICAgICAuLi4oYXdhaXQgaW1wb3J0KFwiQG1keC1qcy9yb2xsdXBcIikpLmRlZmF1bHQoe1xuICAgICAgICBqc3g6IHRydWUsXG4gICAgICAgIGpzeEltcG9ydFNvdXJjZTogXCJzb2xpZC1qc1wiLFxuICAgICAgICBwcm92aWRlckltcG9ydFNvdXJjZTogXCJzb2xpZC1tZHhcIlxuICAgICAgfSksXG4gICAgICBlbmZvcmNlOiBcInByZVwiXG4gICAgfSxcbiAgICBzb2xpZCh7XG4gICAgICBleHRlbnNpb25zOiBbXCIubWR4XCIsIFwiLm1kXCJdXG4gICAgfSlcbiAgXVxufSk7XG4iXSwKICAibWFwcGluZ3MiOiAiO0FBQUE7QUFDQTtBQUVBLElBQU8sc0JBQVEsYUFBYTtBQUFBLEVBQzFCLFNBQVM7QUFBQSxJQUNQO0FBQUEsU0FDTSxPQUFNLE9BQU8sbUJBQW1CLFFBQVE7QUFBQSxRQUMxQyxLQUFLO0FBQUEsUUFDTCxpQkFBaUI7QUFBQSxRQUNqQixzQkFBc0I7QUFBQTtBQUFBLE1BRXhCLFNBQVM7QUFBQTtBQUFBLElBRVgsTUFBTTtBQUFBLE1BQ0osWUFBWSxDQUFDLFFBQVE7QUFBQTtBQUFBO0FBQUE7IiwKICAibmFtZXMiOiBbXQp9Cg==
