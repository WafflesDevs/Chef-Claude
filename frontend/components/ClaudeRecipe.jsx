import ReactMarkdown from "react-markdown"
export default function ClaudeRecipe({ recipe }) {
    return (
        <section>
            <h2>Chef Claude Recommends:</h2>
            <ReactMarkdown>{recipe}</ReactMarkdown>
        </section>
    )
}