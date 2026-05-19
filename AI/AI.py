from openai import OpenAI
client = OpenAI(
    api_key="a5de6gds5ftj4fhj5rgds9s7f4s2s6dg5hd4w5ds6ses4f4d5s"
)

response = client.responses.create(
    model="gpt-5.5",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)


