import torch
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

print("Running pipeline...", end = " ")
output = generator("Write a poem about cats.")
print("done!\n\n")

print(output[0]['generated_text'])
