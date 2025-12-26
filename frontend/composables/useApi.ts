export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiBase as string

  // Projects API
  const getProjects = async () => {
    return await $fetch('/projects/', {
      baseURL,
    })
  }

  const getProject = async (id: number) => {
    return await $fetch(`/projects/${id}/`, {
      baseURL,
    })
  }

  const createProject = async (data: any) => {
    return await $fetch('/projects/', {
      baseURL,
      method: 'POST',
      body: data,
    })
  }

  const updateProject = async (id: number, data: any) => {
    return await $fetch(`/projects/${id}/`, {
      baseURL,
      method: 'PUT',
      body: data,
    })
  }

  const deleteProject = async (id: number) => {
    await $fetch(`/projects/${id}/`, {
      baseURL,
      method: 'DELETE',
    })
  }

  // Tasks API
  const getTasks = async (filters?: any) => {
    return await $fetch('/tasks/', {
      baseURL,
      query: filters,
    })
  }

  const getTask = async (id: number) => {
    return await $fetch(`/tasks/${id}/`, {
      baseURL,
    })
  }

  const createTask = async (data: any) => {
    return await $fetch('/tasks/', {
      baseURL,
      method: 'POST',
      body: data,
    })
  }

  const updateTask = async (id: number, data: any) => {
    return await $fetch(`/tasks/${id}/`, {
      baseURL,
      method: 'PUT',
      body: data,
    })
  }

  const deleteTask = async (id: number) => {
    await $fetch(`/tasks/${id}/`, {
      baseURL,
      method: 'DELETE',
    })
  }

  // Users API
  const getUsers = async () => {
    return await $fetch('/users/', {
      baseURL,
    })
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


