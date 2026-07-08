import os
from anthropic import Anthropic
from dotenv import load_dotenv
from app.core.config import settings

load_dotenv()

SYSTEM_PROMPT = """
You are an assistant that receives a list of ingredients that a user has and suggests a recipe they could make with some or all of those ingredients. You don't need to use every ingredient they mention in your recipe. The recipe can include additional ingredients they didn't mention, but try not to include too many extra ingredients. Format your response in markdown to make it easier to render to a web page
"""

client = Anthropic(
    api_key=os.environ.get(settings.ANTHROPIC_API_KEY),
)

def get_recipe_from_chef_claude(ingredients: list[str]) -> str:
    ingredients_string = ", ".join(ingredients)

    msg = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"I have {ingredients_string}. Please give me a recipe you'd recommend I make!"},
        ],
    )
    return msg.content[0].text