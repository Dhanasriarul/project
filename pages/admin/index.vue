<template>
  <div>
    <div>
      <h3 class="text-base font-semibold leading-6 text-gray-900">Stats</h3>

      <dl class="grid grid-cols-1 gap-5 mt-5 sm:grid-cols-2 lg:grid-cols-3">
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 448 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              Users Count
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.users || 0 }}
            </p>
          </dd>
        </div>
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 576 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              Home Visits
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.home || 0 }}
            </p>
          </dd>
        </div>
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 576 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              E-commerce visits
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.eCommerce || 0 }}
            </p>
          </dd>
        </div>
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 512 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M64 64c0-17.7-14.3-32-32-32S0 46.3 0 64V400c0 44.2 35.8 80 80 80H480c17.7 0 32-14.3 32-32s-14.3-32-32-32H80c-8.8 0-16-7.2-16-16V64zm406.6 86.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L320 210.7l-57.4-57.4c-12.5-12.5-32.8-12.5-45.3 0l-112 112c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L240 221.3l57.4 57.4c12.5 12.5 32.8 12.5 45.3 0l128-128z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              CRM Visits
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.crm || 0 }}
            </p>
          </dd>
        </div>
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 448 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M96 0C43 0 0 43 0 96V416c0 53 43 96 96 96H384h32c17.7 0 32-14.3 32-32s-14.3-32-32-32V384c17.7 0 32-14.3 32-32V32c0-17.7-14.3-32-32-32H384 96zm0 384H352v64H96c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16zm16 48H336c8.8 0 16 7.2 16 16s-7.2 16-16 16H144c-8.8 0-16-7.2-16-16s7.2-16 16-16z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              Edu-Tech Visits
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.eduTech || 0 }}
            </p>
          </dd>
        </div>
        <div
          class="relative px-4 pt-5 overflow-hidden bg-white rounded-lg shadow sm:px-6 sm:pt-6"
        >
          <dt>
            <div class="absolute p-3 bg-indigo-500 rounded-md">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="1em"
                viewBox="0 0 512 512"
                class="fill-white"
              >
                <!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                <path
                  d="M256 48C141.1 48 48 141.1 48 256v40c0 13.3-10.7 24-24 24s-24-10.7-24-24V256C0 114.6 114.6 0 256 0S512 114.6 512 256V400.1c0 48.6-39.4 88-88.1 88L313.6 488c-8.3 14.3-23.8 24-41.6 24H240c-26.5 0-48-21.5-48-48s21.5-48 48-48h32c17.8 0 33.3 9.7 41.6 24l110.4 .1c22.1 0 40-17.9 40-40V256c0-114.9-93.1-208-208-208zM144 208h16c17.7 0 32 14.3 32 32V352c0 17.7-14.3 32-32 32H144c-35.3 0-64-28.7-64-64V272c0-35.3 28.7-64 64-64zm224 0c35.3 0 64 28.7 64 64v48c0 35.3-28.7 64-64 64H352c-17.7 0-32-14.3-32-32V240c0-17.7 14.3-32 32-32h16z"
                />
              </svg>
            </div>
            <p class="ml-16 text-sm font-medium text-gray-500 truncate">
              Hire-Connect Visits
            </p>
          </dt>
          <dd class="flex items-baseline pb-6 ml-16">
            <p class="text-2xl font-semibold text-gray-900">
              {{ stats.hireConnect || 0 }}
            </p>
          </dd>
        </div>
      </dl>
    </div>

    <canvas
      class="mt-10"
      id="myChart"
      style="width: 100%; height: 500px"
    ></canvas>
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
      stats: {},
      chartUi: null,
    };
  },
  mounted() {
    this.getStats();
  },
  methods: {
    getStats() {
      this.$http
        .$get("/admin-stats")
        .then((res) => {
          if (res.success) {
            this.stats = res.visitCount;

            var xValues = [
              "User",
              "Home",
              "E-Commerce",
              "CRM",
              "Edu-Tech",
              "Hire-Connect",
            ];
            var yValues = [
              res.visitCount.users,
              res.visitCount.home,
              res.visitCount.eCommerce,
              res.visitCount.crm,
              res.visitCount.eduTech,
              res.visitCount.hireConnect,
            ];
            var barColors = ["#6366f1"];

            new Chart("myChart", {
              type: "bar",
              data: {
                labels: xValues,
                datasets: [
                  {
                    backgroundColor: barColors,
                    data: yValues,
                    label: "Visits",
                  },
                ],
              },
            });
            return;
          }
          alert(res.message);
        })
        .catch((err) => {
          alert(err.message);
        });
    },
  },
};
</script>
