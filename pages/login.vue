<template>
  <div class="flex flex-col justify-center items-center min-h-screen px-6 py-12 lg:px-8 bg-[url('https://images.unsplash.com/photo-1496917756835-20cb06e75b4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80')]">
    <div class="bg-white w-full h-max py-10 px-5 rounded-[35px] max-w-[500px]">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        class="w-auto h-10 mx-auto"
        src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
        alt="oneyesinfotechsolutions"
      />
      <h2
        class="mt-10 text-2xl font-bold leading-9 tracking-tight text-center text-gray-900"
      >
        Sign in to your account
      </h2>
    </div>

    <div class="px-4 mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="space-y-6">
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Email address</label
          >
          <div class="mt-2">
            <input
              v-model="user.email"
              type="email"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
            <p v-if="errors.email" class="mt-2 text-sm text-red-500">
              {{ errors.email }}
            </p>
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              v-model="user.password"
              type="password"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            />
            <p v-if="errors.password" class="mt-2 text-sm text-red-500">
              {{ errors.password }}
            </p>
          </div>
        </div>

        <div>
          <button
            @click="login()"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Sign in
          </button>
        </div>
      </div>
      <p class="mt-5 font-bold text-indigo-600">
        <NuxtLink to="/register"> Register Here </NuxtLink>
      </p>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
      errors: {
        email: "",
        password: "",
      },
    };
  },
  mounted() {
    if (localStorage.getItem("isLoggedIn") == "true") {
      window.location.href = "/";
    }
  },
  methods: {
    login() {
      let errorsCount = 0;
      if (!this.user.email) {
        this.errors.email = "Please enter email";
        errorsCount++;
      } else {
        this.errors.email = "";
      }

      if (!this.user.password) {
        this.errors.password = "Please enter password";
        errorsCount++;
      } else {
        this.errors.password = "";
      }

      if (errorsCount > 0) {
        return;
      }

      this.$http
        .$post("/login", {
          body: {
            email: this.user.email,
            password: this.user.password,
          },
        })
        .then((res) => {
          if (res.success) {
            window.localStorage.setItem("isLoggedIn", true);
            window.localStorage.setItem("email", this.user.email);
            window.localStorage.setItem("name", res.user.name);
            window.location.href = "/";
            return;
          }
          this.errors.password = res.message;
        });
    },
  },
};
</script>
