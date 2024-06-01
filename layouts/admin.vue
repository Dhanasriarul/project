<template>
  <div>
    <!-- <div
      v-if="!isAdminLoggedIn"
      class="fixed top-0 left-0 w-full h-screen bg-black z-[99999]"
    >
      <div class="flex flex-col justify-center min-h-full px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2
            class="text-2xl font-bold leading-9 tracking-tight text-center text-white"
          >
            Admin Login
          </h2>
        </div>

        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <div class="space-y-6">
            <div>
              <label
                for="email"
                class="block text-sm font-medium leading-6 text-white"
                >Email address</label
              >
              <div class="mt-2">
                <input
                  v-model="user.email"
                  type="email"
                  class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <div class="flex items-center justify-between">
                <label
                  for="password"
                  class="block text-sm font-medium leading-6 text-white"
                  >Password</label
                >
              </div>
              <div class="mt-2">
                <input
                  v-model="user.password"
                  type="password"
                  class="block w-full rounded-md border-0 bg-white/5 py-1.5 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-indigo-500 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div>
              <button
                @click="login()"
                class="flex w-full justify-center rounded-md bg-indigo-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500"
              >
                Sign in
              </button>
            </div>
          </div>
        </div>
      </div>
    </div> -->
    <div>
      <!-- Off-canvas menu for mobile, show/hide based on off-canvas menu state. -->
      <div
        v-if="sidebarIsOpen"
        class="relative z-50 lg:hidden"
        role="dialog"
        aria-modal="true"
      >
        <!--
      Off-canvas menu backdrop, show/hide based on off-canvas menu state.

      Entering: "transition-opacity ease-linear duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "transition-opacity ease-linear duration-300"
        From: "opacity-100"
        To: "opacity-0"
    -->
        <div class="fixed inset-0 bg-gray-900/80"></div>

        <div class="fixed inset-0 flex">
          <!--
        Off-canvas menu, show/hide based on off-canvas menu state.

        Entering: "transition ease-in-out duration-300 transform"
          From: "-translate-x-full"
          To: "translate-x-0"
        Leaving: "transition ease-in-out duration-300 transform"
          From: "translate-x-0"
          To: "-translate-x-full"
      -->
          <div class="relative flex flex-1 w-full max-w-xs mr-16">
            <!--
          Close button, show/hide based on off-canvas menu state.

          Entering: "ease-in-out duration-300"
            From: "opacity-0"
            To: "opacity-100"
          Leaving: "ease-in-out duration-300"
            From: "opacity-100"
            To: "opacity-0"
        -->
            <div class="absolute top-0 flex justify-center w-16 pt-5 left-full">
              <button
                @click="sidebarIsOpen = false"
                type="button"
                class="-m-2.5 p-2.5"
              >
                <span class="sr-only">Close sidebar</span>
                <svg
                  class="w-6 h-6 text-white"
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

            <!-- Sidebar component, swap this element with another sidebar if you like -->
            <div
              class="flex flex-col px-6 pb-2 overflow-y-auto bg-indigo-600 grow gap-y-5"
            >
              <div class="flex items-center h-16 shrink-0">
                <img
                  class="w-auto h-8"
                  src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
                  alt="Your Company"
                />
              </div>
              <nav class="flex flex-col flex-1">
                <ul role="list" class="flex flex-col flex-1 gap-y-7">
                  <li>
                    <ul role="list" class="-mx-2 space-y-1">
                      <li>
                        <!-- Current: "bg-indigo-700 text-white", Default: "text-indigo-200 hover:text-white hover:bg-indigo-700" -->
                        <a
                          href="#"
                          class="flex p-2 text-sm font-semibold leading-6 text-white bg-indigo-700 rounded-md group gap-x-3"
                        >
                          <svg
                            class="w-6 h-6 text-white shrink-0"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            aria-hidden="true"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                            />
                          </svg>
                          Dashboard
                        </a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>

      <!-- Static sidebar for desktop -->
      <div
        class="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col"
      >
        <!-- Sidebar component, swap this element with another sidebar if you like -->
        <div
          class="flex flex-col px-6 overflow-y-auto bg-indigo-600 grow gap-y-5"
        >
          <div class="flex items-center h-16 shrink-0">
            <img
              class="w-auto h-8"
              src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
              alt="Your Company"
            />
          </div>
          <nav class="flex flex-col flex-1">
            <ul role="list" class="flex flex-col flex-1 gap-y-7">
              <li>
                <ul role="list" class="-mx-2 space-y-1">
                  <li>
                    <!-- Current: "bg-indigo-700 text-white", Default: "text-indigo-200 hover:text-white hover:bg-indigo-700" -->
                    <NuxtLink to="/admin">
                      <div
                        class="flex p-2 text-sm font-semibold leading-6 text-white bg-indigo-700 rounded-md group gap-x-3"
                      >
                        <svg
                          class="w-6 h-6 text-white shrink-0"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                          />
                        </svg>
                        Dashboard
                      </div>
                    </NuxtLink>
                  </li>
                  <li>
                    <!-- Current: "bg-indigo-700 text-white", Default: "text-indigo-200 hover:text-white hover:bg-indigo-700" -->
                    <NuxtLink to="/admin/category">
                      <div
                        class="flex p-2 text-sm font-semibold leading-6 text-white bg-indigo-700 rounded-md group gap-x-3"
                      >
                        <svg
                          class="w-6 h-6 text-white shrink-0"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke-width="1.5"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                          />
                        </svg>
                        Category
                      </div>
                    </NuxtLink>
                  </li>
                </ul>
              </li>
              <li class="mt-auto -mx-6">
                <p
                  @click="logout()"
                  class="flex items-center px-6 py-3 text-sm font-semibold leading-6 text-white gap-x-4 hover:bg-indigo-700"
                >
                  <span class="sr-only">Your profile</span>
                  <span aria-hidden="true">Logout </span>
                </p>
              </li>
            </ul>
          </nav>
        </div>
      </div>

      <div
        class="sticky top-0 z-40 flex items-center px-4 py-4 bg-indigo-600 shadow-sm gap-x-6 sm:px-6 lg:hidden"
      >
        <button
          @click="sidebarIsOpen = true"
          type="button"
          class="-m-2.5 p-2.5 text-indigo-200 lg:hidden"
        >
          <span class="sr-only">Open sidebar</span>
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
        <div class="flex-1 text-sm font-semibold leading-6 text-white"></div>
        <p @click="logout()" class="text-white">Logout</p>
      </div>

      <main class="py-10 lg:pl-72">
        <div class="px-4 sm:px-6 lg:px-8">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sidebarIsOpen: false,
      isAdminLoggedIn: false,
      user: {
        email: "admin@demo.com",
        password: "admin",
      },
    };
  },
  mounted() {
    if (localStorage.getItem("isAdminLoggedIn") == "true") {
      this.isAdminLoggedIn = true;
    }
  },
  methods: {
    login() {
      if (!this.user.email || !this.user.password) {
        alert("Please enter email and password");
        return;
      }

      if (
        this.user.email == "admin@demo.com" &&
        this.user.password == "admin"
      ) {
        localStorage.setItem("isAdminLoggedIn", true);
        this.isAdminLoggedIn = true;
        return;
      } else {
        alert("Invalid credentials");
      }
    },
    logout() {
      localStorage.removeItem("isAdminLoggedIn");
      this.isAdminLoggedIn = false;
    },
  },
};
</script>
