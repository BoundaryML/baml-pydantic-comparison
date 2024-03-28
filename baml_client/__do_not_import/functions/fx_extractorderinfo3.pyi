# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_address import Address
from ..types.classes.cls_item import Item
from ..types.classes.cls_orderinfo3 import OrderInfo3
from ..types.enums.enm_states import States
from ..types.partial.classes.cls_address import PartialAddress
from ..types.partial.classes.cls_item import PartialItem
from ..types.partial.classes.cls_orderinfo3 import PartialOrderInfo3
from baml_core.stream import AsyncStream
from typing import Callable, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IExtractOrderInfo3Output = OrderInfo3

@runtime_checkable
class IExtractOrderInfo3(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        OrderInfo3
    """

    async def __call__(self, arg: str, /) -> OrderInfo3:
        ...

   

@runtime_checkable
class IExtractOrderInfo3Stream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[OrderInfo3, PartialOrderInfo3]
    """

    def __call__(self, arg: str, /) -> AsyncStream[OrderInfo3, PartialOrderInfo3]:
        ...
class BAMLExtractOrderInfo3Impl:
    async def run(self, arg: str, /) -> OrderInfo3:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[OrderInfo3, PartialOrderInfo3]:
        ...

class IBAMLExtractOrderInfo3:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IExtractOrderInfo3, IExtractOrderInfo3Stream], None]:
        ...

    async def __call__(self, arg: str, /) -> OrderInfo3:
        ...

    def stream(self, arg: str, /) -> AsyncStream[OrderInfo3, PartialOrderInfo3]:
        ...

    def get_impl(self, name: ImplName) -> BAMLExtractOrderInfo3Impl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the ExtractOrderInfo3Interface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.ExtractOrderInfo3.mock() as mocked:
                    mocked.return_value = ...
                    result = await ExtractOrderInfo3Impl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractOrderInfo3Interface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.ExtractOrderInfo3.test
            async def test_logic(ExtractOrderInfo3Impl: IExtractOrderInfo3) -> None:
                result = await ExtractOrderInfo3Impl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractOrderInfo3Interface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.ExtractOrderInfo3.test(exclude_impl=["implname"])
            async def test_logic(ExtractOrderInfo3Impl: IExtractOrderInfo3) -> None:
                result = await ExtractOrderInfo3Impl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.ExtractOrderInfo3.test(stream=True)
            async def test_logic(ExtractOrderInfo3Impl: IExtractOrderInfo3Stream) -> None:
                async for result in ExtractOrderInfo3Impl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractOrderInfo3Interface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.ExtractOrderInfo3.test
        class TestClass:
            def test_a(self, ExtractOrderInfo3Impl: IExtractOrderInfo3) -> None:
                ...
            def test_b(self, ExtractOrderInfo3Impl: IExtractOrderInfo3) -> None:
                ...
        ```
        """
        ...

BAMLExtractOrderInfo3: IBAMLExtractOrderInfo3
