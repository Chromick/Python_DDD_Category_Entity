#domain/category.py
import uuid
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

# Que o nome vai ser <= que 255
MAX_NAME = 255

@dataclass
class Category:
    """
    Entidade Category(sem Framework)
    - name(obrigatório) e <= 255
    - id/description/is_active (opcionais)
    - is_active default = True
    - gera o id automaticamente (uuid4) se não for informado
    - permitir o update(name/description) e desactivar
    """
    name: str
    description: str = ""
    is_active: bool = True
    id: Optional[str] = field(default=None)
    events: list = field(default_factory=list, init=False)
#Construtor Inteligente
    def __post_init__(self):
        #gera o id se não vier um
        if not self.id:
            self.id = str(uuid.uuid4())
        #validar e normalizar os dados
        self.name = self._validate_name(self.name)
        self.description = self.description or ""
        self.is_active = bool(self.is_active)
        
        # Registrar evento de criação
        from events.category_events import CategoryCreated
        self.events.append(CategoryCreated(
            category_id=self.id,
            timestamp=None,  # será preenchido automaticamente
            name=self.name,
            description=self.description,
            is_active=self.is_active
        ))
    
    @staticmethod
    def _validate_name(name: str)-> str:
        if not isinstance(name, str):
            raise ValueError("name deve ser string")
        n = name.strip()
        if not n:
            raise ValueError("name é obrigatório")
        if len(n)> MAX_NAME:
            raise ValueError(f"name deve ter no máximo {MAX_NAME} caracteres")
        return n
    #Comportamentos do Domínio

    def update(self, *, name: Optional[str]= None, description: Optional[str]=None) -> None:
        changed_fields = {}
        
        if name is not None:
            old_name = self.name
            self.name = self._validate_name(name)
            if old_name != self.name:
                changed_fields["name"] = {"old": old_name, "new": self.name}
                
        if description is not None:
            old_description = self.description
            self.description = description
            if old_description != self.description:
                changed_fields["description"] = {"old": old_description, "new": self.description}
        
        # Registrar evento de atualização se houve mudanças
        if changed_fields:
            from events.category_events import CategoryUpdated
            self.events.append(CategoryUpdated(
                category_id=self.id,
                timestamp=None,  # será preenchido automaticamente
                changed_fields=changed_fields
            ))
    
    def activate(self)-> None:
        if not self.is_active:  # Só registra evento se realmente mudou
            self.is_active = True
            from events.category_events import CategoryActivated
            self.events.append(CategoryActivated(
                category_id=self.id,
                timestamp=None  # será preenchido automaticamente
            ))

    def deactivate(self)-> None:
        if self.is_active:  # Só registra evento se realmente mudou
            self.is_active = False
            from events.category_events import CategoryDeactivated
            self.events.append(CategoryDeactivated(
                category_id=self.id,
                timestamp=None  # será preenchido automaticamente
            ))
    
    #Logs e Depuração
    def __str__(self)-> str:
        return f"{self.name} | {self.description} ({self.is_active})"
    
    def __repr__(self)-> str:
        return f"<Category {self.name} ({self.id})>"
    
    # Métodos de Serialização
    def to_dict(self) -> Dict[str, Any]:
        """Converte a entidade Category para um dicionário"""
        return {
            "class_name": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_active": self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Category':
        """Reconstrói uma instância Category a partir de um dicionário"""
        return cls(
            id=data.get("id"),
            name=data["name"],
            description=data.get("description", ""),
            is_active=data.get("is_active", True)
        )