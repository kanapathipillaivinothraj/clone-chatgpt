import openai

openai.api_key = "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"
while True:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(input("What Do You Want: ")),
        temperature=0.3,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    print(response["choices"][0]["text"])
