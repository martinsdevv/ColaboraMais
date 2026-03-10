import { api } from "./client"

export async function getDepartments() {

  const res = await api.get("/departments")

  return res.data

}

export async function createDepartment(name: string) {

  const res = await api.post("/departments", {
    name
  })

  return res.data
}