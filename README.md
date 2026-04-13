# YouTube Downloader

Aplicacao desktop com interface grafica (Tkinter) para download de videos e audios do YouTube utilizando yt-dlp.

## Funcionalidades

- Download de videos em MP4 (melhor qualidade disponivel)
- Extracao de audio em MP3 (192 kbps)
- Deteccao automatica de playlists
- Barra de progresso em tempo real
- Downloads organizados automaticamente em pastas separadas
- Interface grafica moderna e responsiva

## Requisitos

- Python 3.10+
- [FFmpeg](https://ffmpeg.org/) — necessario para conversao de audio/video
- [Deno](https://deno.com/) — runtime JavaScript exigido pelo yt-dlp para extracoes do YouTube

### Instalacao dos requisitos (Windows)

```bash
winget install "FFmpeg (Essentials Build)"
winget install DenoLand.Deno
```

### Instalacao das dependencias Python

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python src/app.py
```

## Estrutura do projeto

```
yt/
├── src/
│   └── app.py
├── Downloads/
│   ├── audios_unicos/
│   ├── videos_unicos/
│   ├── playlist_audio/
│   └── playlist_video/
├── .gitignore
├── README.md
└── requirements.txt
```

A pasta `Downloads/` e suas subpastas sao criadas automaticamente ao realizar o primeiro download.

## Screenshots

<img width="498" height="305" alt="Screenshot_7" src="https://github.com/user-attachments/assets/59bf6449-8b7b-448a-b61b-a855c2c34516" />

<img width="630" height="394" alt="Screenshot_8" src="https://github.com/user-attachments/assets/7b2c0fab-d9c1-427d-9c2b-116b2a4087bf" />

<img width="642" height="387" alt="Screenshot_9" src="https://github.com/user-attachments/assets/68b37403-5ba1-4a89-802f-4051c61d3069" />

---

Este projeto e apenas para fins educacionais. O usuario e responsavel por respeitar os termos de uso do YouTube e as leis de direitos autorais.
