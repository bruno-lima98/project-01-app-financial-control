from dataclasses import dataclass, field
from uuid import uuid4

# Criando a classe de transação para uso no projeto

@dataclass
class Transacao:
    # Campos obrigatórios não possuem valor padrão e devem vir antes:
    data: str
    tipo: str
    categoria: str
    fonte: str
    valor: float

    # Campos com valor padrão (automático ou opicional) devem vir depois: 
    id: str = field(default_factory=lambda: str(uuid4()))
    descricao: str = "" # como esse campo é opicional, precisa de um valor padrão
