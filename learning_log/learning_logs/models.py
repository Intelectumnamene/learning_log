from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """ faz com que, quando um registro do modelo Topic for deletado, todos os registros relacionados na 
    tabela Entry também sejam automaticamente excluídos (efeito de cascata)."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
   
    class Meta:
        """É usada para fornecer metadados sobre o modelo. Influenciam o 
        comportamento do Django em relação ao modelo (como nomes, ordenação padrão, etc.)."""

        verbose_name_plural = 'entries'
        """verbose_name_plural é um atributo da classe Meta que define o nome 
        plural legível do modelo quando exibido no Django Admin e em outras interfaces de usuário."""

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + "..."
        return self.text


# Esse código é uma definição de modelo Django, que representa uma estrutura de dados para uma tabela em um banco de dados. Vamos detalhar cada parte da lógica:

# ### 1. `class Topic(models.Model):`
# Essa linha define uma classe chamada `Topic`, que herda de `models.Model`. [
# Isso significa que a classe `Topic` é um modelo Django, e será traduzida para uma tabela no banco de dados. Cada instância da classe será uma linha na tabela.

# ### 2. `text = models.CharField(max_length=200)`
# Essa linha define um campo de texto chamado `text`. Ele é do tipo `CharField`, que é usado para armazenar pequenas cadeias de texto. O argumento `max_length=200` limita o campo para armazenar no máximo 200 caracteres.

# ### 3. `date_added = models.DateTimeField(auto_now_add=True)`
# Aqui temos um campo `date_added` do tipo `DateTimeField`, usado para armazenar data e hora.
# O argumento `auto_now_add=True` faz com que, toda vez que um novo objeto `Topic` for criado, a data e a hora atuais sejam automaticamente armazenadas nesse campo. Isso é útil para registrar quando o tópico foi adicionado.

# ### 4. `def __str__(self):`Este método define como o objeto será representado como string.
# No Django, o método `__str__` é usado para fornecer uma representação legível do objeto no admin do Django ou em outras interfaces que exibem o objeto.
# Aqui, ele retorna o valor do campo `text`, ou seja, quando o objeto `Topic` for convertido em string (por exemplo, em uma lista de tópicos), será mostrado o valor armazenado no campo `text`.

# ### Resumo
# - O modelo `Topic` tem dois campos: `text` (um campo de texto limitado a 200 caracteres) e `date_added` (que armazena a data e hora de criação).
# - O método `__str__` retorna o conteúdo do campo `text` quando o objeto for exibido como string.

# Esse modelo poderia ser usado, por exemplo, para armazenar tópicos em um sistema de blog ou fórum, onde cada tópico tem um título e uma data de criação.
