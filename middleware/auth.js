// create nuxt middlewate
export default defineNuxtRouteMiddleware(() => {
  if (process.client) {
    let isLoggedIn = localStorage.getItem("isLoggedIn");

    if (isLoggedIn != "true") {
      return navigateTo("/login");
    }
  }
});
