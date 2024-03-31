from pydantic import BaseModel
from instructor import patch, Mode
from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
from baml_client.baml_types import OrderInfo2
from typing import List, Optional
import instructor

# set debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

# Desired output structure
class OrderInfo(BaseModel):
    id: str
    price: int

openai_api_key = os.environ.get("OPENAI_API_KEY")

# Patch the OpenAI client
client: OpenAI = patch(OpenAI(api_key=openai_api_key), mode=Mode.MD_JSON)

ollama_client = client = instructor.patch(
    OpenAI(
        base_url="http://localhost:11434",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)


def extract_order_info_mistral(arg: str):
    resp = ollama_client

def extract_order_info_instructor(arg: str):
    resp = client.chat.completions.create(
        model="gpt-4",
        response_model=OrderInfo, 
        messages=[
            {"role": "user", "content": "The order id is 123 and the price is 1000"},
        ]
    )

    print(resp._raw_response)


def extract_order_info_instructor2(arg: str):
    resp = client.chat.completions.create(
        model="gpt-4",
        response_model=OrderInfo2, 
        messages=[
            {"role": "user", "content": arg},
        ]
    )

    print(resp._raw_response)
    print(resp.id)
    print(resp.price)
from pydantic import Field
from enum import Enum

class Item(BaseModel):
    name: str
    quantity: int

class State(Enum):
    WASHINGTON = "WASHINGTON"
    CALIFORNIA = "CALIFORNIA"
    OREGON = "OREGON"

class Address(BaseModel):
    street: Optional[str]
    city: Optional[str] = Field(description="The city name in lowercase")
    state: Optional[State] = Field(description="The state abbreviation from the predefined states")
    zip_code: Optional[str]

class OrderInfo3(BaseModel):
    id: str = Field(alias="order_id")
    price: Optional[int] = Field(alias="total_price", description="The total price. Don't include shipping costs.")
    items: List[Item] = Field(description="purchased_items")
    shipping_address: Optional[Address]


def extract_order_info_instructor3(arg: str):
    try:
      resp: OrderInfo3 = client.chat.completions.create(
          model="gpt-4",
          response_model=OrderInfo3, 
          messages=[
              {"role": "user", "content": arg},
          ]
      )

      print(resp._raw_response) # instructor adds the _raw_resopnse here so the type is not accurate.
      print(resp.model_dump_json(indent=2))
    except Exception as e:
      print(e)


from baml_client import baml as b

async def extract_order_info_baml(arg: str):
    resp = await b.ExtractOrderInfo(arg)
    print(resp)


async def extract_order_info_baml2(arg: str):
    resp = await b.ExtractOrderInfo2(arg)
    print(resp)

async def extract_order_info_baml3(arg: str):
    resp = await b.ExtractOrderInfo3(arg)
    print(resp.model_dump_json(indent=2))


if __name__ == "__main__":
    arg = "The order id is 123 and the price is 1000. The state is WA"
    print("\n\n----------Extract 1-----------")

    extract_order_info_instructor(arg)
    print("-------------BAML-------------")
    asyncio.run(extract_order_info_baml(arg))

    print("\n\n----------Extract2-----------")
    extract_order_info_instructor2(arg)
    print("-------------BAML-------------")
    asyncio.run(extract_order_info_baml2(arg))

    print("\n\n----------Extract3-----------")
    extract_order_info_instructor3(arg)
    print("-------------BAML-------------")
    asyncio.run(extract_order_info_baml3(arg))

