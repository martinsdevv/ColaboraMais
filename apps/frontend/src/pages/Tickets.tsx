import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import Layout from "../components/layout/Layout"
import { api } from "../api/client"
import { Ticket, Plus, Calendar, Hash, Activity } from "lucide-react"

export default function Tickets() {
  const [tickets, setTickets] = useState<any[]>([])

  useEffect(() => {
    api.get("/tickets")
      .then(res => {
        setTickets(res.data)
      })
  }, [])

  // Função para estilizar as pílulas de status
  const getStatusBadge = (status: string) => {
    const styles: { [key: string]: string } = {
      OPEN: "bg-blue-100 text-blue-700 border-blue-200",
      IN_PROGRESS: "bg-amber-100 text-amber-700 border-amber-200",
      CLOSED: "bg-emerald-100 text-emerald-700 border-emerald-200",
    }
    return styles[status.toUpperCase()] || "bg-slate-100 text-slate-700 border-slate-200"
  }

  return (
    <Layout>
      {/* Cabeçalho da Página */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-8">
        <div>
          <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
            Central de Tickets
          </h1>
          <p className="text-slate-500 mt-1">Gerencie e acompanhe todos os chamados do sistema.</p>
        </div>

        <Link
          to="/tickets/new"
          className="inline-flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-5 py-2.5 rounded-xl font-semibold transition-all shadow-lg shadow-blue-200 active:scale-95"
        >
          <Plus size={20} />
          Abrir Novo Chamado
        </Link>
      </div>

      {/* Container da Tabela */}
      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr className="bg-slate-50 border-b border-slate-200">
                <th className="p-4 text-left">
                  <span className="flex items-center gap-2 text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <Hash size={14} /> ID
                  </span>
                </th>
                <th className="p-4 text-left">
                  <span className="flex items-center gap-2 text-xs font-bold text-slate-500 uppercase tracking-widest">
                    Título do Chamado
                  </span>
                </th>
                <th className="p-4 text-left">
                  <span className="flex items-center gap-2 text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <Activity size={14} /> Status
                  </span>
                </th>
                <th className="p-4 text-left">
                  <span className="flex items-center gap-2 text-xs font-bold text-slate-500 uppercase tracking-widest">
                    <Calendar size={14} /> Criado em
                  </span>
                </th>
              </tr>
            </thead>

            <tbody className="divide-y divide-slate-100">
              {tickets.length > 0 ? (
                tickets.map((t) => (
                  <tr key={t.id} className="hover:bg-slate-50/80 transition-colors group">
                    <td className="p-4 text-sm font-mono text-slate-400">
                      #{t.id}
                    </td>
                    <td className="p-4">
                      <div className="text-sm font-semibold text-slate-800 group-hover:text-blue-600 transition-colors">
                        {t.title}
                      </div>
                    </td>
                    <td className="p-4">
                      <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-bold border ${getStatusBadge(t.status)}`}>
                        {t.status}
                      </span>
                    </td>
                    <td className="p-4 text-sm text-slate-500">
                      {new Date(t.created_at).toLocaleDateString('pt-BR', {
                        day: '2-digit',
                        month: '2-digit',
                        year: 'numeric',
                        hour: '2-digit',
                        minute: '2-digit'
                      })}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={4} className="p-12 text-center text-slate-400">
                    <div className="flex flex-col items-center gap-2">
                      <Ticket size={48} className="text-slate-200" />
                      <p>Nenhum ticket encontrado.</p>
                    </div>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </Layout>
  )
}