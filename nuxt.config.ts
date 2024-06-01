let baseURL = "http://localhost:5000/api";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default {
  devtools: { enabled: false },
  modules: ["@nuxtjs/tailwindcss", "@nuxt-alt/http"],
  http: {
    baseURL,
    credentials: "omit",
    browserBaseURL: baseURL,
  },
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css",
        },
      ],
    },
  },
  runtimeConfig: {
    public: {
      baseURL,
    },
  },
};
