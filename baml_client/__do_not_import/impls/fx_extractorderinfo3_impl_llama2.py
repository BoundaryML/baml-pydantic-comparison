# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_llama2 import Llama2
from ..functions.fx_extractorderinfo3 import BAMLExtractOrderInfo3
from ..types.classes.cls_address import Address
from ..types.classes.cls_item import Item
from ..types.classes.cls_orderinfo3 import OrderInfo3
from ..types.enums.enm_states import States
from ..types.partial.classes.cls_address import PartialAddress
from ..types.partial.classes.cls_item import PartialItem
from ..types.partial.classes.cls_orderinfo3 import PartialOrderInfo3
from baml_core.provider_manager.llm_response import LLMResponse
from baml_core.stream import AsyncStream
from baml_lib._impl.deserializer import Deserializer


import typing
# Impl: llama2
# Client: Llama2
# An implementation of ExtractOrderInfo3.

__prompt_template = """\
Extract the following information from the TEXT:
{arg}

---
Return the information in JSON following this schema:
{
  "order_id": string,
  // The total price. Don't include shipping costs.
  "total_price": int | null,
  "purchased_items": {
    "name": string,
    "quantity": int
  }[],
  "address_in_text": {
    "street": string,
    // The city name in lowercase
    "city": string | null,
    // The state from the predefined states
    "state": "STATES as string",
    "zip_code": string | null
  }
}

Predefined STATES:
STATES
---
WA
OR
CA

JSON:\
"""

__input_replacers = {
    "{arg}"
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[OrderInfo3](OrderInfo3)  # type: ignore

# Add a deserializer that handles stream responses, which are all Partial types
__partial_deserializer = Deserializer[PartialOrderInfo3](PartialOrderInfo3)  # type: ignore







async def llama2(arg: str, /) -> OrderInfo3:
    response = await Llama2.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized


def llama2_stream(arg: str, /) -> AsyncStream[OrderInfo3, PartialOrderInfo3]:
    def run_prompt() -> typing.AsyncIterator[LLMResponse]:
        raw_stream = Llama2.run_prompt_template_stream(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
        return raw_stream
    stream = AsyncStream(stream_cb=run_prompt, partial_deserializer=__partial_deserializer, final_deserializer=__deserializer)
    return stream

BAMLExtractOrderInfo3.register_impl("llama2")(llama2, llama2_stream)