
class PIIData {
  index int
  data_type string
  pii_value string
}

function ExtractPII {
  input string
  output PIIData[] 
}

impl<llm, ExtractPII> v1 {
  client GPT35
  prompt #"
    {#chat(system)} You are a world class PII scrubbing model, Extract the PII data from the following document.

    Return the PII in the following json format:
    {#print_type(output)}
    {#chat(user)} {#input}
  "#
}

