import { useState } from "react";
import { Link } from "react-router-dom";
import { login } from "../api/auth";
import { Lock, Mail } from "lucide-react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function handleSubmit(e: any) {
    e.preventDefault();
    try {
      const data = await login(email, password);
      localStorage.setItem("token", data.access_token);
      window.location.href = "/";
    } catch {
      alert("Login inválido");
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-50 p-4">
      <div className="bg-white p-8 rounded-2xl shadow-xl shadow-slate-200 w-full max-w-md border border-slate-100">
        <h1 className="text-3xl font-bold mb-2 text-center text-slate-900">ColaboraMais</h1>
        <p className="text-slate-500 text-center mb-8 text-sm">Entre com suas credenciais para acessar</p>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">E-mail</label>
            <div className="relative">
              <Mail className="absolute left-3 top-3 text-slate-400" size={18} />
              <input
                className="w-full border border-slate-200 p-3 pl-10 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                placeholder="seu@email.com"
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">Senha</label>
            <div className="relative">
              <Lock className="absolute left-3 top-3 text-slate-400" size={18} />
              <input
                type="password"
                className="w-full border border-slate-200 p-3 pl-10 rounded-xl focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                placeholder="••••••••"
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-xl font-semibold shadow-lg shadow-blue-200 transition-all active:scale-[0.98]">
            Entrar no sistema
          </button>
        </form>

        <div className="mt-8 text-center text-sm text-slate-600">
          Não tem uma conta?{" "}
          <Link to="/register" className="text-blue-600 font-semibold hover:underline">
            Crie uma agora
          </Link>
        </div>
      </div>
    </div>
  );
}