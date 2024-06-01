<template>
  <div>
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="sm:flex sm:items-center">
        <div class="sm:flex-auto">
          <h1 class="text-2xl font-bold leading-6 text-gray-900">Services</h1>
        </div>
        <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
          <button
            @click="addServiceModal = true"
            class="block px-3 py-2 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Add Service
          </button>
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
                      <p @click="openEnquiry(service.serviceId)">Enquiries</p>
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
  </div>
</template>

<script>
definePageMeta({
  layout: "admin",
});

export default {
  data() {
    return {
      services: [],
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
    this.getServices();
  },
  methods: {
    getServices() {
      this.$http.$get(`/services?categoryId=${this.categoryId}`).then((res) => {
        if (res.success) {
          this.services = res.services;
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
  },
};
</script>
