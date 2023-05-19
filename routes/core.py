from fastapi import APIRouter
from momoai_core import logging
from momoai_core import chains
from main import chain_manager
from main import document_manager
from fastapi.responses import StreamingResponse
from langchain.callbacks.base import AsyncCallbackHandler
from typing import Any
from langchain.chat_models import ChatOpenAI
from time import sleep
import asyncio


router = APIRouter(prefix="/core")

class StreamCallbackHandler(AsyncCallbackHandler):
    """Callback handler for streaming. Only works with LLMs that support streaming."""

    def __init__(self) -> None:
        self.queue = []

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        self.queue.insert(0, token)

    async def get_stream(self) -> str:
        """Returns a stream of tokens from the LLM."""
        while True:
            if len(self.queue) != 0:
                sleep(0.1)
                token = self.queue.pop()
                logging.info("token: %s", token)
                if token == None:
                    break
                yield token
            else:
                break



@router.get("/llm/{inp}", response_model=None)
async def llm(inp: str):
    handler = StreamCallbackHandler()
    llm_chain = chain_manager.create_custom_chain(1, chains.LLMChain, llm = ChatOpenAI(verbose=True, streaming=True, callbacks=[handler]))
    llm_chain.run(inp)
    return StreamingResponse(handler.get_stream())
    #{"message": chain_manager.default_chains["llm"].run(inp)}

