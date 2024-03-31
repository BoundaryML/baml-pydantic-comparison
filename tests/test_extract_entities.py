from typing import List
from pydantic import BaseModel

import instructor
from openai import OpenAI
from baml_client.baml_types import ComplexRestorationProject, TimePeriod, MaterialOrigin, ManuscriptState

import logging
logging.basicConfig(level=logging.DEBUG)

client = instructor.patch(OpenAI())

from baml_client import baml as b
import pytest



tests = [
"""\
A document from the time when Europe was rediscovering classical philosophies, thought to originate from a region known for its scholars, holds significant insights into the period's societal norms. The material, predominantly natural, includes inks derived from historical recipes and bindings consistent with the era's techniques. Restoration efforts focused on methods that are both physical, like cleaning and mending, and digital, for future generations. Initially described as worn but intact, the document now stands as a testament to enduring history, though some minor textual clarity issues remain. Preservation actions emphasized both the tangible and intangible heritage.\
""",
"""
A series of writings from an era marked by profound philosophical questioning, believed to have originated from a confluence of cultures, provides rare insights into ancient debates. These writings, preserved on materials blending both traditional and innovative practices, feature a mix of known and obscure substances for ink and binding, hinting at a fusion of techniques. Efforts to rejuvenate these pieces have spanned the gamut from manual, tactile restorations to cutting-edge, digital archiving, aiming to bridge past and present. The initial assessment painted a picture of resilience amidst degradation, with subsequent treatments elevating their status, albeit leaving behind subtle marks of their journey. The drive for preservation has been holistic, touching on the physical and the digital realms
"""
]


@pytest.mark.asyncio
def test_instructor_extract_entities():
  output: ComplexRestorationProject = client.chat.completions.create(
      model="gpt-4",
      response_model=ComplexRestorationProject,
      messages=[
          {
              "role": "user",
              "content": 
f"""
Given the following restoration project document, analyze the details and return the desired output.

Document:
---
{tests[0]}
---""",
          },
      ],
  )  # type: ignore

  print(output.model_dump_json(indent=2))
  assert output.context.timePeriod ==  TimePeriod.RENAISSANCE


@pytest.mark.asyncio
async def test_baml_extract_entities():
  output = await b.AnalyzeRestorationProject(tests[0])
  assert output.context.timePeriod ==  TimePeriod.RENAISSANCE
    
