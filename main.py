import discord
import openai

openai.api_key = "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"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$code'):
        openai.api_key = "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"
        response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"\"\"\"\n{message.content})\n\"\"\"\n",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
        )
        await message.channel.send(response.choices[0].text)

client.run('MTA1MTgzNTkzNTQyNTMwMjU3OA.GL43NI.MJPWr0WDzsCDxsJnedZzjHcWK2BJ2rzxpAKh2A')