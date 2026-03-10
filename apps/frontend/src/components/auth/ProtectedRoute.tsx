export default function ProtectedRoute({ children }: any) {

  const token = localStorage.getItem("token")

  if (!token) {
    window.location.href = "/login"
    return null
  }

  return children
}