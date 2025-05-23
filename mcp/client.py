from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession




from fastmcp import Client
import asyncio
async def main():
    # Connect via stdio to a local script
    # async with Client("my_server.py") as client:
    #     tools = await client.list_tools()
    #     print(f"Available tools: {tools}")
    #     result = await client.call_tool("add", {"a": 5, "b": 3})
    #     print(f"Result: {result.text}")

    # Connect via SSE
    async with Client("http://localhost:9998/mcp") as client:
        # ... use the client
        result =  await client.list_tools()
        # print(await client.call_tool("add", {"a": 5, "b": 3}))
        print(f"Available tools: {result}")

asyncio.run(main())