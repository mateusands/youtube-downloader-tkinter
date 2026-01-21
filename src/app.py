import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading
import os

def processar_download(url, formato_escolhido, label_status, botao):
    try:
        # Define configurações baseado na escolha
        if formato_escolhido == 'mp3':
            pasta_nome = "Audios"
            opcoes = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(pasta_nome, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': True,
            }
        else:
            pasta_nome = "Videos"
            opcoes = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(pasta_nome, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4', 
                'quiet': True,
            }

        # Cria a pasta
        if not os.path.exists(pasta_nome):
            os.makedirs(pasta_nome)

        # Atualiza status
        label_status.config(text=f"Baixando {formato_escolhido.upper()}... Aguarde.", fg="blue")
        
        # Download
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        label_status.config(text=f"Sucesso! Salvo na pasta '{pasta_nome}'.", fg="green")
        messagebox.showinfo("Concluído", "Download finalizado com sucesso!")

    except Exception as e:
        label_status.config(text="Erro.", fg="red")
        messagebox.showerror("Erro", f"Ocorreu um erro:\n{e}")
    
    finally:
        botao.config(state=tk.NORMAL)

def iniciar_thread():
    url = entry_url.get()
    formato = var_formato.get()

    if not url:
        messagebox.showwarning("Atenção", "Cole um link primeiro.")
        return

    btn_enviar.config(state=tk.DISABLED)
    thread = threading.Thread(target=processar_download, args=(url, formato, lbl_status, btn_enviar))
    thread.start()

# --- Interface Gráfica ---
root = tk.Tk()
root.title("Downloader Youtube Pro")
root.geometry("500x280")
root.resizable(False, False)

tk.Label(root, text="Downloader Youtube", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Cole o link do vídeo:", font=("Arial", 10)).pack()

entry_url = tk.Entry(root, width=55, font=("Arial", 10))
entry_url.pack(pady=5)

frame_opcoes = tk.Frame(root)
frame_opcoes.pack(pady=10)
var_formato = tk.StringVar(value="mp3")

tk.Radiobutton(frame_opcoes, text="Áudio (MP3)", variable=var_formato, value="mp3", font=("Arial", 11)).pack(side=tk.LEFT, padx=20)
tk.Radiobutton(frame_opcoes, text="Vídeo (MP4 Compatível)", variable=var_formato, value="mp4", font=("Arial", 11)).pack(side=tk.LEFT, padx=20)

btn_enviar = tk.Button(root, text="BAIXAR AGORA", command=iniciar_thread, bg="#2196F3", fg="white", font=("Arial", 11, "bold"), width=20, height=2)
btn_enviar.pack(pady=10)

lbl_status = tk.Label(root, text="Pronto.", font=("Arial", 9), fg="gray")
lbl_status.pack(pady=5)

root.mainloop()