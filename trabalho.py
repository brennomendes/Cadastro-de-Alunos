import tkinter as tk
from tkinter import messagebox

# Simulando banco de dados com dicionário
banco_alunos = {}

def cadastrar_aluno():
    matricula = entry_matricula.get()
    nome = entry_nome.get()
    curso = entry_curso.get()
    nota = entry_nota.get()

    if all([matricula, nome, curso, nota]):
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                banco_alunos[matricula] = {
                    "nome": nome,
                    "curso": curso,
                    "nota": nota
                }
                messagebox.showinfo("Cadastro Realizado", f"Aluno {nome} cadastrado com sucesso!")
                limpar_campos()
            else:
                messagebox.showwarning("Nota Inválida", "A nota deve estar entre 0 e 10.")
        except ValueError:
            messagebox.showerror("Erro de Valor", "A nota deve ser um número.")
    else:
        messagebox.showwarning("Campos Vazios", "Preencha todos os campos antes de cadastrar.")

def consultar_aluno():
    matricula = entry_matricula.get()

    if matricula:
        aluno = banco_alunos.get(matricula)

        if aluno:
            mensagem = (
                f"Nome: {aluno['nome']}\n"
                f"Curso: {aluno['curso']}\n"
                f"Nota: {aluno['nota']}"
            )
            messagebox.showinfo("Consulta de Aluno", mensagem)
        else:
            messagebox.showwarning("Não Encontrado", "Aluno não encontrado com a matrícula fornecida.")
    else:
        messagebox.showwarning("Campo Requerido", "Informe a matrícula do aluno.")

def limpar_campos():
    entry_matricula.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_curso.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Criação da interface
root = tk.Tk()
root.title("Sistema Acadêmico - Cadastro de Notas")
root.geometry("1024x768")
root.configure(bg="#e9eef1")

# Frame container que ocupa a tela inteira
frame_container = tk.Frame(root, bg="#e9eef1")
frame_container.pack(fill="both", expand=True)

# Frame centralizado para o formulário
frame_formulario = tk.Frame(frame_container, bg="#ffffff", padx=40, pady=30)
frame_formulario.pack(expand=True)

# Título
titulo = tk.Label(frame_formulario, text="Cadastro Acadêmico de Notas", font=("Segoe UI", 20, "bold"), bg="#ffffff")
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 30))

# Campos
campos = [
    ("Matrícula:", "entry_matricula"),
    ("Nome Completo:", "entry_nome"),
    ("Curso:", "entry_curso"),
    ("Nota (0 a 10):", "entry_nota")
]

entries = {}

for i, (label_text, var_name) in enumerate(campos, start=1):
    label = tk.Label(frame_formulario, text=label_text, font=("Segoe UI", 11), bg="#ffffff")
    label.grid(row=i, column=0, sticky="e", pady=10, padx=10)

    entry = tk.Entry(frame_formulario, font=("Segoe UI", 11), width=40)
    entry.grid(row=i, column=1, sticky="w", pady=10, padx=10)

    entries[var_name] = entry

entry_matricula = entries["entry_matricula"]
entry_nome = entries["entry_nome"]
entry_curso = entries["entry_curso"]
entry_nota = entries["entry_nota"]

# Botões
btn_cadastrar = tk.Button(
    frame_formulario, text="Cadastrar Aluno", font=("Segoe UI", 12, "bold"),
    bg="#4CAF50", fg="white", padx=20, pady=10, command=cadastrar_aluno
)
btn_cadastrar.grid(row=6, column=0, pady=30, sticky="e", padx=10)

btn_consultar = tk.Button(
    frame_formulario, text="Consultar por Matrícula", font=("Segoe UI", 12, "bold"),
    bg="#2196F3", fg="white", padx=20, pady=10, command=consultar_aluno
)
btn_consultar.grid(row=6, column=1, pady=30, sticky="w", padx=10)

# Responsividade dentro do formulário
for i in range(7):
    frame_formulario.grid_rowconfigure(i, weight=1)
frame_formulario.grid_columnconfigure(0, weight=1)
frame_formulario.grid_columnconfigure(1, weight=2)

# Iniciar o loop da interface
root.mainloop()
