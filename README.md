<<<<<<< HEAD
RESUMO DAS PRINCIPAIS FUNCIONALIDADES MINISTRADAS - P1 BACK-END
================================================================

1. @STATICMETHOD
===============
- Método que pertence à classe, mas não precisa de uma instância para ser chamado
- Não recebe 'self' como parâmetro
- Usado para funcionalidades utilitárias relacionadas à classe
- Exemplo na Category: _validate_name() - valida o nome sem precisar de uma instância

Características:
• Não acessa atributos da instância (self)
• Não acessa atributos da classe (cls)
• Pode ser chamado diretamente pela classe: Category._validate_name("teste")
• Útil para validações e operações auxiliares

2. DATACLASSES
==============
- Decorator que automatiza a criação de classes com métodos especiais
- Gera automaticamente __init__, __repr__, __eq__, etc.
- Reduz código boilerplate significativamente
- Usado na entidade Category e nos eventos

Funcionalidades principais:
• @dataclass - decorator principal
• field() - para configurações especiais de atributos
• field(default_factory=list) - para valores mutáveis como listas
• field(init=False) - para atributos não incluídos no __init__
• Suporte a type hints nativo

Exemplo:
@dataclass
class Category:
    name: str
    description: str = ""
    events: list = field(default_factory=list, init=False)

3. EVENTOS DE DOMÍNIO
====================
- Padrão para capturar e registrar mudanças importantes na entidade
- Permite rastreamento do histórico de operações
- Facilita integração com outros sistemas (auditoria, notificações)
- Implementado através de classes específicas para cada tipo de evento

Eventos implementados:
• CategoryCreated - quando uma categoria é criada
• CategoryUpdated - quando atributos são modificados
• CategoryActivated - quando uma categoria é ativada
• CategoryDeactivated - quando uma categoria é desativada

Características:
• Cada evento possui timestamp automático
• Eventos são armazenados em uma lista interna (self.events)
• Contêm informações relevantes sobre a operação realizada
• Seguem o padrão de nomenclatura: [Entidade][Ação]

4. DECORADORES
==============
- Funções que modificam ou estendem o comportamento de outras funções/classes
- Aplicados usando a sintaxe @decorator
- Muito utilizados em Python para funcionalidades transversais

Tipos utilizados no projeto:
• @dataclass - automatiza criação de classes
• @staticmethod - define métodos estáticos
• @classmethod - define métodos de classe (usado em from_dict)

Sintaxe:
@decorator
def funcao():
    pass

# Equivale a:
def funcao():
    pass
funcao = decorator(funcao)

5. DDD (DOMAIN-DRIVEN DESIGN)
=============================
- Abordagem de desenvolvimento focada no domínio do negócio
- Entidades representam conceitos centrais do domínio
- Comportamentos ficam encapsulados nas próprias entidades

Conceitos aplicados:
• Entidade - objeto com identidade única (Category com ID)
• Comportamentos de domínio - métodos que representam ações do negócio
• Validações de domínio - regras de negócio na própria entidade
• Eventos de domínio - captura de mudanças importantes
• Serialização - conversão para formatos de transporte/persistência

Princípios seguidos:
• Encapsulamento - dados e comportamentos juntos
• Validação - regras de negócio na entidade
• Imutabilidade controlada - mudanças através de métodos específicos
• Rastreabilidade - histórico através de eventos

FUNCIONALIDADES IMPLEMENTADAS NA CATEGORY:
==========================================

Serialização:
• to_dict() - converte entidade para dicionário
• from_dict() - reconstrói entidade a partir de dicionário
• Inclui class_name para identificação do tipo

Sistema de Eventos:
• Lista interna de eventos (self.events)
• Registro automático em todas as operações
• Timestamp automático em cada evento
• Informações detalhadas sobre mudanças

Validações:
• Nome obrigatório e com limite de caracteres
• Normalização automática de dados
• Validação no momento da criação e atualização

Comportamentos:
• Criação com ID automático (UUID4)
• Atualização controlada de atributos
• Ativação/desativação com controle de estado
• Representação textual (__str__ e __repr__)

Esta implementação demonstra como combinar conceitos modernos de Python
(dataclasses, decoradores) com padrões de DDD para criar entidades
robustas e bem estruturadas.
=======
# Python_DDD_Category_Entity
>>>>>>> f5f62a2544691219cf1eab62f0e924bd2aaf0e00
