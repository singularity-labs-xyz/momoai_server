from fastapi import Body
import asyncio
import uuid
from time import sleep
from pydantic import BaseModel

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from main import document_manager

from momoai_core import chains, logging

router = APIRouter(prefix="/chain")

class Message(BaseModel):
    message: str

@router.post("/llm/", response_model=None)
async def llm(message: Message = Body(...)):
    handler = AsyncIteratorCallbackHandler()
    llm_chain = chains.LLMChain(llm=ChatOpenAI(verbose=True, streaming=True, callbacks=[handler]))
    asyncio.create_task(llm_chain.arun(message.message))
    return StreamingResponse(handler.aiter())
