from pydantic import BaseModel
from src.model.document import Document

class CreateDocumentRequest(BaseModel):
    id: int | None = None
    content: str

    def to_orm(self) -> Document:
      return Document(id=self.id, content=self.content)
    
class ModifyDocumentRequest(BaseModel):
    id: int
    content: str

    def to_orm(self) -> Document:
      return Document(id=self.id, content=self.content)