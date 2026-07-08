<div align="center">

# 🍳 Chef Claude

### Turn your leftover ingredients into a real recipe — powered by Claude AI

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

---
</div>

---

## 📸 Screenshots

<div align="center">

**Add your ingredients**

<img src="https://i.postimg.cc/Y9Z3mdxd/Screenshot-2026-07-07-at-10-36-04-PM.png" alt="Chef Claude ingredient input screen" width="700"/>

**Get an AI-generated recipe**

<img src="https://i.postimg.cc/8JGfmfc1/Screenshot-2026-07-07-at-10-37-06-PM.png" alt="Chef Claude recipe result screen" width="700"/>

</div>

---

Chef Claude is a recipe generator that takes a list of ingredients you have on hand and suggests a recipe you can make with them, powered by Anthropic's Claude Haiku model.

As I start to get deeper into learning React.js I started to make some cool frontends! Hopefully I can soon add my own backend skills to make a fully functioning website by myself! Otherwise Im just focusing on frontend using react.js


## ✨ How it works

1. Enter the ingredients you have available.
2. The app sends your ingredient list to Claude (Haiku) with a prompt asking it to suggest a recipe.
3. Claude returns a recipe — formatted in Markdown — using some or all of your ingredients (it may include a few extra pantry staples if needed).
4. The recipe is rendered right on the page.

## 🛠️ Tech stack

- **React** + **Vite** for the frontend
- **@anthropic-ai/sdk** to call the Claude API
- **react-markdown** to render the returned recipe

## 🚀 Getting started

### 1. Install dependencies

```bash
npm install
```

## 2. on .env (ADD THIS TO UR .ENV FILE)

```bash
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
ANTHROPIC_API_KEY=
```

You can get an API key from the [Anthropic Console](https://console.anthropic.com/).

### 3. Run the app

```bash
npm run dev
```

This starts the Vite dev server. Open the local URL it prints (usually `http://localhost:5173`) in your browser.

## 🔑 A note on .env (ADD THIS TO UR .ENV FILE)

```bash
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
ANTHROPIC_API_KEY=
```

## 📜 Available scripts

| Command | Description |
|---|---|
| `npm run dev` | Starts the Vite development server |
| `npm run build` | Builds the app for production |
| `npm run preview` | Previews the production build locally |
| ` uv run uvicorn main:app --reload` | Runs the backend (MUST BE ON DIR OF backend)|
