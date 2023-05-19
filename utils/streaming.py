import asyncio
from typing import Any, Coroutine, Optional
from uuid import UUID

from fastapi.responses import StreamingResponse
from langchain.callbacks.base import AsyncCallbackHandler
from langchain.schema import LLMResult


class StreamCallbackHandler(AsyncCallbackHandler):
    """Callback handler for streaming. Only works with LLMs that support streaming."""

    def __init__(self) -> None:
        self.queue = asyncio.Queue()

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        await self.queue.put(token)

    async def get_stream(self) -> str:
        """Returns a stream of tokens from the LLM."""
        while True:
            token = await self.queue.get()
            if token == None:
                break
            else:
                yield token

    async def on_llm_end(self, response: LLMResult, *, run_id: UUID, parent_run_id: UUID or None = None, **kwargs: Any) -> Coroutine[Any, Any, None]:
        await self.queue.put(None)
        return await super().on_llm_end(response, run_id=run_id, parent_run_id=parent_run_id, **kwargs)

async def stream(chain, handler, inp="test"):
        asyncio.create_task(await chain.arun(inp))
        return StreamingResponse(handler.get_stream(), media_type="text/plain")