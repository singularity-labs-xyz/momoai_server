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

from momoai_core import chains, logging, DocumentMetadata

from typing import List

router = APIRouter(prefix="/chains")

class LLMRequestArgs(BaseModel):
    message: str

@router.post("/llm/", response_model=None)
async def llm(args: LLMRequestArgs = Body(...)):
    handler = AsyncIteratorCallbackHandler()
    llm_chain = chains.LLMChain(llm=ChatOpenAI(verbose=True, streaming=True, callbacks=[handler], max_tokens=4000))
    asyncio.create_task(llm_chain.arun(args.message))
    return StreamingResponse(handler.aiter())

class CRRequestArgs(BaseModel):
    user_id: str
    document_ids: List[str]
    message: str

@router.post("/cr/", response_model=None)
async def cr(args: CRRequestArgs = Body(...)):
    handler = AsyncIteratorCallbackHandler()
    document_metadatas = [
        DocumentMetadata(
            id=document_id,
            user_id=None,
            name=None,
        )
        for document_id in args.document_ids
    ]
    retriever = document_manager.get_document_retriever(user_id=args.user_id, document_metadatas=document_metadatas)
    cr_chain = chains.CRChain(retriever=retriever, llm=ChatOpenAI(verbose=True, streaming=True, callbacks=[handler]), max_tokens_limit=3000)
    asyncio.create_task(cr_chain.arun({"question": args.message, "chat_history": []}))
    return StreamingResponse(handler.aiter())
