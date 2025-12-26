<template>
  <div>
    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
      <div>
        <h1 class="text-4xl font-bold bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">
          Projects
        </h1>
        <p class="text-gray-600 mt-2 text-lg">Organize and track all your projects</p>
      </div>
      <UButton 
        @click="isCreateModalOpen = true" 
        icon="i-heroicons-plus" 
        size="lg"
        class="shadow-lg hover:shadow-xl transition-all duration-300"
      >
        New Project
      </UButton>
    </div>

    <div v-if="loading" class="text-center py-20">
      <UIcon name="i-heroicons-arrow-path" class="text-6xl text-gray-400 animate-spin mb-4" />
      <p class="text-gray-500 text-lg">Loading projects...</p>
    </div>

    <div v-else-if="projects.length === 0" class="text-center py-20 bg-white rounded-2xl shadow-lg">
      <UIcon name="i-heroicons-folder-plus" class="text-8xl text-gray-300 mb-4" />
      <p class="text-gray-500 mb-2 text-lg">No projects yet</p>
      <p class="text-gray-400 mb-6">Create your first project to get started!</p>
      <UButton @click="isCreateModalOpen = true" icon="i-heroicons-plus" size="lg">
        Create Project
      </UButton>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div
        v-for="project in projects"
        :key="project.id"
        class="group bg-white rounded-2xl shadow-md hover:shadow-2xl transition-all duration-300 cursor-pointer transform hover:-translate-y-2 overflow-hidden"
        @click="navigateTo(`/projects/${project.id}`)"
      >
        <div class="h-2 bg-gradient-to-r" :class="getStatusGradient(project.status)"></div>
        <div class="p-6">
          <div class="flex justify-between items-start mb-4">
            <div class="flex-1">
              <div class="flex items-center space-x-2 mb-2">
                <UIcon name="i-heroicons-folder" class="text-xl text-gray-400 group-hover:text-primary-600 transition-colors" />
                <h3 class="text-xl font-bold text-gray-900 group-hover:text-primary-600 transition-colors">
                  {{ project.name }}
                </h3>
              </div>
            </div>
            <UBadge :color="getStatusColor(project.status)" variant="subtle" size="sm">
              {{ formatStatus(project.status) }}
            </UBadge>
          </div>
          
          <p class="text-gray-600 text-sm mb-6 line-clamp-2 min-h-[40px]">
            {{ project.description || 'No description provided' }}
          </p>
          
          <div class="space-y-3">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-500 flex items-center space-x-2">
                <UIcon name="i-heroicons-clipboard-document-list" />
                <span>Tasks</span>
              </span>
              <span class="font-semibold text-gray-900 bg-gray-100 px-3 py-1 rounded-full">
                {{ project.task_count }}
              </span>
            </div>
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-500 flex items-center space-x-2">
                <UIcon name="i-heroicons-user" />
                <span>Owner</span>
              </span>
              <span class="font-medium text-gray-900">{{ project.owner?.username }}</span>
            </div>
            <div v-if="project.start_date" class="flex items-center justify-between text-sm">
              <span class="text-gray-500 flex items-center space-x-2">
                <UIcon name="i-heroicons-calendar" />
                <span>Start Date</span>
              </span>
              <span class="font-medium text-gray-900">{{ formatDate(project.start_date) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Create Project Modal -->
    <UModal v-model="isCreateModalOpen" :ui="{ width: 'sm:max-w-2xl' }">
      <UCard>
        <template #header>
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-primary-100 rounded-xl flex items-center justify-center">
              <UIcon name="i-heroicons-folder-plus" class="text-xl text-primary-600" />
            </div>
            <div>
              <h3 class="text-xl font-bold text-gray-900">Create New Project</h3>
              <p class="text-sm text-gray-500">Fill in the details below</p>
            </div>
          </div>
        </template>
        
        <form @submit.prevent="createProject" class="space-y-6">
          <UFormGroup label="Project Name" required>
            <UInput 
              v-model="newProject.name" 
              placeholder="Enter project name" 
              size="lg"
              icon="i-heroicons-folder"
            />
          </UFormGroup>
          
          <UFormGroup label="Description">
            <UTextarea 
              v-model="newProject.description" 
              placeholder="Enter project description"
              :rows="4"
            />
          </UFormGroup>
          
          <UFormGroup label="Status">
            <USelectMenu
              v-model="newProject.status"
              :options="statusOptions"
              option-attribute="label"
              value-attribute="value"
              size="lg"
            />
          </UFormGroup>
          
          <div class="grid grid-cols-2 gap-4">
            <UFormGroup label="Start Date">
              <UInput v-model="newProject.start_date" type="date" size="lg" />
            </UFormGroup>
            
            <UFormGroup label="End Date">
              <UInput v-model="newProject.end_date" type="date" size="lg" />
            </UFormGroup>
          </div>
        </form>
        
        <template #footer>
          <div class="flex justify-end gap-3">
            <UButton variant="ghost" @click="isCreateModalOpen = false" size="lg">
              Cancel
            </UButton>
            <UButton 
              @click="createProject" 
              :loading="creating"
              icon="i-heroicons-check"
              size="lg"
            >
              Create Project
            </UButton>
          </div>
        </template>
      </UCard>
    </UModal>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default',
})

const api = useApi()
const loading = ref(true)
const creating = ref(false)
const projects = ref<any[]>([])
const isCreateModalOpen = ref(false)

const statusOptions = [
  { label: 'Planning', value: 'planning' },
  { label: 'In Progress', value: 'in_progress' },
  { label: 'Completed', value: 'completed' },
  { label: 'On Hold', value: 'on_hold' },
]

const newProject = ref({
  name: '',
  description: '',
  status: 'planning',
  start_date: '',
  end_date: '',
})

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    planning: 'amber',
    in_progress: 'blue',
    completed: 'green',
    on_hold: 'gray',
  }
  return colors[status] || 'gray'
}

const getStatusGradient = (status: string) => {
  const gradients: Record<string, string> = {
    planning: 'from-amber-400 to-yellow-500',
    in_progress: 'from-blue-400 to-blue-600',
    completed: 'from-green-400 to-emerald-600',
    on_hold: 'from-gray-400 to-gray-500',
  }
  return gradients[status] || 'from-gray-400 to-gray-500'
}

const formatStatus = (status: string) => {
  return status.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString('en-US', { 
    month: 'short', 
    day: 'numeric', 
    year: 'numeric' 
  })
}

const loadProjects = async () => {
  try {
    loading.value = true
    const data = await api.getProjects()
    projects.value = data.results || data || []
  } catch (error) {
    console.error('Error loading projects:', error)
  } finally {
    loading.value = false
  }
}

const createProject = async () => {
  try {
    creating.value = true
    const projectData: any = {
      name: newProject.value.name,
      description: newProject.value.description,
      status: newProject.value.status,
    }
    
    if (newProject.value.start_date) {
      projectData.start_date = newProject.value.start_date
    }
    if (newProject.value.end_date) {
      projectData.end_date = newProject.value.end_date
    }
    
    await api.createProject(projectData)
    isCreateModalOpen.value = false
    newProject.value = {
      name: '',
      description: '',
      status: 'planning',
      start_date: '',
      end_date: '',
    }
    await loadProjects()
  } catch (error) {
    console.error('Error creating project:', error)
  } finally {
    creating.value = false
  }
}

onMounted(() => {
  loadProjects()
})
</script>
