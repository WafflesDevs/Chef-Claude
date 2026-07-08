import axios from "axios";

export async function getRecipeFromChefClaude(ingredientsArr) {
    try {
        const response = await axios.post("http://127.0.0.1:8000/getrecipe", {
            items: ingredientsArr
        });
        return response.data.recipe;
    } catch (error) {
        console.error(error);
    }
}