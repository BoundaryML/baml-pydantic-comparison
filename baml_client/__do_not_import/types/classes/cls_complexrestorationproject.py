# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..enums.enm_manuscriptstate import ManuscriptState
from ..enums.enm_materialorigin import MaterialOrigin
from ..enums.enm_timeperiod import TimePeriod
from .cls_manuscriptcondition import ManuscriptCondition
from .cls_manuscriptcontext import ManuscriptContext
from .cls_restoration import Restoration
from baml_lib._impl.deserializer import register_deserializer
from pydantic import BaseModel
from typing import List, Optional


@register_deserializer({  })
class ComplexRestorationProject(BaseModel):
    id: str
    title: str
    context: ManuscriptContext
    materials: Restoration
    condition: ManuscriptCondition
    actionsTaken: List[str]
    unresolvedIssues: List[str]
    isComplete: bool
