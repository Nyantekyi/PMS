// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxt/content',
    '@nuxt/ui',
  ],
  devtools: { enabled: true },
  compatibilityDate: '2024-04-03',
  
  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:8000/api',
    },
  },
  
  colorMode: {
    preference: 'light',
  },
})
