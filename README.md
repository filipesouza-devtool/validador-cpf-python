# 🛡️ Validador de CPF Minimalista (Python + Tkinter)

Uma aplicação leve e moderna desenvolvida em **Python** puro utilizando **Tkinter**, focada em performance, validação matemática de documentos e formatação automática (máscara em tempo real). 

O projeto foi pensado e estruturado para ser extremamente eficiente, rodando de forma fluida tanto no computador quanto diretamente em ambientes móveis (como Pydroid 3 e PyramIDE).

---

## ✨ Funcionalidades

* 🎨 **Dark Mode Minimalista:** Interface limpa com design *flat* (`#1e1e1e` de fundo e `#3b82f6` como cor de destaque).
* ⌨️ **Máscara em Tempo Real:** Formatação automática do documento (`000.000.000-00`) à medida que os números são digitados.
* 🛡️ **Filtro Inteligente:** Bloqueio imediato de sequências repetidas inválidas (ex: `111.111.111-11`) e caracteres indesejados.
* 🧮 **Validação Matemática Real:** Implementação algorítmica do cálculo oficial dos dois dígitos verificadores do CPF.
* 📱 **Foco Mobile:** Construído sem dependências externas pesadas (como `customtkinter`), garantindo compatibilidade nativa em editores Python de telemóvel.

---

## 🛠️ Tecnologias Utilizadas

* **Python** (Lógica principal e algoritmos de validação)
* **Tkinter** (Interface gráfica nativa)

---

## 🚀 Como Executar

1. Certifica-te de que tens o **Python** instalado no teu dispositivo (ou um ambiente mobile compatível como Pydroid 3 / PyramIDE).
2. Clona este repositório ou descarrega o ficheiro `main.py`.
3. Executa o script:

```bash
python main.py
