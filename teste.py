import re

# Carrega o arquivo com as palavras
with open("br-utf8.txt", "r", encoding="utf-8") as f:
    palavras = [p.strip() for p in f if p.strip()]

# Critério simples para detectar conjugações verbais
# Mantém palavras terminadas em "ar", "er", "ir" (infinitivos)
# e remove palavras que tenham terminações típicas de conjugação
padrao_conjugacao = re.compile(
    r"(o|as|a|amos|am|ei|ou|ava|avam|asse|assem|ara|aram|arei|ariam|ando|endo|indo|es|eis|ia|iam|iria|iriam|ou|u|iu)$"
)

# Mantém apenas as palavras que:
# - são infinitivos (ar, er, ir)
# - ou não batem com o padrão de conjugação
limpas = []
for p in palavras:
    if p.endswith(("ar", "er", "ir")) or not padrao_conjugacao.search(p):
        limpas.append(p)

# Remove duplicadas e ordena
limpas = sorted(set(limpas))

# Salva em um novo arquivo
with open("palavras_sem_conjugacoes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(limpas))

print(f"Foram mantidas {len(limpas)} palavras sem conjugações.")
