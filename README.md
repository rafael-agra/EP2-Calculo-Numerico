# EP2‑Cálculo Numérico 

Segundo Exercício Programa (EP2) da disciplina **MAC0210 – Métodos Numéricos** da Escola Politécnica, Universidade de São Paulo. O projeto demonstra a utilização de **Quadratura de Gauss** para calcular integrais duplas em diversas situações geométricas.

## Índice 📑
- Descrição 📝  
- Pré‑requisitos ⚙️  
- Estrutura do Projeto 🗂️  
- Instalação 🔧  
- Uso 🚀  
- Exemplos 💻  
- Funções Disponíveis 🔍  
- Licença 📜  

## Descrição 📝
O arquivo **EP2.py** implementa três variantes da quadratura de Gauss:

| Função | Caso tratado | Limites inferiores/superiores |
| ------ | ------------ | ----------------------------- |
| `QuadraturaGauss1` | Limites fixos a ≤ x ≤ b, c ≤ y ≤ d | ambos constantes |
| `QuadraturaGauss2` | Limites dependentes nas duas variáveis | `c(x)` e `d(x)` |
| `QuadraturaGauss3` | Limite superior dependente, inferior constante | `c` e `d(x)` |

Cada rotina:
1. Obtém nós e pesos de Legendre via `numpy.polynomial.legendre.leggauss(n)`;  
2. Mapeia os nós para o intervalo desejado;  
3. Avalia a função e soma os produtos peso·função para formar a integral.

O script inclui **8 exemplos práticos** (cubo, tetraedro, regiões poligonais, sólidos de revolução) com graus de precisão `n = 6, 8, 10`, imprimindo os resultados no console.

## Pré‑requisitos ⚙️
- Python ≥ 3.8  
- NumPy (única dependência externa)

## Estrutura do Projeto 🗂️
```
├── EP2.py              # Código‑fonte principal com exemplos
├── LEIAME.txt          # Relatório em português (resumo teórico)
├── Relatório EP2.pdf   # Relatório completo em PDF
└── LICENSE             # GPL‑3.0
```

## Instalação 🔧
```bash
git clone https://github.com/rafael-agra/EP2-Calculo-Numerico.git
cd EP2-Calculo-Numerico
python -m venv .venv && source .venv/bin/activate  # Linux/macOS
pip install numpy
```

## Uso 🚀
Execute diretamente:
```bash
python EP2.py
```
O script executará todos os exemplos e exibirá as integrais aproximadas para cada valor de `n`.

Para usar as rotinas em outro projeto:
```python
from EP2 import QuadraturaGauss1, QuadraturaGauss2, QuadraturaGauss3

f = lambda x, y: x**2 + y**2
resultado = QuadraturaGauss1(f, n=8, a=0, b=1, c=0, d=1)
print(resultado)
```

## Exemplos 💻
### Tetraedro (n = 8)
```
----EXEMPLO 1----
Tetraedro (para n = 8):  0.16666666666666666
```
### Sólido de revolução (n = 10)
```
Solido de revolucao (para n = 10):  3.141611859...
```

## Funções Disponíveis 🔍
- `QuadraturaGauss1(func, n, a, b, c, d)`  
- `QuadraturaGauss2(func, n, a, b, c(x), d(x))`  
- `QuadraturaGauss3(func, n, a, b, c, d(x))`  
Todas possuem docstrings que explicam parâmetros, retorno e exemplo de uso.

## Licença 📜
Distribuído sob a licença **GPL‑3.0** — consulte o arquivo `LICENSE` para detalhes.


