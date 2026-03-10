import { api } from "./client"

export async function getTickets() {
  const res = await api.get("/tickets")
  return res.data
}

export async function createTicket(data: any) {
  const res = await api.post("/tickets", data)
  return res.data
}

export async function updateTicketStatus(id: number, status: string) {
  const res = await api.patch(`/tickets/${id}/status`, {
    status
  })

  return res.data
}