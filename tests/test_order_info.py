from pydantic import BaseModel, Field
from instructor import patch, Mode
from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
from baml_client.baml_types import OrderInfo2
from typing import List, Optional
import instructor
import pytest

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
        base_url="http://localhost:11434/v1",
        api_key="ollama", # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

test_case = """In the vibrant online marketplace, a customer recently completed a purchase with order ID "ORD1234567". This transaction, totaling $85 without accounting for shipping costs, included an eclectic mix of items: a handcrafted ceramic vase, a set of artisanal kitchen knives, and a vintage-inspired wall clock. The order is destined for 456 Artisan Way in the bustling city of portland, adhering to the lowercase convention for city names. Oregon, represented by its abbreviation "OR" as per the predefined states, is where this delightful array will find its new home, at the ZIP code 97205. This meticulous record encapsulates not just a transaction but the seamless fusion of commerce and craftsmanship, poised to enrich the living space of its recipient. testing testing123 hello hello."""

test_case2 = """A recent acquisition by a prominent law firm was meticulously cataloged in their procurement system under the order ID "LFM348920". The order, valued at $450, excluded shipping expenses and comprised an assortment of high-grade office supplies, including executive pens, leather-bound notebooks, and ergonomic desk chairs designed for optimal comfort during extended work periods. The delivery is scheduled for their main office location at 789 Barrister Blvd, in the culturally rich city of seattle. This city, noted in lowercase as per formatting guidelines, falls within Washington ("WA"), following the enumerated state abbreviations. The specified ZIP code for this delivery is 98101, ensuring accurate and prompt distribution of these essential office resources."""

def extract_order_info3_instructor_llama2(arg: str):
    resp = ollama_client.chat.completions.create(
        model="llama2:chat",
        messages=[
            {
                "role": "user",
                "content": arg
            }
        ],
        max_retries=0,
        response_model=OrderInfo3
    )
    print("resp", resp._raw_response)
    print("Mistral: ", resp.model_dump_json(indent=2))

def extract_order_info_instructor(arg: str):
    resp = client.chat.completions.create(
        model="gpt-4",
        response_model=OrderInfo,
        messages=[
            {"role": "user", "content": arg},
        ]
    )
    print(resp._raw_response)

def extract_order_info_instructor_llama2(arg: str):
    resp = ollama_client.chat.completions.create(
        model="llama2:chat",
        response_model=OrderInfo2,
        messages=[
            {"role": "user", "content": arg},
        ]
    )
    print(resp._raw_response)

def extract_order_info2_instructor(arg: str):
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
    WA = "WA"
    CA = "CA"
    OR = "OR"

class Address(BaseModel):
    street: Optional[str]
    city: Optional[str] = Field(description="The city name in lowercase")
    state: Optional[State] = Field(description="The state abbreviation from the predefined states")
    zip_code: Optional[str]

class OrderInfo3(BaseModel):
    id: str = Field(alias="order_id")
    price: Optional[int] = Field(alias="total_price", description="The total price. Don't include shipping costs.")
    items: List[Item] = Field(description="purchased_items")
    shipping_address: Address

def extract_order_info3_instructor(arg: str):
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

async def extract_order_info2_baml(arg: str):
    resp = await b.ExtractOrderInfo2(arg)
    print(resp)

async def extract_order_info3_baml(arg: str):
    resp = await b.ExtractOrderInfo3.get_impl("llama2").run(arg)
    print(resp.model_dump_json(indent=2))

@pytest.mark.parametrize("func", [extract_order_info_instructor, extract_order_info2_instructor, extract_order_info3_instructor])
def test_extract_order_info_instructor(func):
    arg = "The order id is 123 and the price is 1000. The state is WA"
    print(f"\n\n----------{func.__name__}-----------")
    print("-------------Instructor-------------")
    func(test_case)

@pytest.mark.parametrize("func", [extract_order_info_baml, extract_order_info2_baml, extract_order_info3_baml])
@pytest.mark.parametrize("iter", range(100))
@pytest.mark.asyncio
async def test_extract_order_info_baml(func, iter):
    arg = "The order id is 123 and the price is 1000. The state is WA"
    print(f"\n\n----------{func.__name__}-----------")
    print("-------------Llama2 using BAML-------------")
    await func(test_case)

@pytest.mark.parametrize("func", [extract_order_info_instructor_llama2, extract_order_info3_instructor_llama2])
@pytest.mark.parametrize("iter", range(100))
def test_extract_order_info_llama2(func, iter):
    arg = "The order id is 123 and the price is 1000. The state is WA"
    print(f"\n\n----------{func.__name__}-----------")
    print("-------------Llama2 using Instructor-------------")
    func(test_case)