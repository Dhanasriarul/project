<template>
  <div>
    <div
      @click="chatIsOpen = !chatIsOpen"
      class="h-[50px] w-[50px] bg-black rounded-full fixed bottom-10 right-10 flex justify-center items-center cursor-pointer"
    >
      <i
        v-if="!chatIsOpen"
        class="text-lg text-white fa-regular fa-message"
      ></i>
      <i v-else class="text-lg text-white fa-solid fa-x"></i>
    </div>
    <div
      v-if="chatIsOpen"
      class="fixed bottom-[120px] right-10 h-[70%] w-[420px] bg-white shadow-2xl rounded-xl border border-gray-200 overflow-hidden p-4"
    >
      <div
        class="flex items-center justify-center w-full px-3 h-[70px] bg-black rounded-2xl"
      >
        <h1 class="text-2xl font-bold text-white">OneYes Chat bot</h1>
      </div>
      <div
        class="w-full h-[calc(100%-140px)] flex flex-col gap-3 py-3 overflow-auto"
      >
        <div v-for="(chat, index) in chats" :key="index" class="chat-message">
          <div
            class="flex items-end"
            :class="chat.side == 'right' ? 'justify-end' : ''"
          >
            <div
              class="flex flex-col items-end order-1 max-w-xs mx-2 space-y-2 text-xs"
            >
              <div>
                <span
                  class="inline-block px-4 py-2 text-white bg-blue-600 rounded-lg rounded-br-none"
                  >{{ chat.message }}</span
                >
              </div>
            </div>
            <div
              class="flex items-center justify-center w-10 h-10 bg-black rounded-lg"
              :class="chat.side == 'right' ? 'order-2' : ''"
            >
              <i
                v-if="chat.side == 'right'"
                class="text-white fa-solid fa-user"
              ></i>
              <i v-else class="text-white fa-solid fa-robot"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="w-full h-[70px] flex items-center justify-between gap-3">
        <input
          v-model="prompt"
          type="text"
          @keyup.enter="output()"
          placeholder="Type your prompt here"
          class="w-full h-[50px] rounded-xl border border-gray-300 px-3"
        />
        <div
          @click="output()"
          class="w-10 h-10 bg-black rounded-md min-w-[40px] flex justify-center items-center"
        >
          <i class="text-white fa-regular fa-paper-plane"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chatIsOpen: false,
      prompt: "",
      chats: [
        {
          side: "left",
          message: "Can be verified on any platform using docker",
        },
        {
          side: "right",
          message:
            "Your error message says permission denied, npm global installs must be given root privileges.",
        },
      ],
      prompts: [
        ["how are you"],
        ["what", "what are the services", "services", "tell me all services"],
        [
          "hi",
          "hii",
          "hai",
          "haii",
          "hello",
          "good morning",
          "hey",
          "good afternoon",
        ],
        ["support", "support for clients", "contact", " how to contact"],
        ["what are the products", "products", "product details"],
        [
          "e-commerce",
          "ecommerce",
          "tell me about e-commerce",
          "what is e-commerce",
        ],
        ["CRM", "tell me about CRM", "what is CRM"],
        ["edu-tech", "edutech", "tell me about edutech", "edutech"],
        ["hire-connect", "Hire-connect", "hireconnect", "what is hireconnect"],
        ["ok", "nice"],
      ],
      replies: [
        ["I'm Fine.. How can I help you?"],
        [
          "we give you a user friendly services like Web Development,Mobile app development,Web Design,Digital Marketing",
        ],
        ["Hii Heartily Welcome to Oneyes Infotech Solutions"],
        [
          "We give our almost support to your requirements and we you can contact us through mail,mobile number",
        ],
        ["we are having a products like e-commerce,CRM,Hire-connect,Edu-tech"],
        [
          "We specialize in developing and optimizing e-commerce websites and platforms, enabling businesses to sell their products or services online efficiently.",
          "Our e-commerce solutions include creating user-friendly and secure online stores, implementing payment gateways, optimizing product listings, and enhancing the overall shopping experience for both businesses and their customers. We also offer features like inventory management, order tracking, and analytics to help businesses manage their online operations effectively.",
          "Whether you're a small startup or an established enterprise, our e-commerce solutions are tailored to meet your specific needs, drive sales, and enhance your online presence. If you have any specific questions or need more details about our e-commerce services, please feel free to ask.",
        ],
        [
          "Our CRM systems are designed to help organizations effectively manage and nurture their customer relationships, resulting in improved customer satisfaction and business growth.",
          "Our CRM solutions encompass a wide range of features, including contact management, sales automation, customer support, and analytics. With our CRM systems, businesses can streamline their sales processes, track customer interactions, and gain valuable insights into customer behavior.",
          "Whether you're looking to enhance your sales team's productivity, provide exceptional customer service, or gain a better understanding of your customer base, our CRM solutions are tailored to meet your unique requirements. If you have any specific questions or need more information about our CRM services, please don't hesitate to ask.",
        ],
        [
          " We specialize in providing innovative Edu-Tech solutions that enhance the learning experience for students and improve operational efficiency for educational organizations.",
          "Our Edu-Tech solutions cover a broad spectrum of services, including e-learning platforms, student management systems, online assessment tools, and more. We understand the evolving needs of educational institutions, from schools to universities, and offer customized solutions to meet their specific requirements.",
          "Whether you're an educational institution looking to modernize your teaching methods or a student seeking a user-friendly online learning platform, our Edu-Tech solutions are designed to meet your needs.",
        ],
        [
          " We offer a comprehensive platform designed to streamline the hiring process and help companies find the right candidates for their job vacancies.",
          "Our Hire-Connect platform includes features such as job posting, applicant tracking, candidate screening, and interview scheduling. We understand the challenges of recruitment, and our solution is tailored to simplify the process, saving time and resources for businesses.",
          "Our goal is to bridge the gap between employers and job seekers, ensuring mutually beneficial connections.",
        ],
        ["Thank you for visiting Oneyes Infotech Solution"],
      ],
      alternative: [
        "Try again",
        "I'm not listening...Try again",
        "I don't understand :/",
      ],
      coronavirus: [
        "Please stay home",
        "Wear a mask",
        "Fortunately, I don't have COVID",
        "These are uncertain times",
      ],
      developers: ["XYZ.. "],
    };
  },
  methods: {
    compare() {
      let reply;
      let replyFound = false;

      for (let x = 0; x < this.prompts.length; x++) {
        for (let y = 0; y < this.prompts[x].length; y++) {
          if (this.prompts[x][y] === this.prompt) {
            let replies = this.replies[x];
            reply = replies[Math.floor(Math.random() * replies.length)];
            replyFound = true;
            break;
          }
        }
        if (replyFound) {
          break;
        }
      }
      return reply;
    },
    output() {
      let product;

      this.chats.push({
        side: "right",
        message: this.prompt,
      });

      let text = this.prompt
        .toLowerCase()
        .replace(/[^\w\s]/gi, "")
        .replace(/[\d]/gi, "")
        .trim();

      text = text
        .replace(/ a /g, " ")
        .replace(/i feel /g, "")
        .replace(/whats/g, "what is")
        .replace(/please /g, "")
        .replace(/ please/g, "")
        .replace(/r u/g, "are you");

      if (this.compare()) {
        product = this.compare();
      } else if (text.match(/thank/gi)) {
        product = "You're welcome!";
      } else {
        product =
          this.alternative[Math.floor(Math.random() * this.alternative.length)];
      }

      this.chats.push({
        side: "left",
        message: product,
      });

      this.prompt = "";
    },
  },
};
</script>
