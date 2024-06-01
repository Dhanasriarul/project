<template>
  <div>
    <div class="fixed top-0 left-0 w-full h-screen bg-black z-[99999]">
      <div class="flex flex-col justify-center min-h-full px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
          <h2
            class="text-2xl font-bold leading-9 tracking-tight text-center text-white"
          >
            Business Login
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
                  v-model="email"
                  type="email"
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
    </div>
  </div>
</template>
<script>
import Chart from "chart.js/auto";

definePageMeta({
  layout: "admin",
});

export default {
  data() {
    return {
      email: "",
    };
  },
  mounted() {
    if (localStorage.getItem("businessEmail")) {
      this.$router.push("/business/category");
    }
  },
  methods: {
    login() {
      localStorage.setItem("businessEmail", this.email);
      this.$router.push("/business/category");
    },
  },
};
</script>
