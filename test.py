import openai

openai.api_key = "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"
response = openai.Completion.create(
  model="code-davinci-002",
  prompt="\"\"\"\ncreate a function to count sum\n\"\"\"\n",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)
print(response.choices[0].text)
