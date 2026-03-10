import { useEffect, useState } from "react"
import Layout from "../components/layout/Layout"

import { getMetrics } from "../api/metrics"
import { getTickets } from "../api/tickets"

import Card from "../components/ui/Card"

export default function Dashboard() {

  const [metrics, setMetrics] = useState<any>({})
  const [tickets, setTickets] = useState<any[]>([])

  useEffect(() => {

    loadData()

  }, [])

  async function loadData() {

    const m = await getMetrics()
    const t = await getTickets()

    setMetrics(m)
    setTickets(t.slice(0, 5))

  }

  return (
    <Layout>

      <h1 className="text-2xl font-bold mb-8">
        Dashboard
      </h1>

      {/* Metrics */}

      <div className="grid grid-cols-4 gap-6 mb-10">

        <Card
          title="Tickets abertos"
          value={metrics.open_tickets ?? "-"}
        />

        <Card
          title="Em análise"
          value={metrics.in_analysis ?? "-"}
        />

        <Card
          title="Em andamento"
          value={metrics.in_progress ?? "-"}
        />

        <Card
          title="Concluídos"
          value={metrics.closed ?? "-"}
        />

      </div>

      {/* Tickets recentes */}
<div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
  
  {/* Header da Tabela - Ajustado com Flexbox */}
  <div className="p-4 border-b border-slate-100 flex items-center justify-between bg-white">
    <h2 className="font-semibold text-slate-700">Tickets recentes</h2>
    
    <a
      href="/tickets/new"
      className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors shadow-sm flex items-center gap-2"
    >
      <span>+</span> Novo Ticket
    </a>
  </div>

  <div className="overflow-x-auto">
    <table className="w-full">
      <thead className="bg-slate-50 border-b border-slate-200">
        <tr>
          <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">ID</th>
          <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Título</th>
          <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Status</th>
          <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Criado</th>
        </tr>
      </thead>

      <tbody className="divide-y divide-slate-100">
        {tickets.map((t) => (
          <tr key={t.id} className="hover:bg-slate-50 transition-colors">
            <td className="p-4 text-sm text-slate-600 font-mono">#{t.id}</td>
            <td className="p-4 text-sm font-medium text-slate-800">{t.title}</td>
            <td className="p-4">
              <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800 border border-blue-200">
                {t.status}
              </span>
            </td>
            <td className="p-4 text-sm text-slate-500">
              {t.created_at}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
</div>

    </Layout>
  )
}