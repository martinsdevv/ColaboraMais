/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}", // Isso aqui avisa o Tailwind para ler seus componentes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}