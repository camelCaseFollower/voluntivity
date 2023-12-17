import "./navbar.css"
import Button from "./button"
import { useState } from "react"

export default function Navbar(){
    const [display,useDisplay] = useState("default")
    return(
        <div className="flex flex-col shadow h-screen navbar rounded-2xl">
            <Button content="Profile" state="profile"/>
            <Button content="Events" state="profile"/>
            <Button content="Profile" state="profile"/>
        </div>
    )
}