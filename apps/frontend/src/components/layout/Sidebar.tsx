import { Link } from "react-router-dom"

export default function Sidebar() {
  return (
    <div className="w-64 bg-gray-900 text-white p-6">

      <h1 className="text-2xl font-bold mb-8">
        ColaboraMais
      </h1>

      <nav className="space-y-3">

        <Link
          to="/"
          className="block hover:text-blue-400"
        >
          Dashboard
        </Link>

        <Link
          to="/tickets"
          className="block hover:text-blue-400"
        >
          Tickets
        </Link>
        <Link
          to="/departments"
          className="block hover:text-blue-400"
        >
          Departamentos
        </Link>

      </nav>

    </div>
  )
}