import torch
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/t5-efficient-mini")

output = pipe("Be conversational and talk to me for a bit.")

print(output[0])

new = input()

output = pipe(new)
print(output[0])


# query
# takes in user input string and anxiety level, and uses it to generate text using text2text
def gen_query(user_inp, anx):
    output = pipe(f"""
    
    You are a health anxiety chatbot that is serving a user. Give a reasonable assessment of the following query: {user_inp}
    \nContext: The user is current anxious level {anx} on a scale of 1 to 10, so remain mindful of tone.
    
    Remind the user that you cannot diagnose as a chatbot if asked anything pertaining diagnosis.""")
    return output

def symptom_query(user_inp, anx):
    condition = input("Tell me what you believe you are experiencing: ")
    symptoms = input("\nGive me a list of all symptoms you are experiencing separated by commas: ").split(",")
    
    output = pipe(f"""
    You are a health anxiety chatbot that is serving a user, currently by evaluating their list of symptoms against what they think they have.

    Context: The current user is anxious level {anx} on a scale of 1 to 10, so be mindful of their current stress level.
    The condition they believe they have is {condition}.
    The symptoms they have are as follows: {symptoms}.

    Try to rationalize their judgment of condition and if there are possibly leaps in logic due to stress, or if symptoms may not necessarily be representative of the condition.
    """)
    return output

