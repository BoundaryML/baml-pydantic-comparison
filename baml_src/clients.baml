client<llm> GPT4 {
  provider baml-openai-chat
  options {
    model gpt-4
    api_key env.OPENAI_API_KEY
  }
}

client<llm> GPT4Turbo {
  provider baml-openai-chat
  options {
    model gpt-4-1106-preview
    api_key env.OPENAI_API_KEY
  }
}

client<llm> GPT35 {
  provider baml-openai-chat
  options {
    model gpt-3.5-turbo
    api_key env.OPENAI_API_KEY
  }
}

client<llm> Mistral {
  provider baml-ollama-chat
  options {
    model Mistral
  }
}

client<llm> Llama2 {
  provider baml-ollama-chat
  options {
    model llama2:chat
  }
}