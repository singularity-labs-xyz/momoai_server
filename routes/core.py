import asyncio
import uuid
from time import sleep
from typing import Any, Coroutine, Optional
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain.callbacks.base import AsyncCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult
from main import chain_manager, document_manager
from utils import streaming

from momoai_core import chains, logging

router = APIRouter(prefix="/core")


@router.get("/llm/{inp}", response_model=None)
async def llm(inp: str):
    handler = streaming.StreamCallbackHandler()
    llm_chain = chain_manager.create_custom_chain(uuid.uuid4(), chains.LLMChain, llm=ChatOpenAI(verbose=True, streaming=True, callbacks=[handler]))

    return await streaming.stream(llm_chain, handler, inp)





