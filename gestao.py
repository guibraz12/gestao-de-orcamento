import pandas as pd
import matplotlib.pyplot as plt

orcamento = {
    'Categoria': ['Salários', 'Aluguel', 'Marketing', 'Tecnologia', 'Outros'],
    'Valor': [50000, 10000, 20000, 5000, 12000]
}

df = pd.DataFrame(orcamento)

plt.figure(figsize=(5, 5))
plt.pie(df['Valor'], labels=df['Categoria'],
        autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Distribuição de Gastos\n')
plt.show()