<template>
  <div class="flex flex-col justify-center items-center min-h-screen px-6 py-12 lg:px-8 bg-[url('https://images.unsplash.com/photo-1496917756835-20cb06e75b4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1908&q=80')]">
    <div class="bg-white w-full h-max py-10 px-5 rounded-[35px] max-w-[500px]">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="w-auto h-10 mx-auto" src="https://oneyesinfotechsolutions.com/img/oneyes%20logo.png"
        alt="oneyesinfotechsolutions" />
      <h2 class="mt-10 text-2xl font-bold leading-9 tracking-tight text-center text-gray-900">
        Create a account
      </h2>
    </div>

    <div class="px-4 mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
          <div class="mt-2">
            <input id="nameInput" type="text" @keyup="formatname()"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <p v-if="errors.name" class="mt-2 text-sm text-red-500">
              {{ errors.name }}
            </p>
          </div>
        </div>

        <div>
          <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
          <div class="mt-2">
            <input v-model="user.email" type="email"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <p v-if="errors.email" class="mt-2 text-sm text-red-500">
              {{ errors.email }}
            </p>
          </div>
        </div>

        <div>
          <label for="phone" class="block text-sm font-medium leading-6 text-gray-900">Phone</label>
          <div class="mt-2">
            <input v-model="user.phone" type="number"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <p v-if="errors.phone" class="mt-2 text-sm text-red-500">
              {{ errors.phone }}
            </p>
          </div>
        </div>

        <div>
          <label for="dob" class="block text-sm font-medium leading-6 text-gray-900">Date of birth</label>
          <div class="mt-2">
            <input v-model="user.dob" type="date" :max="getMaxDate()" :min="getMinDate()"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <p v-if="errors.dob" class="mt-2 text-sm text-red-500">
              {{ errors.dob }}
            </p>
          </div>
        </div>

        <div>
          <label for="gender" class="block text-sm font-medium leading-6 text-gray-900">Gender</label>
          <div class="mt-2">
            <select v-model="user.gender"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
              <option value="" selected disabled>Choose gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
            <p v-if="errors.gender" class="mt-2 text-sm text-red-500">
              {{ errors.gender }}
            </p>
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
          </div>
          <div class="mt-2">
            <input v-model="user.password" type="password"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            <p v-if="errors.password" class="mt-2 text-sm text-red-500">
              {{ errors.password }}
            </p>
          </div>
        </div>

        <div>
          <button @click="register()"
            class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            Register
          </button>
        </div>
      </div>
      <p class="mt-5 font-bold text-indigo-600">
        <NuxtLink to="/login"> Login </NuxtLink>
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
        name: "",
        email: "",
        password: "",
        dob: "",
        phone: "",
        gender: "",
      },
      errors: {
        name: "",
        email: "",
        password: "",
        dob: "",
        phone: "",
        gender: "",
      },
    };
  },
  mounted() {
    if (localStorage.getItem("isLoggedIn") == "true") {
      window.location.href = "/";
    }
  },
  methods: {
    formatname() {
      let name = document.getElementById("nameInput");

      name.addEventListener("input", function () {
        let nameValue = name.value;

        let pattern = /^[A-Za-z ]*$/;

        if (!pattern.test(nameValue)) {
          name.value = nameValue.replace(/[^A-Za-z\s]/g, "");
          this.user.name = nameValue.replace(/[^A-Za-z\s]/g, "");
        }
      });

      this.setName();
    },
    setName() {
      let name = document.getElementById("nameInput");
      this.user.name = name.value;
    },
    getMaxDate() {
      // Max date is yesterday
      let date = new Date();
      date.setDate(date.getDate() - 1);

      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (month < 10) {
        month = "0" + month;
      }

      if (day < 10) {
        day = "0" + day;
      }

      return date.getFullYear() + "-" + month + "-" + day;
    },
    getMinDate() {
      // Min date is 100 years ago
      let date = new Date();
      date.setFullYear(date.getFullYear() - 100);

      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (month < 10) {
        month = "0" + month;
      }

      if (day < 10) {
        day = "0" + day;
      }

      return date.getFullYear() + "-" + month + "-" + day;
    },
    isValidIndianPhoneNumber(input) {
      // Regular expression to match Indian phone numbers
      var regex = /^[789]\d{9}$/;
      return regex.test(input);
    },
    register() {
      // if (!this.user.name) {
      //   alert("Please enter name");
      //   return;
      // }
      // if (!this.user.email) {
      //   alert("Please enter email");
      //   return;
      // }
      // if (!this.user.password) {
      //   alert("Please enter password");
      //   return;
      // }

      let errorsCount = 0;

      if (!this.user.name) {
        this.errors.name = "Please enter name";
        errorsCount++;
      } else {
        this.errors.name = "";
      }

      function validateName(name) {
        for (let i = 0; i < name.length - 2; i++) {
          if (name[i] === name[i + 1] && name[i] === name[i + 2]) {
            return false;
          }
        }
        return true;
      }

      if (!validateName(this.user.name)) {
        this.errors.name = "Invalid name. Cannot have the same character repeated three times consecutively.";
        errorsCount++;
      } else {
        this.errors.name = "";
      }

      if (!this.user.email) {
        this.errors.email = "Please enter email";
        errorsCount++;
      } else {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(this.user.email)) {
          this.errors.email = "Please enter valid email";
          errorsCount++;
        } else {
          this.errors.email = "";
        }
      }

      function validateEmail(email) {
        // Define the regular expression pattern
        var pattern = /^[a-zA-Z0-9]/;

        // Test if the first character matches the pattern
        return pattern.test(email);
      }

      if (!validateEmail(this.user.email)) {
        this.errors.email = "Email must start with (a-z) or (0-9)";
        errorsCount++;
      }else{
        this.errors.email = "";
      }

      if (!this.user.password) {
        this.errors.password = "Please enter password";
        errorsCount++;
      } else {
        if (Number(this.user.password.length) < 8) {
          this.errors.password = "Password must be atleast 8 characters";
          errorsCount++;
        } else {
          const regexPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*[\W_]{2,})(?=.*[\W_])[a-zA-Z\d\W_]{8,}$/;

          if (!regexPattern.test(this.user.password)) {
            this.errors.password =
              "Password must contain at least one uppercase letter, one lowercase letter, one digit, at least one special character (not more than 4 consecutive), and be at least 8 characters long.";
            return;
          }
          // check password contains atleast one number
          // if (!/\d/.test(this.user.password)) {
          //   this.errors.password = "Password must contain atleast one number";
          //   return;
          // } else {
          // // check password contains atleast one uppercase
          // if (!/[A-Z]/.test(this.user.password)) {
          //   this.errors.password =
          //     "Password must contain atleast one uppercase";
          //   return;
          // } else {
          //   // check password contains atleast one lowercase
          //   if (!/[a-z]/.test(this.user.password)) {
          //     this.errors.password =
          //       "Password must contain atleast one lowercase";
          //     return;
          //   } else {
          //     // check password contains atleast one special character
          //     if (
          //       !/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(
          //         this.user.password
          //       )
          //     ) {
          //       this.errors.password =
          //         "Password must contain atleast one special character";
          //       return;
          //     } else {
          //       this.errors.password = "";
          //     }
          //   }
          // }


          // }
        }
      }

      if (!this.user.dob) {
        this.errors.dob = "Please enter date of birth";
        errorsCount++;
      } else {
        this.errors.dob = "";
      }

      if (!this.user.phone) {
        this.errors.phone = "Please enter phone";
        errorsCount++;
      } else {
        if (this.user.phone.toString().length != 10) {
          this.errors.phone = "Phone number should be 10 digits";
          errorsCount++;
        } else {
          if (!this.isValidIndianPhoneNumber(this.user.phone)) {
            this.errors.phone = "Please enter Indian phone";
            errorsCount++;
          } else {
            this.errors.phone = "";
          }
        }
      }

      if (!this.user.gender) {
        this.errors.gender = "Please choose your gender";
        errorsCount++;
      } else {
        this.errors.gender = "";
      }

      if (errorsCount > 0) {
        return;
      }

      this.$http
        .$post("/register", {
          body: {
            name: this.user.name,
            email: this.user.email.toLowerCase(),
            password: this.user.password,
            phone: this.user.phone,
            gender: this.user.gender,
            dob: this.user.dob,
          },
        })
        .then((res) => {
          if (res.success) {
            window.location.href = "/login";
            return;
          }
          alert(res.message);
        });
    },
  },
};
</script>
