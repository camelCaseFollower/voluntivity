import Navbar from "./components/navbar"
import MainPage from "./components/mainpage"

function App() {
  return (
    <div className="flex screen w-screen h-screen">
      <Navbar />
      <MainPage state = "default"/>
    </div>
  );
}

export default App;
