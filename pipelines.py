import torch
from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-large")

# TODO: interactions with data to properly provide accurate information.

# TODO: testing prompts in depth
def gen_query(user_inp, anx):
    output = pipe(f"""
    You are a health anxiety chatbot that is serving a user. Give a reasonable assessment of the following query, and elaborate upon your reasoning without giving the prompt back: {user_inp}
    \nContext: The user is current anxious level {anx} on a scale of 1 to 10, so remain mindful of tone.
    The user wants to be addressed conversationally, so use the pronoun "you".
    Remind the user of strategies to rationalize and reduce feelings of anxiety.
    Remind the user that you cannot diagnose as a chatbot if asked anything pertaining diagnosis.""", max_length = 500)
    return output[0]['generated_text']

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
    return output[0]['generated_text']

# TODO: method for general talking 
def general(user_inp, anx):
    output = pipe(f"""
    You are a health anxiety chatbot that is serving a user.
    Your current task is listening to your user's request and answering accordingly based on the information you have.
    If you believe you have insufficient information, reply as such.

    Request from user: {user_inp}

    Context: The current user is anxious level {anx} on a scale of 1 to 10, so be mindful of their current stress level.

    Try to rationalize their judgment of condition and if there are possibly leaps in logic due to stress, or if symptoms may not necessarily be representative of the condition.
    """)
    #return output[0]['generated_text']
