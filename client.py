# from openai import OpenAI
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="sk-svcacct-afo9Uoy0aZ95gzu1N0mSNCLWsNfCWNOP1UkFKloJ435xzEAS5nvnkpUWL7JJfAT3BlbkFJY0PPqBOdGT1cFmKGCrr2ufNB0rS-oxtjEETqrZaWFuD47jCnQ_HVp3oqGF4sIA",
# )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)


# LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg

import cohere

co = cohere.Client("LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg")  # Replace with your API key

# First prompt
response1 = co.generate(
    model="command-xlarge-nightly",
    prompt="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud.",
    max_tokens=50
)
print("Response 1:")
print(response1.generations[0].text)

# Second prompt
response2 = co.generate(
    model="command-xlarge-nightly",
    prompt="What is coding?",
    max_tokens=50
)
print("\nResponse 2:")
print(response2.generations[0].text)
