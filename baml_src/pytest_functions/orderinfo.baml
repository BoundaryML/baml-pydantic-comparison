class OrderInfo {
  id string
  price int
}

function ExtractOrderInfo {
  input string
  output OrderInfo
}

impl<llm, ExtractOrderInfo> v1 {
  client GPT4
  prompt #"
    Extract the following information from the text.
    {#input}

    ---
    Return the information in JSON following this schema:
    {#print_type(output)}

    JSON:
  "#
}


// more complex example -- nested types

class Item {
  name string
  quantity int
}

class OrderInfo2 {
  id string
  price int
  items Item[]
}

function ExtractOrderInfo2 {
  input string
  output OrderInfo2
}

impl<llm, ExtractOrderInfo2> v2 {
  client GPT4
  prompt #"
    Extract the following information from the text.
    {#input}

    ---
    Return the information in JSON following this schema:
    {#print_type(output)}

    JSON:
  "#
}


enum States {
  WA
  OR
  CA
  @@alias(STATES)
}

class Address {
  street string
  city string? @description("The city name in lowercase")
  state States @description("The state from the predefined states")
  zip_code string?
}
 
class OrderInfo3 {
  id string @alias("order_id")
  price int? @alias("total_price") @description("The total price. Don't include shipping costs.")
  items Item[] @alias("purchased_items")
  shipping_address Address @alias("address_in_text")
}

function ExtractOrderInfo3 {
  input string
  output OrderInfo3
  default_impl v1
}

impl<llm, ExtractOrderInfo3> v1 {
  client GPT4
  prompt #"
    Extract the following information from the TEXT:
    {#input}

    ---
    Return the information in JSON following this schema:
    {#print_type(output)}

    Predefined STATES:
    {#print_enum(States)}

    JSON:
  "#
}

impl<llm, ExtractOrderInfo3> llama2 {
  client Llama2
  prompt #"
    Extract the following information from the TEXT:
    {#input}

    ---
    Return the information in JSON following this schema:
    {#print_type(output)}

    Predefined STATES:
    {#print_enum(States)}

    JSON:
  "#
}