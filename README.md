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

<img width="851" height="639" alt="image" src="https://github.com/user-attachments/assets/c0645424-a871-448f-ad57-84f73e9460bd" />

<img width="833" height="646" alt="image" src="https://github.com/user-attachments/assets/81a9c69b-bc59-4c6f-858b-40a77b74819d" />

<img width="862" height="666" alt="image" src="https://github.com/user-attachments/assets/be464037-fea4-466e-ae07-3a7639a8a8fe" />

---

Este projeto e apenas para fins educacionais. O usuario e responsavel por respeitar os termos de uso do YouTube e as leis de direitos autorais.
