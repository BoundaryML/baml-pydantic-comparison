# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ...classes.cls_address import Address
from ...classes.cls_item import Item
from ...enums.enm_states import States
from baml_lib._impl.deserializer import register_deserializer
from pydantic import BaseModel
from typing import List, Optional


@register_deserializer({ "order_id": "id","total_price": "price","purchased_items": "items","address_in_text": "shipping_address", })
class PartialOrderInfo3(BaseModel):
    id: Optional[str] = None
    price: Optional[int] = None
    items: List[Item]
    shipping_address: Optional[Address] = None
