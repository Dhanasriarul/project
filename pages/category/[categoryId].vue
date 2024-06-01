<template>
  <div>
    <NavBar />

    <!-- Shops -->
    <div class="px-2 bg-white md:px-10">
      <div class="px-4 py-16 mx-auto max-w-7xl sm:px-6 sm:py-24 lg:px-0">
        <h1
          class="text-3xl font-bold tracking-tight text-center text-gray-900 sm:text-4xl"
        >
          <span class="block">{{ serviceName }}</span>
        </h1>

        <div class="flex items-center justify-between w-full mt-5">
          <input
            v-model="filters.keyword"
            type="text"
            placeholder="Search"
            class="px-3 py-1 border outline-none rounded-xl"
            @keyup="getServices()"
          />
          <div
            @click="filtersIsOpen = !filtersIsOpen"
            class="flex items-center justify-center w-10 h-10 border rounded-full"
          >
            <i class="fa-solid fa-filter text-black/40"></i>
          </div>
        </div>
        <div
          v-if="filtersIsOpen"
          class="flex gap-4 p-3 mt-2 bg-gray-200 rounded-xl"
        >
          <select
            v-model="filters.sort"
            @change="getServices()"
            class="px-3 py-1 bg-white rounded-md"
          >
            <option value="" disabled selected>Sort</option>
            <option value="asc">Impressions Low to High</option>
            <option value="desc">Impressions High to Low</option>
          </select>
          <select
            v-model="filters.rating"
            @change="getServices()"
            class="px-3 py-1 bg-white rounded-md"
          >
            <option value="" disabled selected>Rating</option>
            <option value="">All</option>
            <option value="5">5 Star</option>
            <option value="4">4+ Star</option>
            <option value="3">3+ Star</option>
            <option value="2">2+ Star</option>
            <option value="1">1+ Star</option>
          </select>
          <select
            v-model="filters.city"
            @change="getServices()"
            class="px-3 py-1 bg-white rounded-md"
          >
            <option value="" disabled selected>Location</option>
            <option value="">All</option>
            <option value="chennai">Chennai</option>
            <option value="mumbai">Mumbai</option>
            <option value="bangalore">Bangalore</option>
          </select>
          <button
            @click="
              filters.city = '';
              filters.keyword = '';
              filters.rating = '';
              filters.sort = '';
              getServices();
            "
            class="px-3 py-1 bg-white rounded-md"
          >
            Clear filters
          </button>
        </div>

        <div class="mt-12">
          <section aria-labelledby="cart-heading">
            <ul
              role="list"
              class="border-t border-b border-gray-200 divide-y divide-gray-200"
            >
              <li
                v-for="(service, index) in services"
                :key="index"
                class="py-6"
              >
                <div class="md:flex justify-between items-center">
                  <div class="md:flex">
                    <NuxtLink :to="`service/${service.serviceId}`">
                    <div class="flex-shrink-0">
                      <img
                        :src="service.image"
                        class="object-cover object-center w-full h-auto rounded-md md:w-32 md:h-32"
                      />
                    </div>
                  </NuxtLink>

                  <div class="flex flex-col flex-1 mt-4 ml-4 sm:ml-6 md:mt-0">
                    <div class="flex flex-col justify-between h-full">
                      <div>
                        <p
                        class="text-lg font-medium text-gray-700 hover:text-gray-800"
                      >
                        <NuxtLink :to="`service/${service.serviceId}`">
                          {{ service.title }}
                        </NuxtLink>
                      </p>
                      
                      <div class="flex items-center gap-2 mt-3 text-gray-500">
                        <p>{{ service.address }}</p>
                      </div>
                      </div>
                      <div class="flex items-center gap-3 mt-3">
                        <a :href="`tel:${service.phone}`">
                          <button
                            class="flex items-center justify-center gap-2 px-3 py-1 text-white bg-blue-500 rounded-lg"
                          >
                            <i class="fa-solid fa-phone"></i>
                            <span class="font-bold">{{ service.phone }}</span>
                          </button>
                        </a>
                        <a
                          :href="`https://wa.me/91${service.phone}`"
                          target="_blank"
                        >
                          <button
                            class="flex items-center justify-center gap-2 px-3 py-1 text-white bg-green-500 rounded-lg"
                          >
                            <i class="fa-brands fa-whatsapp"></i>
                            <span class="font-bold">Chat</span>
                          </button>
                        </a>
                      </div>
                    </div>
                  </div>
                  </div>
                  <div>
                    <div class="flex items-center gap-2 mt-4">
                        <i
                          class="fa-solid fa-star"
                          :class="
                            service.rating >= 1
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            service.rating >= 2
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            service.rating >= 3
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            service.rating >= 4
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            service.rating >= 5
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <div
                          class="px-2 py-1 font-medium bg-gray-300 rounded-lg"
                        >
                          {{ service.reviewsCount }} reviews
                        </div>
                      </div>
                      <div class="flex items-center gap-2 mt-3 text-gray-500">
                        <i class="fa-solid fa-eye"></i>
                        <p>{{ service.impressions }} Impressions</p>
                      </div>
                  </div>
                </div>
              </li>

              <!-- More products... -->
            </ul>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categoryId: this.$route.params.categoryId,
      services: [],
      filtersIsOpen: false,
      serviceName: this.$route.query.name || "Service",
      filters: {
        keyword: "",
        city: "",
        rating: "",
        sort: "desc",
      },
    };
  },
  mounted() {
    if (!this.categoryId) {
      this.$router.push("/");
      return;
    }

    this.getServices();
  },
  methods: {
    getServices() {
      this.$http
        .$get(
          `/services?categoryId=${this.categoryId}&keyword=${this.filters.keyword}&city=${this.filters.city}&sort=${this.filters.sort}&rating=${this.filters.rating}`
        )
        .then((res) => {
          if (res.success) {
            this.services = res.services;
            return;
          }
          alert(res.message);
        });
    },
  },
};
</script>
