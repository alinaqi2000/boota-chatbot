const prompts_data = [
  { question: "how are you?", answer: "I'm good, thank you for asking." },
  {
    question: "What's your name?",
    answer: "I'm a chatbot. You can call me ChatGPT.",
  },
  {
    question: "Can you help me with Python programming?",
    answer:
      "Yes, I can help you with Python programming. What specific question do you have?",
  },
  {
    question: "Tell me a joke.",
    answer:
      "Why don't scientists trust atoms? Because they make up everything.",
  },
  {
    question: "What is the meaning of life?",
    answer:
      "The meaning of life is a philosophical question. Different people have different perspectives on it.",
  },
];

for (inp of prompts_data) {
  var requestHeaders = {
    "Content-Type": "application/json",
  };
  var requestBody = {
    prompt: inp.question,
  };
  pm.sendRequest(
    {
      url: pm.collectionVariables.get("baseURL") + "prompt",
      method: "POST",
      headers: requestHeaders,
      body: JSON.stringify(requestBody),
    },
    function (err, response) {
      pm.test(
        "Prompt: " + JSON.stringify(response) + ", Response: " + inp.answer,
        function () {
          pm.expect(response.code).to.include(inp.answer);
        }
      );
    }
  );
}
