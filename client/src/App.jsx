import { useState } from 'react'
import {Route, Routes} from 'react-router-dom'
import IndexPage from './pages/IndexPage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Routes>
        <Route index element= {<IndexPage />} />
    </Routes>
  )
}

export default App
