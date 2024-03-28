from typing import List
from pydantic import BaseModel

import instructor
from openai import OpenAI

client = instructor.patch(OpenAI())

from baml_client import baml as b
import pytest

class Data(BaseModel):
    index: int
    data_type: str
    pii_value: str


def scrub_data(content: str, private_data: List[Data]):
    for i, data in enumerate(private_data):
        content = content.replace(data.pii_value, f"<{data.data_type}_{i}>")

    return content


class PIIDataExtraction(BaseModel):
    """
    Extracted PII data from a document, all data_types should try to have consistent property names. Company names should also be extracted.
    """

    private_data: List[Data]


EXAMPLE_DOCUMENT = """
# Fake Document with PII for Testing PII Scrubbing Model

## Personal Story

John Doe was born on 01/02/1980. His social security number is 123-45-6789. He has been using the email address john.doe@email.com for years, and he can always be reached at 555-123-4567.

## Residence

John currently resides at 123 Main St, Springfield, IL, 62704. He's been living there for about 5 years now.

## Career

At the moment, John is employed at Company Acme. He started his role as a Software Engineer in January 2015 and has been with the company since then.
"""


expected_pii = [
    "01/02/1980",
    "123-45-6789",
    "john.doe@email.com",
    "555-123-4567",
    "123 Main St, Springfield, IL, 62704",
]


# Scrub the PII Data from the document
@pytest.mark.asyncio
def test_instructor_pii():
    # Define the PII Scrubbing Model
  pii_data: PIIDataExtraction = client.chat.completions.create(
      model="gpt-3.5-turbo",
      response_model=PIIDataExtraction,
      messages=[
          {
              "role": "system",
              "content": "You are a world class PII scrubbing model, Extract the PII data from the following document",
          },
          {
              "role": "user",
              "content": EXAMPLE_DOCUMENT,
          },
      ],
  )  # type: ignore

  print(pii_data.model_dump_json(indent=2))
  scrubbed_data = scrub_data(EXAMPLE_DOCUMENT, pii_data.private_data)
  print(scrubbed_data)
  pii_vaues = [obj.pii_value for obj in pii_data.private_data]


  

@pytest.mark.asyncio
async def test_baml_pii():
    # Define the PII Scrubbing Model
  pii_data = await b.ExtractPII(EXAMPLE_DOCUMENT)
  print(pii_data)
  
  scrubbed_data = scrub_data(EXAMPLE_DOCUMENT, pii_data) #type: ignore
  print(scrubbed_data)
  pii_vaues = [obj.pii_value for obj in pii_data]
  assert pii_vaues == expected_pii
  
