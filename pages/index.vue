<template>
  <div>
    <NavBar />
    <div class="bg-white">
      <main class="isolate">
        <!-- Hero section -->
        <div id="hero-sec" class="relative">
          <div
            class="absolute inset-x-0 overflow-hidden -top-40 -z-10 transform-gpu blur-3xl sm:-top-80"
            aria-hidden="true"
          >
            <div
              class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
              style="
                clip-path: polygon(
                  74.1% 44.1%,
                  100% 61.6%,
                  97.5% 26.9%,
                  85.5% 0.1%,
                  80.7% 2%,
                  72.5% 32.5%,
                  60.2% 62.4%,
                  52.4% 68.1%,
                  47.5% 58.3%,
                  45.2% 34.5%,
                  27.5% 76.7%,
                  0.1% 64.9%,
                  17.9% 100%,
                  27.6% 76.8%,
                  76.1% 97.7%,
                  74.1% 44.1%
                );
              "
            ></div>
          </div>
          <div class="py-24 sm:py-32">
            <div class="px-6 mx-auto max-w-7xl lg:px-8">
              <div class="max-w-2xl mx-auto text-center">
                <h1
                  class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl"
                >
                  We provide solutions for your business!
                </h1>
                
                <!-- <div class="flex items-center justify-center mt-10 gap-x-6">
                  <a
                    href="#"
                    class="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                    >Get started</a
                  >
                  <a
                    href="#"
                    class="text-sm font-semibold leading-6 text-gray-900"
                    >Our Services <span aria-hidden="true">→</span></a
                  >
                </div> -->
              </div>
              <div class="flow-root mt-16 sm:mt-24">
                <div
                  class="p-2 -m-2 rounded-xl bg-gray-900/5 ring-1 ring-inset ring-gray-900/10 lg:-m-4 lg:rounded-2xl lg:p-4"
                >
                  <img
                    src="https://digisajilo.com/images/about/spl-image-main.svg"
                    alt="App screenshot"
                    width="2432"
                    height="1442"
                    class="rounded-md shadow-2xl ring-1 ring-gray-900/10"
                  />
                </div>
              </div>
            </div>
          </div>
          <div
            class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
            aria-hidden="true"
          >
            <div
              class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"
              style="
                clip-path: polygon(
                  74.1% 44.1%,
                  100% 61.6%,
                  97.5% 26.9%,
                  85.5% 0.1%,
                  80.7% 2%,
                  72.5% 32.5%,
                  60.2% 62.4%,
                  52.4% 68.1%,
                  47.5% 58.3%,
                  45.2% 34.5%,
                  27.5% 76.7%,
                  0.1% 64.9%,
                  17.9% 100%,
                  27.6% 76.8%,
                  76.1% 97.7%,
                  74.1% 44.1%
                );
              "
            ></div>
          </div>
        </div>

        <!-- Categories -->
        <div class="py-24 bg-white sm:py-32">
          <div class="px-6 mx-auto max-w-7xl lg:px-8">
            <div class="max-w-2xl mx-auto lg:mx-0">
              <h2
                class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl"
              >
                Categories
              </h2>
            </div>
            <ul
              role="list"
              class="grid max-w-2xl grid-cols-1 mx-auto mt-20 gap-x-8 gap-y-16 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3"
            >
              <li v-for="(category, index) in categories" :key="index">
                <NuxtLink :to="`/category/${category.categoryId}?name=${category.name}`">
                  <div>
                    <img
                      class="aspect-[3/2] w-full rounded-2xl object-cover"
                      :src="category.image"
                      alt=""
                    />
                    <h3
                      class="mt-6 text-lg font-semibold leading-8 tracking-tight text-gray-900"
                    >
                      {{ category.name }}
                    </h3>
                  </div>
                </NuxtLink>
              </li>

              <!-- More people... -->
            </ul>
          </div>
        </div>

        <!-- About section -->
        <div id="about-sec" class="py-20 bg-black">
          <div class="px-6 mx-auto max-w-7xl lg:px-8">
            <div class="max-w-2xl mx-auto text-center">
              <h2 class="text-base font-semibold leading-7 text-indigo-400">
                To know
              </h2>
              <p
                class="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl"
              >
                About Us
              </p>
              <p class="mt-6 text-lg leading-8 text-gray-300">
                We have carved a distinct niche for ourselves in the realm of
                mobile and website development, having embarked on this journey
                in 2012 with just three team members. Our remarkable growth, now
                boasting a team of over 50 experts, serves as a testament to the
                quality of work we've consistently delivered over the years.
              </p>
            </div>
            <div
              class="max-w-2xl mx-auto mt-16 sm:mt-20 lg:mt-24 lg:max-w-none"
            >
              <dl
                class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3"
              >
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"
                        />
                      </svg>
                    </div>
                    Research and Analysis
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      We place a strong emphasis on thorough research and
                      analysis to formulate efficient strategies that drive cost
                      reduction. Our hallmark lies in our flexibility, as we are
                      always prepared to tailor our services to meet our
                      clients' specific requirements.
                    </p>
                    <p class="mt-6">
                      <a
                        href="#"
                        class="text-sm font-semibold leading-6 text-indigo-400"
                        >Learn more <span aria-hidden="true">→</span></a
                      >
                    </p>
                  </dd>
                </div>
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"
                        />
                      </svg>
                    </div>

                    Creative and innovative solutions
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      Our team comprises professionals who possess the ability
                      to think creatively and innovatively, consistently
                      delivering solutions that transcend conventional
                      boundaries.
                    </p>
                    <p class="mt-6">
                      <a
                        href="#"
                        class="text-sm font-semibold leading-6 text-indigo-400"
                        >Learn more <span aria-hidden="true">→</span></a
                      >
                    </p>
                  </dd>
                </div>
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z"
                        />
                      </svg>
                    </div>
                    Agile Method
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      Our methodologies are rooted in the principles outlined in
                      the Agile Manifesto for software development, ensuring
                      that our product development approaches are in alignment
                      with these values and principles.
                    </p>
                    <p class="mt-6">
                      <a
                        href="#"
                        class="text-sm font-semibold leading-6 text-indigo-400"
                        >Learn more <span aria-hidden="true">→</span></a
                      >
                    </p>
                  </dd>
                </div>
              </dl>
            </div>
          </div>
        </div>

        <!-- Products Section -->
        <section id="product-sec" class="py-20">
          <div class="max-w-2xl mx-auto mb-5 lg:text-center">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">
              Our Valuable
            </h2>
            <p
              class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl"
            >
              Products
            </p>
          </div>
          <div
            class="grid min-h-full grid-cols-1 grid-rows-2 gap-3 px-3 lg:grid-cols-2 lg:grid-rows-1"
          >
            <div class="relative flex overflow-hidden rounded-3xl">
              <img
                src="https://blogassets.leverageedu.com/blog/wp-content/uploads/2020/05/14190804/e-commerce-.jpg"
                alt=""
                class="absolute inset-0 object-cover object-center w-full h-full"
              />
              <div
                class="relative flex flex-col items-start justify-end w-full p-8 bg-black bg-opacity-60 sm:p-12"
              >
                <p class="text-2xl font-medium text-white">E-Commerce</p>
                <h2 class="mt-2 text-sm text-white">
                  As you are aware, the advancement of technology and
                  communications has had a great say in the business and economy
                  of the world that trading is made possible round the clock
                  from any corner of the globe. Such a transaction, also known
                  as ecommerce, has enabled companies to gain access to their
                  clients at any part of the world at any time. We are the best
                  Ecommerce Website Development in Chennai to fullfill your
                  needs.
                </h2>
                <div class="flex items-center justify-between w-full">
                  <NuxtLink
                    to="/product/e-commerce"
                    class="mt-4 rounded-md bg-white px-4 py-2.5 text-sm font-medium text-gray-900 hover:bg-gray-50"
                    >Learn more</NuxtLink
                  >
                  <h1 class="text-2xl font-bold text-white">
                    Visits: {{ counts.eCommerce }}
                  </h1>
                </div>
              </div>
            </div>
            <div class="relative flex overflow-hidden rounded-3xl">
              <img
                src="https://www.reallysimplesystems.com/assets/blog_images/data-mining-in-crm/data-mining-in-crm.jpeg"
                alt=""
                class="absolute inset-0 object-cover object-center w-full h-full"
              />
              <div
                class="relative flex flex-col items-start justify-end w-full p-8 bg-black bg-opacity-60 sm:p-12"
              >
                <p class="text-2xl font-medium text-white">CRM</p>
                <h2 class="mt-2 text-sm text-white">
                  We serve cloud-based CRM software for enterprises, which
                  provides comprehensive customer experience management
                  facilities across multiple communication channels. The
                  software is also capable of automating business-critical
                  activities such as lead capturing, distribution, ticket
                  management, and more.The program can be configured according
                  to unique business requirements.
                </h2>
                <div class="flex items-center justify-between w-full">
                  <NuxtLink
                    to="/product/crm"
                    class="mt-4 rounded-md bg-white px-4 py-2.5 text-sm font-medium text-gray-900 hover:bg-gray-50"
                  >
                    Learn more
                  </NuxtLink>
                  <h1 class="text-2xl font-bold text-white">
                    Visits: {{ counts.crm }}
                  </h1>
                </div>
              </div>
            </div>
            <div class="relative flex overflow-hidden rounded-3xl">
              <img
                src="https://thetinytech.com/wp-content/uploads/2021/02/Software-Development-Team.png"
                alt=""
                class="absolute inset-0 object-cover object-center w-full h-full"
              />
              <div
                class="relative flex flex-col items-start justify-end w-full p-8 bg-black bg-opacity-60 sm:p-12"
              >
                <p class="text-2xl font-medium text-white">Hire-Connect</p>
                <h2 class="mt-2 text-sm text-white text-opacity-75">
                  Give your talent acquisition team the power to develop
                  engaging and interactive virtual hiring events that drive
                  conversions.The technical interview- in which subject related
                  questions will be asked, Group discussion and finally face to
                  face interview will happen through our portal and the HR will
                  select the qualified candidates . Offer letter issuance can be
                  directly done from our portal.
                </h2>
                <div class="flex items-center justify-between w-full">
                  <NuxtLink
                    to="/product/hire-connect"
                    class="mt-4 rounded-md bg-white px-4 py-2.5 text-sm font-medium text-gray-900 hover:bg-gray-50"
                  >
                    Learn more
                  </NuxtLink>
                  <h1 class="text-2xl font-bold text-white">
                    Visits: {{ counts.hireConnect }}
                  </h1>
                </div>
              </div>
            </div>
            <div class="relative flex overflow-hidden rounded-3xl">
              <img
                src="https://tradebrains.in/wp-content/uploads/2020/11/Untitled-design.jpg"
                alt=""
                class="absolute inset-0 object-cover object-center w-full h-full"
              />
              <div
                class="relative flex flex-col items-start justify-end w-full p-8 bg-black bg-opacity-60 sm:p-12"
              >
                <p class="text-2xl font-medium text-white">Edu-Tech</p>
                <h2 class="mt-2 text-sm text-white text-opacity-75">
                  Online Education Portal is one of our premium products and
                  this portal focuses on providing end-to-end management
                  solutions to all the stakeholders of an educational
                  institute.Online Education ensures flexibility to all its
                  stakeholders. While the students get the freedom to study at
                  their pace, the teachers can also share their e-assessments,
                  reports at their convenience.
                </h2>
                <div class="flex items-center justify-between w-full">
                  <NuxtLink
                    to="/product/edu-tech"
                    class="mt-4 rounded-md bg-white px-4 py-2.5 text-sm font-medium text-gray-900 hover:bg-gray-50"
                  >
                    Learn more
                  </NuxtLink>
                  <h1 class="text-2xl font-bold text-white">
                    Visits: {{ counts.eduTech }}
                  </h1>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- Services section -->
        <div
          id="services-sec"
          class="px-6 mx-auto mt-32 max-w-7xl sm:mt-56 lg:px-8"
        >
          <div class="max-w-2xl mx-auto lg:text-center">
            <h2 class="text-base font-semibold leading-7 text-indigo-600">
              Our Customer centric
            </h2>
            <p
              class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl"
            >
              Services
            </p>
          </div>
          <div class="max-w-2xl mx-auto mt-16 sm:mt-20 lg:mt-24 lg:max-w-4xl">
            <dl
              class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16"
            >
              <div class="relative pl-16">
                <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div
                    class="absolute top-0 left-0 flex items-center justify-center w-10 h-10 bg-indigo-600 rounded-lg"
                  >
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
                        d="M12 16.5V9.75m0 0l3 3m-3-3l-3 3M6.75 19.5a4.5 4.5 0 01-1.41-8.775 5.25 5.25 0 0110.233-2.33 3 3 0 013.758 3.848A3.752 3.752 0 0118 19.5H6.75z"
                      />
                    </svg>
                  </div>
                  WEB DEVELOPMENT
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">
                  We build a distinct agile approach in web development & design
                  services to meet all the business needs and stay out from
                  competitors. Our website development outcome is creating
                  abiding impressions.
                </dd>
              </div>
              <div class="relative pl-16">
                <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div
                    class="absolute top-0 left-0 flex items-center justify-center w-10 h-10 bg-indigo-600 rounded-lg"
                  >
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
                        d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"
                      />
                    </svg>
                  </div>
                  MOBILE APP DEVELOPMENT
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">
                  You might have a business that you wish to take to the next
                  level. In the age of the internet, it’s possible! Your
                  business can have a presence online within your compact mobile
                  phone.
                </dd>
              </div>
              <div class="relative pl-16">
                <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div
                    class="absolute top-0 left-0 flex items-center justify-center w-10 h-10 bg-indigo-600 rounded-lg"
                  >
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
                        d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
                      />
                    </svg>
                  </div>
                  WEB DESIGN
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">
                  If you want to have creative web design services, then you’ve
                  landed at the right place! At OneYes Infotech Solutions, we
                  have designed different websites for our esteemed clients.
                </dd>
              </div>
              <div class="relative pl-16">
                <dt class="text-base font-semibold leading-7 text-gray-900">
                  <div
                    class="absolute top-0 left-0 flex items-center justify-center w-10 h-10 bg-indigo-600 rounded-lg"
                  >
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
                        d="M7.864 4.243A7.5 7.5 0 0119.5 10.5c0 2.92-.556 5.709-1.568 8.268M5.742 6.364A7.465 7.465 0 004.5 10.5a7.464 7.464 0 01-1.15 3.993m1.989 3.559A11.209 11.209 0 008.25 10.5a3.75 3.75 0 117.5 0c0 .527-.021 1.049-.064 1.565M12 10.5a14.94 14.94 0 01-3.6 9.75m6.633-4.596a18.666 18.666 0 01-2.485 5.33"
                      />
                    </svg>
                  </div>
                  DIGITAL MARKETING
                </dt>
                <dd class="mt-2 text-base leading-7 text-gray-600">
                  In today’s world, the internet plays a huge part in everyone’s
                  life. A wide audience is available on the internet, who
                  continuously searching for products or services.
                </dd>
              </div>
            </dl>
          </div>
        </div>

        <!-- Stats -->
        <div id="stats-sec" class="py-20 mt-32 bg-black sm:mt-56">
          <div class="px-6 mx-auto max-w-7xl lg:px-8">
            <div class="max-w-2xl mx-auto lg:mx-0 lg:max-w-xl">
              <h2 class="text-base font-semibold leading-8 text-indigo-400">
                Our track record
              </h2>
              <p
                class="mt-2 text-3xl font-bold tracking-tight text-white sm:text-4xl"
              >
                Why choose us?
              </p>
            </div>
            <div
              class="max-w-2xl mx-auto mt-16 sm:mt-20 lg:mt-24 lg:max-w-none"
            >
              <dl
                class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3"
              >
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"
                        />
                      </svg>
                    </div>
                    We Create Experiences & Attractions:
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      We specialize in crafting purpose-driven websites,
                      consistently delivering top-notch digital products that
                      are renowned for their simplicity. Our reputation as one
                      of the leading web design and development companies in the
                      region reflects our unwavering commitment to creating
                      exceptional online experiences tailored to your audience's
                      needs.
                    </p>
                  </dd>
                </div>
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"
                        />
                      </svg>
                    </div>

                    We Ask, Listen and Understand:
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      At the outset of every web development project, we
                      initiate a thorough process of inquiry, attentive
                      listening, and comprehensive understanding. Our goal is to
                      delve into your essence, unravel your purpose, and unearth
                      the 'why' behind your endeavors. This foundational
                      understanding forms the bedrock upon which we craft
                      strategic web design solutions that effectively convey
                      your intended messages and authentically express your
                      distinctive brand identity.
                    </p>
                  </dd>
                </div>
                <div class="flex flex-col">
                  <dt class="text-base font-semibold leading-7 text-white">
                    <div
                      class="flex items-center justify-center w-10 h-10 mb-6 bg-indigo-500 rounded-lg"
                    >
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
                          d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5m-9-6h.008v.008H12v-.008zM12 15h.008v.008H12V15zm0 2.25h.008v.008H12v-.008zM9.75 15h.008v.008H9.75V15zm0 2.25h.008v.008H9.75v-.008zM7.5 15h.008v.008H7.5V15zm0 2.25h.008v.008H7.5v-.008zm6.75-4.5h.008v.008h-.008v-.008zm0 2.25h.008v.008h-.008V15zm0 2.25h.008v.008h-.008v-.008zm2.25-4.5h.008v.008H16.5v-.008zm0 2.25h.008v.008H16.5V15z"
                        />
                      </svg>
                    </div>
                    Hundreds of Clients & Years of Experience:
                  </dt>
                  <dd
                    class="flex flex-col flex-auto mt-1 text-base leading-7 text-gray-300"
                  >
                    <p class="flex-auto">
                      With a rich history dating back to 2012, Oneyes Infotech
                      Solutions has had the privilege of assisting numerous
                      businesses in achieving remarkable success in their online
                      marketing endeavors. Our extensive experience and in-depth
                      knowledge form the cornerstone of our approach as we guide
                      our clients toward elevating their businesses to new
                      heights through a range of results-oriented solutions.
                    </p>
                  </dd>
                </div>
              </dl>
            </div>
            <dl
              class="grid max-w-2xl grid-cols-1 mx-auto mt-16 text-white gap-x-8 gap-y-10 sm:mt-20 sm:grid-cols-2 sm:gap-y-16 lg:mx-0 lg:max-w-none lg:grid-cols-4"
            >
              <div class="flex flex-col pl-6 border-l gap-y-3 border-white/10">
                <dt class="text-sm leading-6">Clients</dt>
                <dd class="order-first text-3xl font-semibold tracking-tight">
                  50+
                </dd>
              </div>
              <div class="flex flex-col pl-6 border-l gap-y-3 border-white/10">
                <dt class="text-sm leading-6">Projects</dt>
                <dd class="order-first text-3xl font-semibold tracking-tight">
                  500+
                </dd>
              </div>
              <div class="flex flex-col pl-6 border-l gap-y-3 border-white/10">
                <dt class="text-sm leading-6">Hours Of Support</dt>
                <dd class="order-first text-3xl font-semibold tracking-tight">
                  1364
                </dd>
              </div>
              <div class="flex flex-col pl-6 border-l gap-y-3 border-white/10">
                <dt class="text-sm leading-6">Hard Workers</dt>
                <dd class="order-first text-3xl font-semibold tracking-tight">
                  50
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </main>
    </div>
    <ChatBot />
  </div>
</template>

<script>
definePageMeta({
  middleware: ["auth"],
});
export default {
  data() {
    return {
      counts: {},
      categories: [],
    };
  },
  mounted() {
    if (localStorage.getItem("isLoggedIn") == "true") {
      this.$http
        .$post("/visits", {
          body: {
            page: "home",
          },
        })
        .then((res) => {
          if (res.success) {
            return;
          }
          alert(res.message);
        });

      this.$http.$get("/categories").then((res) => {
        if (res.success) {
          this.categories = res.categories;
          return;
        }
        alert(res.message);
      });

      this.$http.$get("/admin-stats").then((res) => {
        if (res.success) {
          this.counts = res.visitCount;
          return;
        }
        alert(res.message);
      });
    }
  },
};
</script>
