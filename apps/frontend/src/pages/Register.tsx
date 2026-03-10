import { useState } from "react";
import { Link } from "react-router-dom";
import { createUser } from "../api/auth";

export default function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleSubmit(e: any) {
    e.preventDefault();
    await createUser({ name, email, password, role_id: 1 });
    alert("Usuário criado!");
    window.location.href = "/login";
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-50 p-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl shadow-slate-200 w-full max-w-md border border-slate-100">
        <h1 className="text-3xl font-bold mb-2 text-center text-slate-900">Criar conta</h1>
        <p className="text-slate-500 text-center mb-8 text-sm">Junte-se ao ColaboraMais hoje</p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            placeholder="Nome Completo"
            onChange={(e) => setName(e.target.value)}
          />
          <input
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            placeholder="E-mail"
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            className="w-full border border-slate-200 p-3 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            placeholder="Senha"
            onChange={(e) => setPassword(e.target.value)}
          />

          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl font-semibold shadow-lg shadow-blue-200 transition-all mt-4">
            Cadastrar
          </button>
        </form>

        <div className="mt-8 text-center text-sm text-slate-600">
          Já possui conta?{" "}
          <Link to="/login" className="text-blue-600 font-semibold hover:underline">
            Fazer login
          </Link>
        </div>
      </div>
    </div>
  );
}