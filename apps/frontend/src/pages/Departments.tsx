import { useEffect, useState } from "react";
import Layout from "../components/layout/Layout";
import { getDepartments, createDepartment } from "../api/departments";
import {  Plus } from "lucide-react";

export default function Departments() {
  const [departments, setDepartments] = useState<any[]>([]);
  const [name, setName] = useState("");

  useEffect(() => { loadDepartments(); }, []);

  async function loadDepartments() {
    const data = await getDepartments();
    setDepartments(data);
  }

  async function handleCreate(e: any) {
    e.preventDefault();
    await createDepartment(name);
    setName("");
    loadDepartments();
  }

  return (
    <Layout>
      <h1 className="text-3xl font-bold text-slate-900 mb-8 flex items-center gap-3">
        Departamentos
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <form onSubmit={handleCreate} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 h-fit">
          <h2 className="font-bold text-slate-800 mb-4 text-lg">Adicionar Novo</h2>
          <input
            className="w-full border border-slate-200 p-3 rounded-xl mb-4 outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Nome do setor"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button className="w-full flex items-center justify-center gap-2 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-xl font-semibold transition-all">
            <Plus size={18} /> Criar
          </button>
        </form>

        <div className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
          <table className="w-full">
            <thead className="bg-slate-50 border-b border-slate-200">
              <tr>
                <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-widest">ID</th>
                <th className="p-4 text-left text-xs font-semibold text-slate-500 uppercase tracking-widest">Nome do Setor</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {departments.map((d) => (
                <tr key={d.id} className="hover:bg-slate-50 transition-colors">
                  <td className="p-4 text-sm font-mono text-slate-400">#{d.id}</td>
                  <td className="p-4 text-sm font-semibold text-slate-700 uppercase tracking-tight">{d.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </Layout>
  );
}