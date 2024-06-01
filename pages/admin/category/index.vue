<template>
  <div class="relative">
    <div class="px-4 sm:px-6 lg:px-8">
      <div class="sm:flex sm:items-center">
        <div class="sm:flex-auto">
          <h1 class="text-2xl font-bold leading-6 text-gray-900">Categories</h1>
        </div>
        <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
          <button
            @click="addCategoryModal = !addCategoryModal"
            type="button"
            class="block px-3 py-2 text-sm font-semibold text-center text-white bg-indigo-600 rounded-md shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            {{ addCategoryModal ? "Close" : "Add Category" }}
          </button>
        </div>
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
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    ></th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="(category, index) in categories" :key="index">
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
                      <NuxtLink :to="`/admin/category/${category.categoryId}`">
                        View Services
                      </NuxtLink>
                    </td>
                    <td
                      class="flex items-center gap-3 px-3 py-4 text-sm text-gray-500 whitespace-nowrap"
                    >
                      <i
                        @click="
                          editCategory = categories[index];
                          editCategoryModal = true;
                        "
                        class="text-blue-500 fa-solid fa-pen"
                      ></i>
                      <i
                        @click="deleteCategory(index)"
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
  </div>
</template>

<script>
definePageMeta({
  layout: "admin",
});

export default {
  data() {
    return {
      categories: [],
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
  },
};
</script>
