import asyncio
import uuid
from time import sleep

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from main import document_manager

from momoai_core import chains, logging

router = APIRouter(prefix="/core")


@router.get("/llm/{inp}", response_model=None)
async def llm(inp: str):
    handler = AsyncIteratorCallbackHandler()
    llm_chain = chains.LLMChain(llm=ChatOpenAI(verbose=True, streaming=True, callbacks=[handler]))
    asyncio.create_task(llm_chain.arun(inp))
    return StreamingResponse(handler.aiter())
