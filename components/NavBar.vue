<template>
  <div>
    <!-- Header -->
    <header class="absolute inset-x-0 top-0 z-50 h-[128px]">
      <nav
        class="flex items-center justify-between p-6 lg:px-8"
        aria-label="Global"
      >
        <div class="flex lg:flex-1">
          <a href="/" class="-m-1.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img
              class="w-auto h-20"
              src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
              alt=""
            />
          </a>
        </div>
        <div class="flex lg:hidden">
          <button
            @click="navIsOpen = true"
            type="button"
            class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="w-6 h-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </button>
        </div>
        <div class="hidden lg:flex lg:gap-x-12">
          <a href="/#" class="text-sm font-semibold leading-6 text-gray-900"
            >Home</a
          >
          <a
            href="/#about-sec"
            class="text-sm font-semibold leading-6 text-gray-900"
            >About Us</a
          >
          <a
            href="/#services-sec"
            class="text-sm font-semibold leading-6 text-gray-900"
            >Services</a
          >
          <a
            href="/#product-sec"
            class="text-sm font-semibold leading-6 text-gray-900"
            >Products</a
          >
          <p
            @click="logout()"
            class="text-sm font-semibold leading-6 text-gray-900"
          >
            Logout
          </p>
        </div>
      </nav>
      <!-- Mobile menu, show/hide based on menu open state. -->
      <div v-if="navIsOpen" class="lg:hidden" role="dialog" aria-modal="true">
        <!-- Background backdrop, show/hide based on slide-over state. -->
        <div class="fixed inset-0 z-50"></div>
        <div
          class="fixed inset-y-0 right-0 z-50 w-full px-6 py-6 overflow-y-auto bg-white sm:max-w-sm sm:ring-1 sm:ring-gray-900/10"
        >
          <div class="flex items-center justify-between">
            <a href="/" class="-m-1.5 p-1.5">
              <span class="sr-only">Your Company</span>
              <img
                class="w-auto h-14"
                src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
                alt=""
              />
            </a>
            <button
              @click="navIsOpen = false"
              type="button"
              class="-m-2.5 rounded-md p-2.5 text-gray-700"
            >
              <span class="sr-only">Close menu</span>
              <svg
                class="w-6 h-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>
          <div class="flow-root mt-6">
            <div class="-my-6 divide-y divide-gray-500/10">
              <div class="py-6 space-y-2">
                <a
                  @click="navIsOpen = false"
                  href="/#"
                  class="block px-3 py-2 -mx-3 text-base font-semibold leading-7 text-gray-900 rounded-lg hover:bg-gray-50"
                  >Home</a
                >
                <a
                  @click="navIsOpen = false"
                  href="/#about-sec"
                  class="block px-3 py-2 -mx-3 text-base font-semibold leading-7 text-gray-900 rounded-lg hover:bg-gray-50"
                  >About us</a
                >
                <a
                  @click="navIsOpen = false"
                  href="/#services-sec"
                  class="block px-3 py-2 -mx-3 text-base font-semibold leading-7 text-gray-900 rounded-lg hover:bg-gray-50"
                  >Services</a
                >
                <a
                  @click="navIsOpen = false"
                  href="/#product-sec"
                  class="block px-3 py-2 -mx-3 text-base font-semibold leading-7 text-gray-900 rounded-lg hover:bg-gray-50"
                  >Products</a
                >
                <p
                  @click="logout()"
                  class="block px-3 py-2 -mx-3 text-base font-semibold leading-7 text-gray-900 rounded-lg hover:bg-gray-50"
                >
                  Logout
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="h-[128px] w-full"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      navIsOpen: false,
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("isLoggedIn");
      window.location.href = "/login";
    },
  },
};
</script>
