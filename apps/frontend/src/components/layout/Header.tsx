import { LogOut } from "lucide-react";

export default function Header() {
  return (
    <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 shadow-sm">
      <div className="flex items-center gap-2">
        <span className="text-sm text-slate-500">Bem-vindo,</span>
        <span className="font-medium text-slate-700">Administrador</span>
      </div>

      <button
        onClick={() => {
          localStorage.removeItem("token");
          window.location.href = "/login";
        }}
        className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-red-600 hover:bg-red-50 rounded-lg transition-colors"
      >
        <LogOut size={18} />
        Sair
      </button>
    </header>
  );
}