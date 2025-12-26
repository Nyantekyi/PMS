<template>
  <div>
    <div class="mb-8 animate-fade-in">
      <h1 class="text-4xl font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
        Dashboard
      </h1>
      <p class="text-gray-600 mt-2 text-lg">Welcome back! Here's what's happening with your projects</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="group bg-gradient-to-br from-blue-500 to-blue-600 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:-translate-y-1">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
            <UIcon name="i-heroicons-folder" class="text-3xl text-white" />
          </div>
          <UIcon name="i-heroicons-arrow-trending-up" class="text-2xl text-white/70" />
        </div>
        <div class="text-white">
          <p class="text-sm font-medium text-white/80 mb-1">Total Projects</p>
          <p class="text-4xl font-bold">{{ stats.totalProjects }}</p>
        </div>
      </div>

      <div class="group bg-gradient-to-br from-green-500 to-emerald-600 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:-translate-y-1">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
            <UIcon name="i-heroicons-clipboard-document-list" class="text-3xl text-white" />
          </div>
          <UIcon name="i-heroicons-arrow-trending-up" class="text-2xl text-white/70" />
        </div>
        <div class="text-white">
          <p class="text-sm font-medium text-white/80 mb-1">Total Tasks</p>
          <p class="text-4xl font-bold">{{ stats.totalTasks }}</p>
        </div>
      </div>

      <div class="group bg-gradient-to-br from-purple-500 to-indigo-600 rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:-translate-y-1">
        <div class="flex items-center justify-between mb-4">
          <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm">
            <UIcon name="i-heroicons-check-circle" class="text-3xl text-white" />
          </div>
          <UIcon name="i-heroicons-arrow-trending-up" class="text-2xl text-white/70" />
        </div>
        <div class="text-white">
          <p class="text-sm font-medium text-white/80 mb-1">Completed</p>
          <p class="text-4xl font-bold">{{ stats.completedTasks }}</p>
          <p class="text-sm text-white/70 mt-1">{{ completionRate }}% completion rate</p>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <UCard class="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
        <template #header>
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <UIcon name="i-heroicons-folder-open" class="text-xl text-primary-600" />
              <h3 class="text-lg font-semibold text-gray-900">Recent Projects</h3>
            </div>
            <UButton to="/projects" size="xs" variant="ghost" icon="i-heroicons-arrow-right">
              View All
            </UButton>
          </div>
        </template>
        <div v-if="loading" class="text-center py-12">
          <UIcon name="i-heroicons-arrow-path" class="text-4xl text-gray-400 animate-spin" />
          <p class="text-gray-500 mt-2">Loading projects...</p>
        </div>
        <div v-else-if="recentProjects.length === 0" class="text-center py-12">
          <UIcon name="i-heroicons-folder-plus" class="text-5xl text-gray-300 mb-3" />
          <p class="text-gray-500 mb-4">No projects yet</p>
          <UButton to="/projects" icon="i-heroicons-plus">Create Your First Project</UButton>
        </div>
        <div v-else class="space-y-3">
          <div
            v-for="project in recentProjects"
            :key="project.id"
            class="group p-4 border border-gray-200 rounded-xl hover:border-primary-300 hover:bg-primary-50/50 cursor-pointer transition-all duration-200 transform hover:scale-[1.02]"
            @click="navigateTo(`/projects/${project.id}`)"
          >
            <div class="flex items-start justify-between mb-2">
              <h4 class="font-semibold text-gray-900 group-hover:text-primary-600 transition-colors">
                {{ project.name }}
              </h4>
              <UBadge :color="getStatusColor(project.status)" variant="subtle" size="xs">
                {{ formatStatus(project.status) }}
              </UBadge>
            </div>
            <p class="text-sm text-gray-600 mb-3 line-clamp-2">{{ project.description || 'No description' }}</p>
            <div class="flex items-center justify-between text-xs text-gray-500">
              <div class="flex items-center space-x-1">
                <UIcon name="i-heroicons-clipboard-document-list" />
                <span>{{ project.task_count }} tasks</span>
              </div>
              <div class="flex items-center space-x-1">
                <UIcon name="i-heroicons-user" />
                <span>{{ project.owner?.username }}</span>
              </div>
            </div>
          </div>
        </div>
      </UCard>

      <UCard class="overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300">
        <template #header>
          <div class="flex items-center justify-between">
            <div class="flex items-center space-x-2">
              <UIcon name="i-heroicons-clipboard-document-check" class="text-xl text-green-600" />
              <h3 class="text-lg font-semibold text-gray-900">Recent Tasks</h3>
            </div>
            <UButton to="/tasks" size="xs" variant="ghost" icon="i-heroicons-arrow-right">
              View All
            </UButton>
          </div>
        </template>
        <div v-if="loading" class="text-center py-12">
          <UIcon name="i-heroicons-arrow-path" class="text-4xl text-gray-400 animate-spin" />
          <p class="text-gray-500 mt-2">Loading tasks...</p>
        </div>
        <div v-else-if="recentTasks.length === 0" class="text-center py-12">
          <UIcon name="i-heroicons-clipboard-document-plus" class="text-5xl text-gray-300 mb-3" />
          <p class="text-gray-500 mb-4">No tasks yet</p>
          <UButton to="/tasks" icon="i-heroicons-plus">Create Your First Task</UButton>
        </div>
        <div v-else class="space-y-3">
          <div
            v-for="task in recentTasks"
            :key="task.id"
            class="group p-4 border border-gray-200 rounded-xl hover:border-green-300 hover:bg-green-50/50 cursor-pointer transition-all duration-200 transform hover:scale-[1.02]"
            @click="navigateTo(`/tasks/${task.id}`)"
          >
            <div class="flex items-start justify-between mb-2">
              <h4 class="font-semibold text-gray-900 group-hover:text-green-600 transition-colors flex-1">
                {{ task.title }}
              </h4>
            </div>
            <p class="text-sm text-gray-600 mb-3 line-clamp-2">{{ task.description || 'No description' }}</p>
            <div class="flex items-center justify-between">
              <div class="flex gap-2">
                <UBadge :color="getStatusColor(task.status)" variant="subtle" size="xs">
                  {{ formatStatus(task.status) }}
                </UBadge>
                <UBadge :color="getPriorityColor(task.priority)" variant="subtle" size="xs">
                  {{ task.priority }}
                </UBadge>
              </div>
              <span class="text-xs text-gray-500 flex items-center space-x-1">
                <UIcon name="i-heroicons-folder" />
                <span>{{ task.project?.name }}</span>
              </span>
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

const completionRate = computed(() => {
  if (stats.value.totalTasks === 0) return 0
  return Math.round((stats.value.completedTasks / stats.value.totalTasks) * 100)
})

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    planning: 'amber',
    in_progress: 'blue',
    completed: 'green',
    on_hold: 'gray',
    todo: 'slate',
    review: 'orange',
    done: 'green',
  }
  return colors[status] || 'gray'
}

const getPriorityColor = (priority: string) => {
  const colors: Record<string, string> = {
    low: 'slate',
    medium: 'blue',
    high: 'orange',
    urgent: 'red',
  }
  return colors[priority] || 'gray'
}

const formatStatus = (status: string) => {
  return status.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
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
