# Chef Claude

AI recipe generator — enter your ingredients and get a recipe from Claude.

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Copy the example env file and add your Anthropic API key:
   ```
   cp .env.example .env
   ```
   Then edit `.env` and set `VITE_ANTHROPIC_API_KEY` to your key from [console.anthropic.com](https://console.anthropic.com/). No quotes needed.

3. Run the dev server:
   ```
   npm run dev
   ```

Open http://localhost:5173/ in your browser.

Happy Coding!