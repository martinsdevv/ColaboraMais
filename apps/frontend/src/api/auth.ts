import { api } from "./client"

export async function login(email: string, password: string) {

  const res = await api.post("/auth/login", {
    email,
    password
  })

  return res.data
}

export async function createUser(data: any) {

  const res = await api.post("/users", data)

  return res.data
}