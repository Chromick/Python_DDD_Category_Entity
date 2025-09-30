# events/category_events.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class CategoryEvent:
    """Classe base para eventos de Category"""
    category_id: str
    timestamp: datetime
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now()


@dataclass
class CategoryCreated(CategoryEvent):
    """Evento disparado quando uma Category é criada"""
    name: str
    description: str
    is_active: bool
    
    def __str__(self):
        return f"CategoryCreated(id={self.category_id}, name={self.name}, timestamp={self.timestamp})"


@dataclass
class CategoryUpdated(CategoryEvent):
    """Evento disparado quando uma Category é atualizada"""
    changed_fields: Dict[str, Any]
    
    def __str__(self):
        fields = ", ".join(f"{k}={v}" for k, v in self.changed_fields.items())
        return f"CategoryUpdated(id={self.category_id}, changed_fields=[{fields}], timestamp={self.timestamp})"


@dataclass
class CategoryActivated(CategoryEvent):
    """Evento disparado quando uma Category é ativada"""
    
    def __str__(self):
        return f"CategoryActivated(id={self.category_id}, timestamp={self.timestamp})"


@dataclass
class CategoryDeactivated(CategoryEvent):
    """Evento disparado quando uma Category é desativada"""
    
    def __str__(self):
        return f"CategoryDeactivated(id={self.category_id}, timestamp={self.timestamp})"