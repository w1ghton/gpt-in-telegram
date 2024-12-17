from g4f.client import AsyncClient


async def ai_answer(query, model="gpt-3.5-turbo"):
    client = AsyncClient()

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
    )

    return response.choices[0].message.content
