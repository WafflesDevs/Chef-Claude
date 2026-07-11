import Header from "./components/Header"
import Main from "./components/Main"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import FrontPage from "/Users/wafflez/Chef Claude/frontend/pages/FrontPage.jsx"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Header />}>
          <Route path="/generate" element={<Main />} />
          <Route path="/" element={<FrontPage/>}/>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}