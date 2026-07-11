import React from "react"
import { useNavigate } from "react-router-dom"

export default function FrontPage() {
    const navigate = useNavigate()

    return (
        <div className="hero">
            <img src="https://burst.shopifycdn.com/photos/flatlay-iron-skillet-with-meat-and-other-food.jpg?width=1000&format=pjpg&exif=0&iptc=0" />
            <div className="hero-text">
                <h1>Chef Claude</h1>
                <h2>No more "what's for dinner?" — just tell us what's in your fridge, and let AI whip up something delicious.</h2>
                <button onClick={() => navigate('/generate')}>Generate now!</button>
            </div>
            
        </div>
    )
}