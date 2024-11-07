import torch
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/t5-efficient-mini")

output = pipe("Be conversational and talk to me for a bit.")

print(output[0])

new = input()

output = pipe(new)
print(output[0])