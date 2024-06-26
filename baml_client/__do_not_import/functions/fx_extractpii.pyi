# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_piidata import PIIData
from ..types.partial.classes.cls_piidata import PartialPIIData
from baml_core.stream import AsyncStream
from typing import Callable, List, Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["v1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IExtractPIIOutput = List[PIIData]

@runtime_checkable
class IExtractPII(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        List[PIIData]
    """

    async def __call__(self, arg: str, /) -> List[PIIData]:
        ...

   

@runtime_checkable
class IExtractPIIStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[List[PIIData], List[PIIData]]
    """

    def __call__(self, arg: str, /) -> AsyncStream[List[PIIData], List[PIIData]]:
        ...
class BAMLExtractPIIImpl:
    async def run(self, arg: str, /) -> List[PIIData]:
        ...
    
    def stream(self, arg: str, /) -> AsyncStream[List[PIIData], List[PIIData]]:
        ...

class IBAMLExtractPII:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IExtractPII, IExtractPIIStream], None]:
        ...

    async def __call__(self, arg: str, /) -> List[PIIData]:
        ...

    def stream(self, arg: str, /) -> AsyncStream[List[PIIData], List[PIIData]]:
        ...

    def get_impl(self, name: ImplName) -> BAMLExtractPIIImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the ExtractPIIInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.ExtractPII.mock() as mocked:
                    mocked.return_value = ...
                    result = await ExtractPIIImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractPIIInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.ExtractPII.test
            async def test_logic(ExtractPIIImpl: IExtractPII) -> None:
                result = await ExtractPIIImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName] = [], stream: bool = False) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractPIIInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.
            stream: bool
                If set, will return a streamable version of the test function.

        Usage:
            ```python
            # All implementations except the given impl will be tested.

            @baml.ExtractPII.test(exclude_impl=["implname"])
            async def test_logic(ExtractPIIImpl: IExtractPII) -> None:
                result = await ExtractPIIImpl(...)
            ```

            ```python
            # Streamable version of the test function.

            @baml.ExtractPII.test(stream=True)
            async def test_logic(ExtractPIIImpl: IExtractPIIStream) -> None:
                async for result in ExtractPIIImpl(...):
                    ...
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the ExtractPIIInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.ExtractPII.test
        class TestClass:
            def test_a(self, ExtractPIIImpl: IExtractPII) -> None:
                ...
            def test_b(self, ExtractPIIImpl: IExtractPII) -> None:
                ...
        ```
        """
        ...

BAMLExtractPII: IBAMLExtractPII
