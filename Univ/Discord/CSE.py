import discord
import aiohttp
import asyncio
import os
import ssl

# SSL 검증 비활성화
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

# 봇 클라이언트 생성
client = discord.Client(intents=discord.Intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# 봇 토큰 가져오기
TOKEN = os.getenv('DISCORD_TOKEN')

# 봇 실행
client.run('')
