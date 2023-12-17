import { useState } from "react"

interface Arguments{
    content: string,
    state: string
}


export default function Button(props: Arguments){
    const [display,setDisplay] = useState("default")

    return(
        <button className="w-3/4 shadow p-4 m-3 button font-bold rounded-3xl self-center">{props.content}</button>
    )
}