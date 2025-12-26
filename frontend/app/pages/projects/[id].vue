<template>
  <div>
    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-500">Loading project...</p>
    </div>

    <div v-else-if="project">
      <div class="mb-8">
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center gap-4">
            <UButton icon="i-heroicons-arrow-left" variant="ghost" @click="navigateTo('/projects')">
              Back
            </UButton>
            <h1 class="text-3xl font-bold text-gray-900">{{ project.name }}</h1>
            <UBadge :color="getStatusColor(project.status)">{{ project.status }}</UBadge>
          </div>
        </div>
        <p class="text-gray-600">{{ project.description || 'No description' }}</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        <UCard>
          <template #header>
            <h3 class="text-sm font-semibold text-gray-500">Owner</h3>
          </template>
          <p class="text-lg font-medium">{{ project.owner?.username }}</p>
        </UCard>

        <UCard>
          <template #header>
            <h3 class="text-sm font-semibold text-gray-500">Start Date</h3>
          </template>
          <p class="text-lg font-medium">{{ project.start_date ? formatDate(project.start_date) : 'Not set' }}</p>
        </UCard>

        <UCard>
          <template #header>
            <h3 class="text-sm font-semibold text-gray-500">End Date</h3>
          </template>
          <p class="text-lg font-medium">{{ project.end_date ? formatDate(project.end_date) : 'Not set' }}</p>
        </UCard>
      </div>

      <UCard>
        <template #header>
          <div class="flex justify-between items-center">
            <h3 class="text-lg font-semibold">Tasks</h3>
            <UButton @click="isCreateTaskModalOpen = true" icon="i-heroicons-plus" size="sm">
              New Task
            </UButton>
          </div>
        </template>

        <div v-if="loadingTasks" class="text-center py-8">
          <p class="text-gray-500">Loading tasks...</p>
        </div>

        <div v-else-if="tasks.length === 0" class="text-center py-8">
          <p class="text-gray-500 mb-4">No tasks yet. Create your first task!</p>
          <UButton @click="isCreateTaskModalOpen = true">Create Task</UButton>
        </div>

        <div v-else class="space-y-3">
          <div
            v-for="task in tasks"
            :key="task.id"
            class="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 cursor-pointer"
            @click="navigateTo(`/tasks/${task.id}`)"
          >
            <div class="flex justify-between items-start mb-2">
              <h4 class="font-medium">{{ task.title }}</h4>
              <div class="flex gap-2">
                <UBadge :color="getStatusColor(task.status)">{{ task.status }}</UBadge>
                <UBadge :color="getPriorityColor(task.priority)">{{ task.priority }}</UBadge>
              </div>
            </div>
            <p class="text-sm text-gray-600 mb-2">{{ task.description }}</p>
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-500">
                Assignee: {{ task.assignee?.username || 'Unassigned' }}
              </span>
              <span class="text-gray-500">
                Due: {{ task.due_date ? formatDate(task.due_date) : 'No due date' }}
              </span>
            </div>
          </div>
        </div>
      </UCard>
    </div>

    <!-- Create Task Modal -->
    <UModal v-model="isCreateTaskModalOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-semibold">Create New Task</h3>
        </template>
        
        <form @submit.prevent="createTask" class="space-y-4">
          <UFormGroup label="Task Title" required>
            <UInput v-model="newTask.title" placeholder="Enter task title" />
          </UFormGroup>
          
          <UFormGroup label="Description">
            <UTextarea v-model="newTask.description" placeholder="Enter task description" />
          </UFormGroup>
          
          <div class="grid grid-cols-2 gap-4">
            <UFormGroup label="Status">
              <USelect
                v-model="newTask.status"
                :options="taskStatusOptions"
                option-attribute="label"
                value-attribute="value"
              />
            </UFormGroup>
            
            <UFormGroup label="Priority">
              <USelect
                v-model="newTask.priority"
                :options="priorityOptions"
                option-attribute="label"
                value-attribute="value"
              />
            </UFormGroup>
          </div>
          
          <UFormGroup label="Due Date">
            <UInput v-model="newTask.due_date" type="date" />
          </UFormGroup>
        </form>
        
        <template #footer>
          <div class="flex justify-end gap-2">
            <UButton variant="ghost" @click="isCreateTaskModalOpen = false">Cancel</UButton>
            <UButton @click="createTask" :loading="creatingTask">Create</UButton>
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

const route = useRoute()
const api = useApi()
const loading = ref(true)
const loadingTasks = ref(true)
const creatingTask = ref(false)
const project = ref<any>(null)
const tasks = ref<any[]>([])
const isCreateTaskModalOpen = ref(false)

const taskStatusOptions = [
  { label: 'To Do', value: 'todo' },
  { label: 'In Progress', value: 'in_progress' },
  { label: 'In Review', value: 'review' },
  { label: 'Done', value: 'done' },
]

const priorityOptions = [
  { label: 'Low', value: 'low' },
  { label: 'Medium', value: 'medium' },
  { label: 'High', value: 'high' },
  { label: 'Urgent', value: 'urgent' },
]

const newTask = ref({
  title: '',
  description: '',
  status: 'todo',
  priority: 'medium',
  due_date: '',
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

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString()
}

const loadProject = async () => {
  try {
    loading.value = true
    const projectId = parseInt(route.params.id as string)
    project.value = await api.getProject(projectId)
  } catch (error) {
    console.error('Error loading project:', error)
  } finally {
    loading.value = false
  }
}

const loadTasks = async () => {
  try {
    loadingTasks.value = true
    const projectId = parseInt(route.params.id as string)
    const data = await api.getTasks({ project: projectId })
    tasks.value = data.results || data || []
  } catch (error) {
    console.error('Error loading tasks:', error)
  } finally {
    loadingTasks.value = false
  }
}

const createTask = async () => {
  try {
    creatingTask.value = true
    const projectId = parseInt(route.params.id as string)
    const taskData: any = {
      title: newTask.value.title,
      description: newTask.value.description,
      status: newTask.value.status,
      priority: newTask.value.priority,
      project_id: projectId,
    }
    
    if (newTask.value.due_date) {
      taskData.due_date = newTask.value.due_date
    }
    
    await api.createTask(taskData)
    isCreateTaskModalOpen.value = false
    newTask.value = {
      title: '',
      description: '',
      status: 'todo',
      priority: 'medium',
      due_date: '',
    }
    await loadTasks()
  } catch (error) {
    console.error('Error creating task:', error)
  } finally {
    creatingTask.value = false
  }
}

onMounted(async () => {
  await Promise.all([loadProject(), loadTasks()])
})
</script>
