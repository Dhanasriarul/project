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
          <div class="relative">
            <div class="px-4 sm:px-6 lg:px-8">
              <div class="sm:flex sm:items-center">
                <div class="sm:flex-auto">
                  <h1 class="text-2xl font-bold leading-6 text-gray-900">
                    Categories
                  </h1>
                </div>
                <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none"></div>
              </div>
              <div v-if="addCategoryModal" class="w-full p-10 mt-5 bg-white">
                <div class="">
                  <h1 class="text-xl font-bold">Enter Category Name</h1>
                  <input
                    v-model="newCategory.name"
                    type="text"
                    class="w-full h-12 px-4 mt-3 border rounded-md"
                    placeholder="Category Name"
                  />
                </div>
                <div class="mt-3">
                  <h1 class="text-xl font-bold">Image URL</h1>
                  <input
                    v-model="newCategory.image"
                    type="text"
                    class="w-full h-12 px-4 mt-3 border rounded-md"
                    placeholder="Image URL"
                  />
                </div>

                <button
                  @click="addCategory()"
                  class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Submit
                </button>
              </div>
              <div v-if="editCategoryModal" class="w-full p-10 mt-5 bg-white">
                <div class="">
                  <h1 class="text-xl font-bold">Enter Category Name</h1>
                  <input
                    v-model="editCategory.name"
                    type="text"
                    class="w-full h-12 px-4 mt-3 border rounded-md"
                    placeholder="Category Name"
                  />
                </div>
                <div class="mt-3">
                  <h1 class="text-xl font-bold">Image URL</h1>
                  <input
                    v-model="editCategory.image"
                    type="text"
                    class="w-full h-12 px-4 mt-3 border rounded-md"
                    placeholder="Image URL"
                  />
                </div>

                <button
                  @click="editCat()"
                  class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Submit
                </button>
                <button
                  @click="
                    editCategoryModal = false;
                    editCategory = {};
                  "
                  class="block px-3 py-2 mt-3 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Close
                </button>
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
                              Name
                            </th>
                            <th
                              scope="col"
                              class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                            >
                              Image
                            </th>
                            <th
                              scope="col"
                              class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                            >
                              View Services
                            </th>
                          </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                          <tr
                            v-for="(category, index) in categories"
                            :key="index"
                          >
                            <td
                              class="py-4 pl-4 pr-3 text-sm font-medium text-gray-900 whitespace-nowrap sm:pl-6"
                            >
                              {{ index + 1 }}
                            </td>
                            <td
                              class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                            >
                              {{ category.name }}
                            </td>
                            <td
                              class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                            >
                              <img :src="category.image" class="h-20" alt="" />
                            </td>
                            <td
                              class="px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                            >
                              <NuxtLink
                                :to="`/business/category/${category.categoryId}`"
                              >
                                View Services
                              </NuxtLink>
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
      categories: [],
      sidebarIsOpen: false,
      addCategoryModal: false,
      editCategoryModal: false,
      newCategory: {
        name: "",
        image: "",
      },
      editCategory: {},
    };
  },
  mounted() {
    if (!localStorage.getItem("businessEmail")) {
      this.$router.push("/");
      return;
    }
    this.getCategories();
  },
  methods: {
    getCategories() {
      this.$http.$get("/categories").then((res) => {
        if (res.success) {
          this.categories = res.categories;
          return;
        }
        alert(res.message);
      });
    },
    addCategory() {
      this.$http
        .$post("/add-category", {
          body: this.newCategory,
        })
        .then((res) => {
          if (res.success) {
            this.getCategories();
            this.addCategoryModal = false;
            this.newCategory = {
              name: "",
              image: "",
            };
            return;
          }
          alert(res.message);
        });
    },
    editCat() {
      this.$http
        .$post("/edit-category", {
          body: this.editCategory,
        })
        .then((res) => {
          if (res.success) {
            this.getCategories();
            this.editCategoryModal = false;
            this.editCategory = {};
            return;
          }
          alert(res.message);
        });
    },
    deleteCategory(index) {
      this.$http
        .$post("/delete-category", {
          body: {
            categoryId: this.categories[index].categoryId,
          },
        })
        .then((res) => {
          if (res.success) {
            this.getCategories();
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
