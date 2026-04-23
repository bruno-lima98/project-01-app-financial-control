from dataclasses import dataclass, field
from uuid import uuid4
import unicodedata
import re
from datetime import datetime

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


    # Normalização de entrada dos campos str:
    @staticmethod # staticmethod significa um método dentro da classe que não depende da instância (self)
    def normalizar(texto):
        return unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8").lower().replace(" ", "_")
    
    
    # Normalização de entrada do campo date:
    @staticmethod
    def normalizar_data(texto):
        padrao_barra = r"^\d{2}/\d{2}/(?:\d{2}|\d{4})$"
        padrao_convertido = r"^\d{4}-\d{2}-\d{2}$"

        if re.match(padrao_barra, texto):
            return datetime.strptime(texto, "%d/%m/%Y").strftime("%Y-%m-%d")
        elif re.match(padrao_convertido, texto):
            return texto
        
    
    def __post_init__(self):
        self.data = Transacao.normalizar_data(self.data)
        self.tipo = Transacao.normalizar(self.tipo)
        self.categoria = Transacao.normalizar(self.categoria)
        self.fonte = Transacao.normalizar(self.fonte)
        self.valor = float(self.valor)

