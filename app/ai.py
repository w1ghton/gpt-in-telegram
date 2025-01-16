from g4f.client import AsyncClient


async def ai_answer(
    query,
    model="gpt-3.5-turbo",
    params="use bold text instead of headings, don't use escaping and special markdown characters.",
):
    client = AsyncClient()

    messages = [
        {"role": "system", "content": params},
        {"role": "user", "content": query},
    ]

    response = await client.chat.completions.create(
        model=model,  # models here: https://platform.openai.com/docs/models
        messages=messages,
    )

    return response.choices[0].message.content
