from g4f.client import Client

client = Client()
response = client.images.generate(
  model="flux",
  prompt="a very cute anime girl",
  width=777,
  height=1024
)
image_url = response.data[0].url
print(image_url)
