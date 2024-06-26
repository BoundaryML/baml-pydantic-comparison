# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..__do_not_import.generated_baml_client import baml
from ..baml_types import Education, IExtractResume, IExtractResumeStream, Resume
from baml_lib._impl.deserializer import Deserializer
from json import dumps
from pytest_baml.ipc_channel import BaseIPCChannel
from typing import Any


@baml.ExtractResume.test(stream=True)
async def test_jason(ExtractResumeImpl: IExtractResumeStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    content = to_str("Jason Doe\nPython, Rust\nUniversity of California, Berkeley, B.S.\nin Computer Science, 2020\nAlso an expert in Tableau, SQL, and C++\n")
    deserializer = Deserializer[str](str) # type: ignore
    param = deserializer.from_string(content)
    async with ExtractResumeImpl(param) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()

@baml.ExtractResume.test(stream=True)
async def test_sarah(ExtractResumeImpl: IExtractResumeStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    content = to_str("Sarah Montez\nHarvard University\nMay 2015-2019\n3.92 GPA\nGoogle\nSoftware Engineer\nJune 2019-Present\n- Backend engineer\n- Rewrote search and uplifted metrics by 120%\n- Used C++ and Python\nMicrosoft\nSoftware Intern\nJune 2018-August 2018\n- Worked on the Windows team\n- Updated the UI\n- Used C++\n")
    deserializer = Deserializer[str](str) # type: ignore
    param = deserializer.from_string(content)
    async with ExtractResumeImpl(param) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()

