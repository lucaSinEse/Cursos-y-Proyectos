import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import {TaskPage} from './pages/TaskPage';
import {TaskFormPage} from './pages/TaskFormPages';
import {Navigation} from './assets/components/Navigation';
function App(){
  return(
    <BrowserRouter>
      <Navigation />
      <Routes>
      <Route path = "/" element={<Navigate to="/tasks" />} />
        <Route path = "/tasks" element={<TaskPage />} />
        <Route path = "/tasks-create" element={<TaskFormPage />} />

      </Routes>
    </BrowserRouter>
  )
}

export default App