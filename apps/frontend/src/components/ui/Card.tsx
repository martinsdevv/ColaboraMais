export default function Card({ title, value }: any) {
  return (
    <div className="bg-white rounded shadow p-6">

      <p className="text-gray-500 text-sm">
        {title}
      </p>

      <p className="text-3xl font-bold mt-2">
        {value}
      </p>

    </div>
  )
}