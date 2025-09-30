from domain.category import Category

c1 = Category(name="Drama")
c2 = Category(name="Ação", description="Filmes de Ação")
c3 = Category(name="Comédia", description="Filmes de Comédia", is_active=False)

print(c1.description)
print(c2)
print(c3)
c3.activate()
print(c3)
"""
Drama |  (True)
Ação | Filmes de Ação (True)
Comédia | Filmes de Comédia (False)
Comédia | Filmes de Comédia (True)
"""