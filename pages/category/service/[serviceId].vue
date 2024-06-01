<template>
  <div>
    <NavBar />

    <!-- Shops -->
    <div class="px-2 bg-white md:px-10">
      <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-0">
        <h1
          class="text-3xl font-bold tracking-tight text-center text-gray-900 sm:text-4xl"
        >
          <span class="block">Service Details</span>
        </h1>
        <div class="mt-12">
          <section aria-labelledby="cart-heading">
            <ul
              role="list"
              class="border-t border-b border-gray-200 divide-y divide-gray-200"
            >
              <li class="py-6">
                <div class="md:flex">
                  <div class="flex-shrink-0">
                    <img
                      :src="serviceData.image"
                      class="object-cover object-center w-full h-auto rounded-md md:w-52 md:h-52"
                    />
                  </div>

                  <div class="flex flex-col flex-1 mt-4 ml-4 sm:ml-6 md:mt-0">
                    <div>
                      <p
                        class="text-lg font-medium text-gray-700 hover:text-gray-800"
                      >
                        {{ serviceData.title }}
                      </p>
                      <div class="flex items-center gap-2 mt-4">
                        <i
                          class="fa-solid fa-star"
                          :class="
                            serviceData.rating >= 1
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            serviceData.rating >= 2
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            serviceData.rating >= 3
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            serviceData.rating >= 4
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <i
                          class="fa-solid fa-star"
                          :class="
                            serviceData.rating >= 5
                              ? 'text-yellow-400'
                              : 'text-gray-400'
                          "
                        ></i>
                        <div
                          class="px-2 py-1 font-medium bg-gray-300 rounded-lg"
                        >
                          {{ serviceData.reviewsCount }} reviews
                        </div>
                      </div>
                      <div class="flex items-center gap-2 mt-3 text-gray-500">
                        <i class="fa-solid fa-eye"></i>
                        <p>{{ serviceData.impressions }} Impressions</p>
                      </div>
                      <div class="flex items-center gap-2 mt-3 text-gray-500">
                        <p>{{ serviceData.address }}</p>
                      </div>
                      <div class="flex items-center gap-3 mt-3">
                        <a :href="`tel:${serviceData.phone}`">
                          <button
                            class="flex items-center justify-center gap-2 px-3 py-1 text-white bg-blue-500 rounded-lg"
                          >
                            <i class="fa-solid fa-phone"></i>
                            <span class="font-bold">{{
                              serviceData.phone
                            }}</span>
                          </button>
                        </a>
                        <a
                          :href="`https://wa.me/91${serviceData.phone}`"
                          target="_blank"
                        >
                          <button
                            class="flex items-center justify-center gap-2 px-3 py-1 text-white bg-green-500 rounded-lg"
                          >
                            <i class="fa-brands fa-whatsapp"></i>
                            <span class="font-bold">Chat</span>
                          </button>
                        </a>
                        <button
                          @click="enquiryIsOpen = true"
                          class="flex items-center justify-center gap-2 px-3 py-1 text-white bg-orange-400 rounded-lg"
                        >
                          <i class="fa-solid fa-calendar-days"></i>
                          <span class="font-bold">Enquiry</span>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </li>

              <!-- More products... -->
            </ul>
          </section>
        </div>

        <h1
          class="mt-5 text-3xl font-bold tracking-tight text-center text-gray-900 sm:text-4xl"
        >
          <span class="block">Gallery</span>
        </h1>
        <div class="grid gap-5 mt-5 lg:grid-cols-3">
          <div
            v-for="(image, index) in gallery"
            :key="index"
            class="w-full overflow-hidden rounded-xl"
          >
            <img :src="image.image" class="w-full" alt="" />
          </div>
        </div>

        <h1
          class="mt-5 text-3xl font-bold tracking-tight text-center text-gray-900 sm:text-4xl"
        >
          <span class="block">Reviews</span>
        </h1>

        <div class="bg-white">
          <div
            class="max-w-2xl px-4 py-10 mx-auto sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-12 lg:gap-x-8 lg:px-8"
          >
            <div class="lg:col-span-4">
              <h2 class="text-2xl font-bold tracking-tight text-gray-900">
                Customer Reviews
              </h2>

              <div class="flex items-center mt-3">
                <div>
                  <div class="flex items-center">
                    <!-- Active: "text-yellow-400", Default: "text-gray-300" -->
                    <i
                      class="fa-solid fa-star"
                      :class="
                        serviceData.rating >= 1
                          ? 'text-yellow-400'
                          : 'text-gray-400'
                      "
                    ></i>
                    <i
                      class="fa-solid fa-star"
                      :class="
                        serviceData.rating >= 2
                          ? 'text-yellow-400'
                          : 'text-gray-400'
                      "
                    ></i>
                    <i
                      class="fa-solid fa-star"
                      :class="
                        serviceData.rating >= 3
                          ? 'text-yellow-400'
                          : 'text-gray-400'
                      "
                    ></i>
                    <i
                      class="fa-solid fa-star"
                      :class="
                        serviceData.rating >= 4
                          ? 'text-yellow-400'
                          : 'text-gray-400'
                      "
                    ></i>
                    <i
                      class="fa-solid fa-star"
                      :class="
                        serviceData.rating >= 5
                          ? 'text-yellow-400'
                          : 'text-gray-400'
                      "
                    ></i>
                  </div>
                </div>
                <p class="ml-2 text-sm text-gray-900">
                  Based on {{ serviceData.reviewsCount }} reviews
                </p>
              </div>

              <div class="mt-6">
                <h3 class="sr-only">Review data</h3>
                <dl class="space-y-3">
                  <div
                    v-if="serviceData.stars"
                    class="flex items-center text-sm"
                  >
                    <dt class="flex items-center flex-1">
                      <p class="w-3 font-medium text-gray-900">
                        5<span class="sr-only"> star reviews</span>
                      </p>
                      <div
                        aria-hidden="true"
                        class="flex items-center flex-1 ml-1"
                      >
                        <i class="text-yellow-400 fa-solid fa-star"></i>

                        <div class="relative flex-1 ml-3">
                          <div
                            class="h-3 bg-gray-100 border border-gray-200 rounded-full"
                          ></div>
                          <div
                            :style="`width: ${serviceData.stars.fiveStars}%`"
                            class="absolute inset-y-0 bg-yellow-400 border border-yellow-400 rounded-full"
                          ></div>
                        </div>
                      </div>
                    </dt>
                    <dd
                      class="w-10 ml-3 text-sm text-right text-gray-900 tabular-nums"
                    >
                      {{ serviceData.stars.fiveStars }}%
                    </dd>
                  </div>
                  <div
                    v-if="serviceData.stars"
                    class="flex items-center text-sm"
                  >
                    <dt class="flex items-center flex-1">
                      <p class="w-3 font-medium text-gray-900">
                        4<span class="sr-only"> star reviews</span>
                      </p>
                      <div
                        aria-hidden="true"
                        class="flex items-center flex-1 ml-1"
                      >
                        <i class="text-yellow-400 fa-solid fa-star"></i>

                        <div class="relative flex-1 ml-3">
                          <div
                            class="h-3 bg-gray-100 border border-gray-200 rounded-full"
                          ></div>
                          <div
                            :style="`width: ${serviceData.stars.fourStars}%`"
                            class="absolute inset-y-0 bg-yellow-400 border border-yellow-400 rounded-full"
                          ></div>
                        </div>
                      </div>
                    </dt>
                    <dd
                      class="w-10 ml-3 text-sm text-right text-gray-900 tabular-nums"
                    >
                      {{ serviceData.stars.fourStars }}%
                    </dd>
                  </div>
                  <div
                    v-if="serviceData.stars"
                    class="flex items-center text-sm"
                  >
                    <dt class="flex items-center flex-1">
                      <p class="w-3 font-medium text-gray-900">
                        3<span class="sr-only"> star reviews</span>
                      </p>
                      <div
                        aria-hidden="true"
                        class="flex items-center flex-1 ml-1"
                      >
                        <i class="text-yellow-400 fa-solid fa-star"></i>

                        <div class="relative flex-1 ml-3">
                          <div
                            class="h-3 bg-gray-100 border border-gray-200 rounded-full"
                          ></div>
                          <div
                            :style="`width: ${serviceData.stars.threeStars}%`"
                            class="absolute inset-y-0 bg-yellow-400 border border-yellow-400 rounded-full"
                          ></div>
                        </div>
                      </div>
                    </dt>
                    <dd
                      class="w-10 ml-3 text-sm text-right text-gray-900 tabular-nums"
                    >
                      {{ serviceData.stars.threeStars }}%
                    </dd>
                  </div>
                  <div
                    v-if="serviceData.stars"
                    class="flex items-center text-sm"
                  >
                    <dt class="flex items-center flex-1">
                      <p class="w-3 font-medium text-gray-900">
                        2<span class="sr-only"> star reviews</span>
                      </p>
                      <div
                        aria-hidden="true"
                        class="flex items-center flex-1 ml-1"
                      >
                        <i class="text-yellow-400 fa-solid fa-star"></i>

                        <div class="relative flex-1 ml-3">
                          <div
                            class="h-3 bg-gray-100 border border-gray-200 rounded-full"
                          ></div>
                          <div
                            :style="`width: ${serviceData.stars.twoStars}%`"
                            class="absolute inset-y-0 bg-yellow-400 border border-yellow-400 rounded-full"
                          ></div>
                        </div>
                      </div>
                    </dt>
                    <dd
                      class="w-10 ml-3 text-sm text-right text-gray-900 tabular-nums"
                    >
                      {{ serviceData.stars.twoStars }}%
                    </dd>
                  </div>
                  <div
                    v-if="serviceData.stars"
                    class="flex items-center text-sm"
                  >
                    <dt class="flex items-center flex-1">
                      <p class="w-3 font-medium text-gray-900">
                        1<span class="sr-only"> star reviews</span>
                      </p>
                      <div
                        aria-hidden="true"
                        class="flex items-center flex-1 ml-1"
                      >
                        <i class="text-yellow-400 fa-solid fa-star"></i>

                        <div class="relative flex-1 ml-3">
                          <div
                            class="h-3 bg-gray-100 border border-gray-200 rounded-full"
                          ></div>
                          <div
                            class="absolute inset-y-0 bg-yellow-400 border border-yellow-400 rounded-full"
                            :style="`width: ${serviceData.stars.oneStars}%`"
                          ></div>
                        </div>
                      </div>
                    </dt>
                    <dd
                      class="w-10 ml-3 text-sm text-right text-gray-900 tabular-nums"
                    >
                      {{ serviceData.stars.oneStars }}%
                    </dd>
                  </div>
                </dl>
              </div>

              <div class="mt-10">
                <h3 class="text-lg font-medium text-gray-900">
                  Share your thoughts
                </h3>
                <p class="mt-1 text-sm text-gray-600">
                  If you’ve used this product, share your thoughts with other
                  customers
                </p>

                <p
                  @click="reviewIsOpen = !reviewIsOpen"
                  class="inline-flex items-center justify-center w-full px-8 py-2 mt-6 text-sm font-medium text-gray-900 bg-white border border-gray-300 rounded-md hover:bg-gray-50 sm:w-auto lg:w-full"
                >
                  {{ reviewIsOpen ? "Close" : "Write a review" }}
                </p>

                <div v-if="reviewIsOpen" class="mt-5">
                  <div class="mb-3">
                    <h3 class="font-bold">Name</h3>
                    <input
                      v-model="newReview.name"
                      type="text"
                      class="w-full h-12 px-3 mt-2 border border-black/30 rounded-xl"
                      placeholder="Name"
                    />
                  </div>

                  <div class="mb-3">
                    <h3 class="font-bold">Stars</h3>
                    <div class="flex items-center gap-3">
                      <i
                        @click="newReview.stars = 1"
                        class="text-xl fa-solid fa-star"
                        :class="
                          newReview.stars >= 1
                            ? 'text-yellow-400'
                            : 'text-gray-400'
                        "
                      ></i>
                      <i
                        @click="newReview.stars = 2"
                        class="text-xl fa-solid fa-star"
                        :class="
                          newReview.stars >= 2
                            ? 'text-yellow-400'
                            : 'text-gray-400'
                        "
                      ></i>
                      <i
                        @click="newReview.stars = 3"
                        class="text-xl fa-solid fa-star"
                        :class="
                          newReview.stars >= 3
                            ? 'text-yellow-400'
                            : 'text-gray-400'
                        "
                      ></i>
                      <i
                        @click="newReview.stars = 4"
                        class="text-xl fa-solid fa-star"
                        :class="
                          newReview.stars >= 4
                            ? 'text-yellow-400'
                            : 'text-gray-400'
                        "
                      ></i>
                      <i
                        @click="newReview.stars = 5"
                        class="text-xl fa-solid fa-star"
                        :class="
                          newReview.stars >= 5
                            ? 'text-yellow-400'
                            : 'text-gray-400'
                        "
                      ></i>
                    </div>
                  </div>

                  <div>
                    <h3 class="font-bold">Message</h3>
                    <textarea
                      v-model="newReview.message"
                      rows="5"
                      placeholder="Message"
                      class="w-full p-3 mt-2 border border-black/30 rounded-xl"
                    ></textarea>
                  </div>

                  <button
                    @click="submitReview()"
                    class="w-full px-3 py-2 mt-5 font-bold text-white bg-blue-500 rounded-lg"
                  >
                    Submit
                  </button>
                </div>
              </div>
            </div>

            <div class="mt-16 lg:col-span-7 lg:col-start-6 lg:mt-0">
              <h3 class="sr-only">Recent reviews</h3>

              <div class="flow-root">
                <div class="-my-12 divide-y divide-gray-200">
                  <div
                    v-for="(review, index) in serviceData.reviews"
                    :key="index"
                    class="py-12"
                  >
                    <div class="flex items-center">
                      <!-- <img
                        src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80"
                        alt="Emily Selman."
                        class="w-12 h-12 rounded-full"
                      /> -->
                      <div class="">
                        <h4 class="mb-2 text-sm font-bold text-gray-900">
                          {{ review.name }}
                        </h4>
                        <div class="flex items-center">
                          <!-- Active: "text-yellow-400", Default: "text-gray-300" -->
                          <i
                            class="fa-solid fa-star"
                            :class="
                              review.rating >= 1
                                ? 'text-yellow-400'
                                : 'text-gray-400'
                            "
                          ></i>
                          <i
                            class="fa-solid fa-star"
                            :class="
                              review.rating >= 2
                                ? 'text-yellow-400'
                                : 'text-gray-400'
                            "
                          ></i>
                          <i
                            class="fa-solid fa-star"
                            :class="
                              review.rating >= 3
                                ? 'text-yellow-400'
                                : 'text-gray-400'
                            "
                          ></i>
                          <i
                            class="fa-solid fa-star"
                            :class="
                              review.rating >= 4
                                ? 'text-yellow-400'
                                : 'text-gray-400'
                            "
                          ></i>
                          <i
                            class="fa-solid fa-star"
                            :class="
                              review.rating >= 5
                                ? 'text-yellow-400'
                                : 'text-gray-400'
                            "
                          ></i>
                        </div>
                      </div>
                    </div>

                    <div class="mt-4 space-y-6 text-base italic text-gray-600">
                      <p>
                        {{ review.message }}
                      </p>
                    </div>
                  </div>

                  <!-- More reviews... -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      v-if="enquiryIsOpen"
      class="fixed top-0 left-0 w-full flex justify-center items-center h-screen bg-black/40 z-[99999]"
    >
      <div class="max-h-[90%] h-fit w-[60%] bg-white rounded-xl p-5">
        <div class="flex items-center justify-between">
          <h1 class="text-xl font-bold">Enquire</h1>
          <div
            @click="
              enquiryIsOpen = false;
              enquiry = {
                name: '',
                email: '',
                phone: '',
                message: '',
              };
            "
            class="flex items-center justify-center w-10 h-10 border rounded-full"
          >
            <i class="fa-solid fa-xmark"></i>
          </div>
        </div>
        <div class="w-full mt-5">
          <div class="mb-5">
            <h1 class="mb-2 font-medium">Name</h1>
            <input
              v-model="enquiry.name"
              type="text"
              placeholder="Enter name"
              class="w-full h-10 px-3 border"
            />
          </div>
          <div class="mb-5">
            <h1 class="mb-2 font-medium">Email</h1>
            <input
              v-model="enquiry.email"
              type="text"
              placeholder="Enter email"
              class="w-full h-10 px-3 border"
            />
          </div>
          <div class="mb-5">
            <h1 class="mb-2 font-medium">Phone</h1>
            <input
              v-model="enquiry.phone"
              type="text"
              placeholder="Enter phone"
              class="w-full h-10 px-3 border"
            />
          </div>
          <div class="mb-5">
            <h1 class="mb-2 font-medium">Message</h1>
            <textarea
              v-model="enquiry.message"
              placeholder="Enter your message"
              class="w-full p-3 border"
            ></textarea>
          </div>
          <button
            @click="addEnquiry()"
            class="w-full h-10 px-3 font-bold text-white bg-indigo-600"
          >
            Submit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      serviceId: this.$route.params.serviceId,
      serviceData: {},
      reviewIsOpen: false,
      newReview: {
        name: "",
        stars: 5,
        message: "",
      },
      enquiryIsOpen: false,
      enquiry: {
        name: "",
        email: "",
        phone: "",
        message: "",
      },
      gallery: [],
    };
  },
  mounted() {
    if (!this.serviceId) {
      this.$router.push("/");
      return;
    }

    this.$http
      .$post(`/add-impression`, {
        body: {
          serviceId: this.serviceId,
        },
      })
      .then((res) => {
        if (res.success) {
          return;
        }
        alert(res.message);
      });

    this.getService();
    this.getGallery();
  },
  methods: {
    getService() {
      this.$http.$get(`/service?serviceId=${this.serviceId}`).then((res) => {
        if (res.success) {
          this.serviceData = res.service;
          return;
        }
        alert(res.message);
      });
    },
    getGallery() {
      this.$http.$get(`/get-images?serviceId=${this.serviceId}`).then((res) => {
        if (res.success) {
          this.gallery = res.images;
          return;
        }
        alert(res.message);
      });
    },
    submitReview() {
      if (!this.newReview.name) {
        alert("Please enter name");
        return;
      }
      if (!this.newReview.message) {
        alert("Please enter message");
        return;
      }

      this.$http
        .$post(`/add-review`, {
          body: {
            serviceId: this.serviceId,
            name: this.newReview.name,
            rating: this.newReview.stars,
            message: this.newReview.message,
          },
        })
        .then((res) => {
          if (res.success) {
            this.getService();
            this.reviewIsOpen = false;
            this.newReview = {
              name: "",
              stars: 5,
              message: "",
            };
            return;
          }
          alert(res.message);
        });
    },
    addEnquiry() {
      if (!this.enquiry.name) {
        alert("Please enter name");
        return;
      }
      if (!this.enquiry.email) {
        alert("Please enter email");
        return;
      }
      if (!this.enquiry.phone) {
        alert("Please enter phone");
        return;
      }
      if (!this.enquiry.message) {
        alert("Please enter message");
        return;
      }

      this.$http
        .$post(`/add-enquiry`, {
          body: {
            serviceId: this.serviceId,
            name: this.enquiry.name,
            email: this.enquiry.email,
            phone: this.enquiry.phone,
            message: this.enquiry.message,
            toEmail: this.serviceData.email,
            messageTemplate: `<html>
<head>
    <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <p>You got a new enquiry.</p>
        <p>Name: ${this.enquiry.name}</p>
        <p>Email: ${this.enquiry.email}</p>
        <p>Phone: ${this.enquiry.phone}</p>
        <p>Message: ${this.enquiry.message}</p>
        <p>Warm regards,<br>XXXX<br>HR<br>OneYes Infotech Solutions<br>9875321345</p>
        <img src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png" style="width: 150px;">
    </div>
</body>
</html>`,
          },
        })
        .then((res) => {
          if (res.success) {
            this.enquiryIsOpen = false;
            this.enquiry = {
              name: "",
              email: "",
              phone: "",
              message: "",
            };
            return;
          }
          alert(res.message);
        });
    },
  },
};
</script>
