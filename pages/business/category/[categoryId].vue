<template>
  <div>
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
                    <NuxtLink to="/business/category">
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
          <div class="sm:flex sm:items-center">
            <div class="sm:flex-auto">
              <h1 class="text-2xl font-bold leading-6 text-gray-900">
                Services
              </h1>
            </div>
            <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
              <!-- <button
                @click="addServiceModal = true"
                class="block px-3 py-2 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Add Service
              </button> -->
            </div>
          </div>
          <div class="flow-root mt-8">
            <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
              <div
                class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8"
              >
                <div
                  class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 sm:rounded-lg"
                >
                  <table class="min-w-full divide-y divide-gray-300">
                    <thead class="bg-gray-50">
                      <tr>
                        <th
                          scope="col"
                          class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6"
                        >
                          Sno
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Title
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Impresions
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Address
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          City
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Phone
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Email
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        >
                          Details
                        </th>
                        <th
                          scope="col"
                          class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                        ></th>
                      </tr>
                    </thead>
                    <tbody class="bg-white divide-y divide-gray-200">
                      <tr v-for="(service, index) in services" :key="index">
                        <td
                          class="py-4 pl-4 pr-3 text-sm font-medium text-gray-900 whitespace-nowrap sm:pl-6"
                        >
                          {{ index + 1 }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.title }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.impressions }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.address }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.city }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.phone }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          {{ service.email }}
                        </td>
                        <td
                          class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          <p @click="openGallery(service.serviceId)">
                            Manage Gallery
                          </p>
                          <p @click="openEnquiry(service.serviceId)">
                            Enquiries
                          </p>
                        </td>
                        <td
                          class="flex items-center gap-3 px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                        >
                          <i
                            @click="
                              editService = services[index];
                              editServiceModal = true;
                            "
                            class="text-blue-500 fa-solid fa-pen"
                          ></i>
                          <i
                            @click="deleteService(index)"
                            class="text-red-500 fa-regular fa-trash-can"
                          ></i>
                        </td>
                      </tr>

                      <!-- More people... -->
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div
          v-if="addServiceModal"
          class="h-screen w-[600px] p-5 bg-white shadow-2xl border fixed right-0 top-0"
        >
          <div class="flex items-center justify-between mb-10">
            <h1 class="text-xl font-bold">Add Service</h1>
            <div
              @click="addServiceModal = false"
              class="flex items-center justify-center w-10 h-10 bg-black rounded-full"
            >
              <i class="text-white fa-solid fa-xmark"></i>
            </div>
          </div>
          <div class="">
            <h1 class="text-xl font-bold">Enter Service Title</h1>
            <input
              v-model="newService.title"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Service Title"
            />
          </div>
          <div class="">
            <h1 class="text-xl font-bold">Image URL</h1>
            <input
              v-model="newService.image"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Image URL"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Address</h1>
            <input
              v-model="newService.address"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Address"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Phone Number</h1>
            <input
              v-model="newService.phone"
              type="number"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Phone Number"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Email</h1>
            <input
              v-model="newService.email"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Email"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter City</h1>
            <select
              v-model="newService.city"
              class="w-full h-12 px-4 mt-3 border rounded-md"
            >
              <option value="" disabled selected>Choose City</option>
              <option value="chennai">Chennai</option>
              <option value="mumbai">Mumbai</option>
              <option value="bangalore">Bangalore</option>
            </select>
          </div>
          <button
            @click="addService()"
            class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Submit
          </button>
        </div>

        <div
          v-if="editServiceModal"
          class="h-screen w-[600px] p-5 bg-white shadow-2xl border fixed right-0 top-0"
        >
          <div class="flex items-center justify-between mb-10">
            <h1 class="text-xl font-bold">Edit Service</h1>
            <div
              @click="editServiceModal = false"
              class="flex items-center justify-center w-10 h-10 bg-black rounded-full"
            >
              <i class="text-white fa-solid fa-xmark"></i>
            </div>
          </div>
          <div class="">
            <h1 class="text-xl font-bold">Enter Service Title</h1>
            <input
              v-model="editService.title"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Service Title"
            />
          </div>
          <div class="">
            <h1 class="text-xl font-bold">Image URL</h1>
            <input
              v-model="editService.image"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Image URL"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Address</h1>
            <input
              v-model="editService.address"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Address"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Phone Number</h1>
            <input
              v-model="editService.phone"
              type="number"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Phone Number"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter Email</h1>
            <input
              v-model="editService.email"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Email"
            />
          </div>
          <div class="mt-3">
            <h1 class="text-xl font-bold">Enter City</h1>
            <select
              v-model="editService.city"
              class="w-full h-12 px-4 mt-3 border rounded-md"
            >
              <option value="" disabled selected>Choose City</option>
              <option value="chennai">Chennai</option>
              <option value="mumbai">Mumbai</option>
              <option value="bangalore">Bangalore</option>
            </select>
          </div>
          <button
            @click="updateService()"
            class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Submit
          </button>
        </div>

        <div
          v-if="galleryModel"
          class="h-screen w-[600px] p-5 bg-white shadow-2xl border fixed right-0 top-0 overflow-auto"
        >
          <div class="flex items-center justify-between mb-10">
            <h1 class="text-xl font-bold">Manage Gallery</h1>
            <div
              @click="
                galleryModel = false;
                images = [];
                galleryModelServiceId = '';
              "
              class="flex items-center justify-center w-10 h-10 bg-black rounded-full"
            >
              <i class="text-white fa-solid fa-xmark"></i>
            </div>
          </div>
          <div class="">
            <h1 class="text-xl font-bold">Enter Image URL</h1>
            <input
              v-model="newImageUrl"
              type="text"
              class="w-full h-12 px-4 mt-3 border rounded-md"
              placeholder="Enter Image URL"
            />
          </div>
          <button
            @click="addImage()"
            class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Add
          </button>

          <div class="grid grid-cols-2 gap-3 mt-5">
            <div
              v-for="(image, index) in images"
              :key="index"
              class="relative overflow-hidden rounded-xl group"
            >
              <img :src="image.image" class="w-full" />
              <div
                @click="deleteImage(index)"
                class="absolute items-center justify-center hidden w-10 h-10 bg-red-400 rounded-full bottom-5 right-5 group-hover:flex"
              >
                <i class="text-white fa-regular fa-trash-can"></i>
              </div>
            </div>
          </div>
        </div>

        <div
          v-if="enquiriesModel"
          class="h-screen w-[600px] p-5 bg-white shadow-2xl border fixed right-0 top-0 overflow-auto"
        >
          <div class="flex items-center justify-between mb-10">
            <h1 class="text-xl font-bold">Enquiries</h1>
            <div
              @click="
                enquiriesModel = false;
                enquiries = [];
              "
              class="flex items-center justify-center w-10 h-10 bg-black rounded-full"
            >
              <i class="text-white fa-solid fa-xmark"></i>
            </div>
          </div>

          <div class="grid gap-3 mt-5">
            <div
              v-for="(enquiry, index) in enquiries"
              :key="index"
              class="relative p-3 overflow-hidden border rounded-xl"
            >
              <p>Name: {{ enquiry.name }}</p>
              <p>Email: {{ enquiry.email }}</p>
              <p>Phone: {{ enquiry.phone }}</p>
              <p>Message: {{ enquiry.message }}</p>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      services: [],
      sidebarIsOpen: false,
      categoryId: this.$route.params.categoryId,
      addServiceModal: false,
      editServiceModal: false,
      galleryModel: false,
      enquiriesModel: false,
      galleryModelServiceId: "",
      newService: {
        image: "",
        title: "",
        address: "",
        phone: "",
        city: "",
        email: "",
      },
      editService: {},
      newImageUrl: "",
      images: [],
      enquiries: [],
    };
  },
  mounted() {
    if (!localStorage.getItem("businessEmail")) {
      this.$router.push("/");
      return;
    }
    this.getServices();
  },
  methods: {
    getServices() {
      this.$http.$get(`/services?categoryId=${this.categoryId}`).then((res) => {
        if (res.success) {
          let services = res.services;

          let email = localStorage.getItem("businessEmail");

          this.services = services.filter((service) => {
            return service.email === email;
          });
          return;
        }
        alert(res.message);
      });
    },
    addService() {
      this.$http
        .$post(`/add-service`, {
          body: {
            categoryId: this.categoryId,
            ...this.newService,
          },
        })
        .then((res) => {
          if (res.success) {
            this.getServices();
            this.addServiceModal = false;
            this.newService = {
              image: "",
              title: "",
              address: "",
              phone: "",
              city: "",
              email: "",
            };
            return;
          }
          alert(res.message);
        });
    },
    updateService() {
      this.$http
        .$post(`/edit-service`, {
          body: {
            ...this.editService,
          },
        })
        .then((res) => {
          if (res.success) {
            this.getServices();
            this.editServiceModal = false;
            this.editService = {};
            return;
          }
          alert(res.message);
        });
    },
    deleteService(index) {
      this.$http
        .$post(`/delete-service`, {
          body: {
            serviceId: this.services[index].serviceId,
          },
        })
        .then((res) => {
          if (res.success) {
            this.getServices();
            return;
          }
          alert(res.message);
        });
    },
    openGallery(serviceId) {
      this.galleryModelServiceId = serviceId;
      this.$http.$get(`/get-images?serviceId=${serviceId}`).then((res) => {
        if (res.success) {
          this.images = res.images;
          this.galleryModel = true;
          return;
        }
        alert(res.message);
      });
    },
    openEnquiry(serviceId) {
      this.$http.$get(`/enquiries?serviceId=${serviceId}`).then((res) => {
        if (res.success) {
          this.enquiries = res.enquiries;
          this.enquiriesModel = true;
          return;
        }
        alert(res.message);
      });
    },
    addImage() {
      this.$http
        .$post(`/add-image`, {
          body: {
            serviceId: this.galleryModelServiceId,
            image: this.newImageUrl,
          },
        })
        .then((res) => {
          if (res.success) {
            this.openGallery(this.galleryModelServiceId);
            this.newImageUrl = "";
            return;
          }
          alert(res.message);
        });
    },
    deleteImage(index) {
      this.$http
        .$post(`/delete-image`, {
          body: {
            galleryId: this.images[index].galleryId,
          },
        })
        .then((res) => {
          if (res.success) {
            this.openGallery(this.galleryModelServiceId);
            return;
          }
          alert(res.message);
        });
    },
    logout() {
      localStorage.removeItem("businessEmail");
      this.$router.push("/");
    },
  },
};
</script>
