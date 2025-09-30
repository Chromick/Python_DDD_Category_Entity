# main.py - Demonstração das funcionalidades da entidade Category
from domain.category import Category
import json

def print_separator(title):
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def main():
    print_separator("DEMONSTRAÇÃO DA ENTIDADE CATEGORY")
    
    # 1. Criação de uma categoria
    print_separator("1. CRIAÇÃO DE CATEGORIA")
    categoria = Category(name="Drama", description="Filmes de drama")
    print(f"Categoria criada: {categoria}")
    print(f"ID: {categoria.id}")
    print(f"Eventos registrados: {len(categoria.events)}")
    for event in categoria.events:
        print(f"  - {event}")
    
    # 2. Serialização
    print_separator("2. SERIALIZAÇÃO (to_dict)")
    categoria_dict = categoria.to_dict()
    print("Dicionário gerado:")
    print(json.dumps(categoria_dict, indent=2, ensure_ascii=False))
    
    # 3. Reconstrução (from_dict)
    print_separator("3. RECONSTRUÇÃO (from_dict)")
    categoria_reconstruida = Category.from_dict(categoria_dict)
    print(f"Categoria reconstruída: {categoria_reconstruida}")
    print(f"ID original: {categoria.id}")
    print(f"ID reconstruído: {categoria_reconstruida.id}")
    print(f"São equivalentes? {categoria.id == categoria_reconstruida.id and categoria.name == categoria_reconstruida.name}")
    
    # 4. Atualização
    print_separator("4. ATUALIZAÇÃO DE CATEGORIA")
    print("Estado antes da atualização:")
    print(f"  Nome: {categoria.name}")
    print(f"  Descrição: {categoria.description}")
    print(f"  Eventos: {len(categoria.events)}")
    
    categoria.update(name="Drama Clássico", description="Filmes de drama clássico")
    print("\nApós atualização:")
    print(f"  Nome: {categoria.name}")
    print(f"  Descrição: {categoria.description}")
    print(f"  Eventos: {len(categoria.events)}")
    print("Último evento:")
    print(f"  - {categoria.events[-1]}")
    
    # 5. Desativação
    print_separator("5. DESATIVAÇÃO DE CATEGORIA")
    print(f"Status antes: {categoria.is_active}")
    categoria.deactivate()
    print(f"Status depois: {categoria.is_active}")
    print(f"Eventos: {len(categoria.events)}")
    print("Último evento:")
    print(f"  - {categoria.events[-1]}")
    
    # 6. Ativação
    print_separator("6. ATIVAÇÃO DE CATEGORIA")
    print(f"Status antes: {categoria.is_active}")
    categoria.activate()
    print(f"Status depois: {categoria.is_active}")
    print(f"Eventos: {len(categoria.events)}")
    print("Último evento:")
    print(f"  - {categoria.events[-1]}")
    
    # 7. Histórico completo de eventos
    print_separator("7. HISTÓRICO COMPLETO DE EVENTOS")
    print(f"Total de eventos registrados: {len(categoria.events)}")
    for i, event in enumerate(categoria.events, 1):
        print(f"{i}. {event}")
    
    # 8. Teste de serialização com categoria atualizada
    print_separator("8. SERIALIZAÇÃO FINAL")
    categoria_final_dict = categoria.to_dict()
    print("Estado final serializado:")
    print(json.dumps(categoria_final_dict, indent=2, ensure_ascii=False))
    
    # 9. Teste de múltiplas categorias
    print_separator("9. TESTE COM MÚLTIPLAS CATEGORIAS")
    categorias = [
        Category(name="Ação", description="Filmes de ação"),
        Category(name="Comédia", description="Filmes de comédia", is_active=False),
        Category(name="Terror")
    ]
    
    for i, cat in enumerate(categorias, 1):
        print(f"Categoria {i}: {cat}")
        print(f"  Eventos: {len(cat.events)}")
    
    # Operações nas categorias
    categorias[1].activate()  # Ativar comédia
    categorias[2].update(description="Filmes de terror e suspense")  # Atualizar terror
    
    print("\nApós operações:")
    for i, cat in enumerate(categorias, 1):
        print(f"Categoria {i}: {cat}")
        print(f"  Eventos: {len(cat.events)}")
        print(f"  Último evento: {cat.events[-1] if cat.events else 'Nenhum'}")

if __name__ == "__main__":
    main()