# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_orderinfo import OrderInfo
from ..types.partial.classes.cls_orderinfo import PartialOrderInfo
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IExtractOrderInfoOutput = OrderInfo

@runtime_checkable
class IExtractOrderInfo(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        OrderInfo
    """

    async def __call__(self, arg: str, /) -> OrderInfo:
        ...

   

@runtime_checkable
class IExtractOrderInfoStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[OrderInfo, PartialOrderInfo]
    """

    def __call__(self, arg: str, /) -> AsyncStream[OrderInfo, PartialOrderInfo]:
        ...
class IBAMLExtractOrderInfo(BaseBAMLFunction[OrderInfo, PartialOrderInfo]):
    def __init__(self) -> None:
        super().__init__(
            "ExtractOrderInfo",
            IExtractOrderInfo,
            ["v1"],
        )

    async def __call__(self, *args, **kwargs) -> OrderInfo:
        return await self.get_impl("v1").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[OrderInfo, PartialOrderInfo]:
        res = self.get_impl("v1").stream(*args, **kwargs)
        return res

BAMLExtractOrderInfo = IBAMLExtractOrderInfo()

__all__ = [ "BAMLExtractOrderInfo" ]
