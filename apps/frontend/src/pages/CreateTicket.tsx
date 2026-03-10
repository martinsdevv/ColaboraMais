import { useEffect, useState } from "react";
import Layout from "../components/layout/Layout";
import { createTicket } from "../api/tickets";
import { getDepartments } from "../api/departments";
import { ArrowLeft, Send } from "lucide-react";
import { Link } from "react-router-dom";

export default function CreateTicket() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [department, setDepartment] = useState("");
  const [departments, setDepartments] = useState<any[]>([]);

  useEffect(() => { loadDepartments(); }, []);

  async function loadDepartments() {
    const data = await getDepartments();
    setDepartments(data);
  }

  async function handleSubmit(e: any) {
    e.preventDefault();
    await createTicket({ title, description, department_target_id: Number(department), author_id: 1 });
    window.location.href = "/tickets";
  }

  return (
    <Layout>
      <div className="mb-8">
        <Link to="/tickets" className="text-blue-600 flex items-center gap-2 text-sm font-medium mb-4 hover:underline">
          <ArrowLeft size={16} /> Voltar para tickets
        </Link>
        <h1 className="text-3xl font-bold text-slate-900">Novo Chamado</h1>
      </div>

      <form onSubmit={handleSubmit} className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200 max-w-2xl space-y-6">
        <div>
          <label className="block text-sm font-semibold text-slate-700 mb-2">Título do Problema</label>
          <input
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none"
            placeholder="Ex: Erro ao acessar impressora"
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div>
          <label className="block text-sm font-semibold text-slate-700 mb-2">Departamento Destino</label>
          <select
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none bg-white"
            onChange={(e) => setDepartment(e.target.value)}
          >
            <option value="">Selecione um departamento</option>
            {departments.map((d) => (
              <option key={d.id} value={d.id}>{d.name}</option>
            ))}
          </select>
        </div>

        <div>
          <label className="block text-sm font-semibold text-slate-700 mb-2">Descrição Detalhada</label>
          <textarea
            rows={5}
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none"
            placeholder="Descreva o que está acontecendo..."
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>

        <button className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-xl font-bold transition-all shadow-lg shadow-blue-100">
          <Send size={18} /> Abrir Ticket
        </button>
      </form>
    </Layout>
  );
}