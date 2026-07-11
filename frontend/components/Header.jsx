import chefClaudeLogo from "../images/chef-claude-icon.png";
import { Outlet } from "react-router-dom";
import {Link} from "react-router-dom"
export default function Header() {
    
    return (
        <>

        <header>
            <img src={chefClaudeLogo}/>
            <h1>Chef Claude</h1>
            <div className ="Links">
             <Link to="/">HomePage</Link>
             <Link to="/generate">Recipe Generator</Link>

            </div>
        </header>
         <Outlet/>
         </>
    )
}