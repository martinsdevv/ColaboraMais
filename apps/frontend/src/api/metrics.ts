import { api } from "./client"

export async function getMetrics() {
  const res = await api.get("/metrics")
  return res.data
}