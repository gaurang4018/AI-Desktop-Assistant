# API key = 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

import os
import openai
from openai import enable_telemetry

OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

prompt="bharuch\n\nBharuch is a city located in the Indian state of Gujarat. It is located on the bank of the Narmada River."

def openai_create(prompt):

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=0.7,
    max_tokens=30,
    top_p=1,
    frequency_penalty=0,    
    presence_penalty=0.6
  )        
  
  return response.choices[0].text

def chatGptClone(input):
  try:
    if input == "none":
      return 
    op =   openai_create(input)
    return op
  except:
    if input == "none":
      return 
    return "Sorry ! try again"