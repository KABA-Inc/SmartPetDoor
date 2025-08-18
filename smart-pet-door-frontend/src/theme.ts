import { createSystem, defineConfig, defaultConfig } from "@chakra-ui/react";

const config = defineConfig({
  theme: {
    tokens: {
      colors: {
        brand: {
          50: { value: "#f7f6f0" }, // background
          100: { value: "#d6e1c9" }, // light olive
          200: { value: "#939b7b" }, // olive, primary
          300: { value: "#e7d7c6" }, // light clay
          400: { value: "#d0946f" }, // clay, secondary
        },
      },
    },
    semanticTokens: {
      colors: {
        brand: {
          solid: { value: "{colors.brand.200}" },
          contrast: { value: "{colors.brand.50}" },
          fg: { value: "{colors.brand.200}" },
          muted: { value: "{colors.brand.100}" },
          subtle: { value: "{colors.brand.100}" },
          emphasized: { value: "{colors.brand.300}" },
          focusRing: { value: "{colors.brand.400}" },
        },
      },
    },
  },
});

export const system = createSystem(defaultConfig, config);
