from fastapi import APIRouter
from src.dto.document import CreateDocumentRequest, ModifyDocumentRequest
import src.service.document as document_service

router = APIRouter()

@router.get("")
def get_documents():
    return document_service.get_documents()

@router.get("/{id}")
def get_document(id: int):
    return document_service.get_document(id)

@router.post("", status_code=201)
def create(document: CreateDocumentRequest):
    document_service.create_document(document.to_orm())
    return "ok"

@router.put("/{id}")
def modify(document: ModifyDocumentRequest):
    document_service.modify_document(document.to_orm())
    return "ok"

@router.delete("/{id}")
def remove(id: int):
    document_service.remove_document(id)
    return "ok"