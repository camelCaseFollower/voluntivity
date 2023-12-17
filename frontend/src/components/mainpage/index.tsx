import "./index.css"
import "../navbar/index"

interface Props{
    state: string
}

export default function MainPage(props: Props){
    return(
        <div className="flex main_page p-3">
            <h1 className="text-2xl w-full text-center">Hello World</h1>
        </div>
    )
}