<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">Dashboard</h1>
      <p class="text-gray-600 mt-2">Welcome to your Project Management System</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Total Projects</h3>
        </template>
        <div class="text-3xl font-bold text-primary-600">{{ stats.totalProjects }}</div>
      </UCard>

      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Total Tasks</h3>
        </template>
        <div class="text-3xl font-bold text-green-600">{{ stats.totalTasks }}</div>
      </UCard>

      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Completed Tasks</h3>
        </template>
        <div class="text-3xl font-bold text-blue-600">{{ stats.completedTasks }}</div>
      </UCard>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Recent Projects</h3>
        </template>
        <div v-if="loading" class="text-center py-4">
          <p class="text-gray-500">Loading...</p>
        </div>
        <div v-else-if="recentProjects.length === 0" class="text-center py-4">
          <p class="text-gray-500">No projects yet</p>
          <UButton to="/projects" class="mt-4">Create Project</UButton>
        </div>
        <div v-else class="space-y-3">
          <div
            v-for="project in recentProjects"
            :key="project.id"
            class="p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer"
            @click="navigateTo(`/projects/${project.id}`)"
          >
            <h4 class="font-medium">{{ project.name }}</h4>
            <p class="text-sm text-gray-600">{{ project.description }}</p>
            <div class="flex items-center justify-between mt-2">
              <UBadge :color="getStatusColor(project.status)">{{ project.status }}</UBadge>
              <span class="text-xs text-gray-500">{{ project.task_count }} tasks</span>
            </div>
          </div>
        </div>
      </UCard>

      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Recent Tasks</h3>
        </template>
        <div v-if="loading" class="text-center py-4">
          <p class="text-gray-500">Loading...</p>
        </div>
        <div v-else-if="recentTasks.length === 0" class="text-center py-4">
          <p class="text-gray-500">No tasks yet</p>
          <UButton to="/tasks" class="mt-4">Create Task</UButton>
        </div>
        <div v-else class="space-y-3">
          <div
            v-for="task in recentTasks"
            :key="task.id"
            class="p-3 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer"
            @click="navigateTo(`/tasks/${task.id}`)"
          >
            <h4 class="font-medium">{{ task.title }}</h4>
            <p class="text-sm text-gray-600">{{ task.description }}</p>
            <div class="flex items-center justify-between mt-2">
              <div class="flex gap-2">
                <UBadge :color="getStatusColor(task.status)">{{ task.status }}</UBadge>
                <UBadge :color="getPriorityColor(task.priority)">{{ task.priority }}</UBadge>
              </div>
              <span class="text-xs text-gray-500">{{ task.project?.name }}</span>
            </div>
          </div>
        </div>
      </UCard>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default',
})

const api = useApi()
const loading = ref(true)
const recentProjects = ref<any[]>([])
const recentTasks = ref<any[]>([])
const stats = ref({
  totalProjects: 0,
  totalTasks: 0,
  completedTasks: 0,
})

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    planning: 'yellow',
    in_progress: 'blue',
    completed: 'green',
    on_hold: 'gray',
    todo: 'gray',
    review: 'orange',
    done: 'green',
  }
  return colors[status] || 'gray'
}

const getPriorityColor = (priority: string) => {
  const colors: Record<string, string> = {
    low: 'gray',
    medium: 'blue',
    high: 'orange',
    urgent: 'red',
  }
  return colors[priority] || 'gray'
}

onMounted(async () => {
  try {
    const [projectsData, tasksData] = await Promise.all([
      api.getProjects(),
      api.getTasks(),
    ])
    
    recentProjects.value = projectsData.results?.slice(0, 5) || projectsData.slice(0, 5) || []
    recentTasks.value = tasksData.results?.slice(0, 5) || tasksData.slice(0, 5) || []
    
    const allProjects = projectsData.results || projectsData || []
    const allTasks = tasksData.results || tasksData || []
    
    stats.value = {
      totalProjects: allProjects.length,
      totalTasks: allTasks.length,
      completedTasks: allTasks.filter((t: any) => t.status === 'done').length,
    }
  } catch (error) {
    console.error('Error loading dashboard data:', error)
  } finally {
    loading.value = false
  }
})
</script>
