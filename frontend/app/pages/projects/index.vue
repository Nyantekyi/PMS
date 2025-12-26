<template>
  <div>
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Projects</h1>
        <p class="text-gray-600 mt-2">Manage your projects</p>
      </div>
      <UButton @click="isCreateModalOpen = true" icon="i-heroicons-plus">
        New Project
      </UButton>
    </div>

    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-500">Loading projects...</p>
    </div>

    <div v-else-if="projects.length === 0" class="text-center py-12">
      <p class="text-gray-500 mb-4">No projects yet. Create your first project!</p>
      <UButton @click="isCreateModalOpen = true">Create Project</UButton>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <UCard
        v-for="project in projects"
        :key="project.id"
        class="cursor-pointer hover:shadow-lg transition-shadow"
        @click="navigateTo(`/projects/${project.id}`)"
      >
        <template #header>
          <div class="flex justify-between items-start">
            <h3 class="text-lg font-semibold">{{ project.name }}</h3>
            <UBadge :color="getStatusColor(project.status)">{{ project.status }}</UBadge>
          </div>
        </template>
        
        <p class="text-gray-600 text-sm mb-4">{{ project.description || 'No description' }}</p>
        
        <div class="space-y-2 text-sm">
          <div class="flex justify-between">
            <span class="text-gray-500">Tasks:</span>
            <span class="font-medium">{{ project.task_count }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">Owner:</span>
            <span class="font-medium">{{ project.owner?.username }}</span>
          </div>
          <div v-if="project.start_date" class="flex justify-between">
            <span class="text-gray-500">Start Date:</span>
            <span class="font-medium">{{ formatDate(project.start_date) }}</span>
          </div>
        </div>
      </UCard>
    </div>

    <!-- Create Project Modal -->
    <UModal v-model="isCreateModalOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Create New Project</h3>
        </template>
        
        <form @submit.prevent="createProject" class="space-y-4">
          <UFormGroup label="Project Name" required>
            <UInput v-model="newProject.name" placeholder="Enter project name" />
          </UFormGroup>
          
          <UFormGroup label="Description">
            <UTextarea v-model="newProject.description" placeholder="Enter project description" />
          </UFormGroup>
          
          <UFormGroup label="Status">
            <USelect
              v-model="newProject.status"
              :options="statusOptions"
              option-attribute="label"
              value-attribute="value"
            />
          </UFormGroup>
          
          <div class="grid grid-cols-2 gap-4">
            <UFormGroup label="Start Date">
              <UInput v-model="newProject.start_date" type="date" />
            </UFormGroup>
            
            <UFormGroup label="End Date">
              <UInput v-model="newProject.end_date" type="date" />
            </UFormGroup>
          </div>
        </form>
        
        <template #footer>
          <div class="flex justify-end gap-2">
            <UButton variant="ghost" @click="isCreateModalOpen = false">Cancel</UButton>
            <UButton @click="createProject" :loading="creating">Create</UButton>
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
    planning: 'yellow',
    in_progress: 'blue',
    completed: 'green',
    on_hold: 'gray',
  }
  return colors[status] || 'gray'
}

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString()
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
