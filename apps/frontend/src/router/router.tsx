import { BrowserRouter, Routes, Route } from "react-router-dom"

import Dashboard from "../pages/Dashboard"
import Tickets from "../pages/Tickets"
import CreateTicket from "../pages/CreateTicket"
import Login from "../pages/Login"
import Register from "../pages/Register"
import ProtectedRoute from "../components/auth/ProtectedRoute"
import Departments from "../pages/Departments"

export default function Router() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
            path="/"
            element={
                <ProtectedRoute>
                    <Dashboard />
                </ProtectedRoute>
            }
        />

        <Route
            path="/tickets"
            element={
                <ProtectedRoute>
                    <Tickets />
                </ProtectedRoute>
            }
        />
        <Route path="/departments" element={
                <ProtectedRoute><Departments /></ProtectedRoute>
            } />
        <Route path="/tickets/new" element={<CreateTicket />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

      </Routes>

    </BrowserRouter>
  )
}