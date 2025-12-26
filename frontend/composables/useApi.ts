import axios from 'axios'

export const useApi = () => {
  const config = useRuntimeConfig()
  
  const api = axios.create({
    baseURL: config.public.apiBase as string,
    headers: {
      'Content-Type': 'application/json',
    },
  })

  // Projects API
  const getProjects = async () => {
    const response = await api.get('/projects/')
    return response.data
  }

  const getProject = async (id: number) => {
    const response = await api.get(`/projects/${id}/`)
    return response.data
  }

  const createProject = async (data: any) => {
    const response = await api.post('/projects/', data)
    return response.data
  }

  const updateProject = async (id: number, data: any) => {
    const response = await api.put(`/projects/${id}/`, data)
    return response.data
  }

  const deleteProject = async (id: number) => {
    await api.delete(`/projects/${id}/`)
  }

  // Tasks API
  const getTasks = async (filters?: any) => {
    const response = await api.get('/tasks/', { params: filters })
    return response.data
  }

  const getTask = async (id: number) => {
    const response = await api.get(`/tasks/${id}/`)
    return response.data
  }

  const createTask = async (data: any) => {
    const response = await api.post('/tasks/', data)
    return response.data
  }

  const updateTask = async (id: number, data: any) => {
    const response = await api.put(`/tasks/${id}/`, data)
    return response.data
  }

  const deleteTask = async (id: number) => {
    await api.delete(`/tasks/${id}/`)
  }

  // Users API
  const getUsers = async () => {
    const response = await api.get('/users/')
    return response.data
  }

  return {
    getProjects,
    getProject,
    createProject,
    updateProject,
    deleteProject,
    getTasks,
    getTask,
    createTask,
    updateTask,
    deleteTask,
    getUsers,
  }
}


