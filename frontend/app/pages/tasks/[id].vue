<template>
  <div>
    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-500">Loading task...</p>
    </div>

    <div v-else-if="task">
      <div class="mb-8">
        <div class="flex items-center gap-4 mb-4">
          <UButton icon="i-heroicons-arrow-left" variant="ghost" @click="navigateTo('/tasks')">
            Back
          </UButton>
          <h1 class="text-3xl font-bold text-gray-900">{{ task.title }}</h1>
          <UBadge :color="getStatusColor(task.status)">{{ task.status }}</UBadge>
          <UBadge :color="getPriorityColor(task.priority)">{{ task.priority }}</UBadge>
        </div>
        <p class="text-gray-600">{{ task.description || 'No description' }}</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <UCard>
          <template #header>
            <h3 class="text-lg font-semibold">Task Details</h3>
          </template>
          
          <div class="space-y-4">
            <div>
              <label class="text-sm font-medium text-gray-500">Project</label>
              <p class="text-lg">
                <span
                  class="text-primary-600 cursor-pointer hover:underline"
                  @click="navigateTo(`/projects/${task.project?.id}`)"
                >
                  {{ task.project?.name }}
                </span>
              </p>
            </div>
            
            <div>
              <label class="text-sm font-medium text-gray-500">Assignee</label>
              <p class="text-lg">{{ task.assignee?.username || 'Unassigned' }}</p>
            </div>
            
            <div>
              <label class="text-sm font-medium text-gray-500">Due Date</label>
              <p class="text-lg">{{ task.due_date ? formatDate(task.due_date) : 'No due date' }}</p>
            </div>
            
            <div>
              <label class="text-sm font-medium text-gray-500">Created</label>
              <p class="text-lg">{{ formatDateTime(task.created_at) }}</p>
            </div>
            
            <div>
              <label class="text-sm font-medium text-gray-500">Last Updated</label>
              <p class="text-lg">{{ formatDateTime(task.updated_at) }}</p>
            </div>
          </div>
        </UCard>

        <UCard>
          <template #header>
            <h3 class="text-lg font-semibold">Update Task</h3>
          </template>
          
          <form @submit.prevent="updateTask" class="space-y-4">
            <UFormGroup label="Status">
              <USelect
                v-model="editTask.status"
                :options="taskStatusOptions"
                option-attribute="label"
                value-attribute="value"
              />
            </UFormGroup>
            
            <UFormGroup label="Priority">
              <USelect
                v-model="editTask.priority"
                :options="priorityOptions"
                option-attribute="label"
                value-attribute="value"
              />
            </UFormGroup>
            
            <UFormGroup label="Due Date">
              <UInput v-model="editTask.due_date" type="date" />
            </UFormGroup>
            
            <UButton type="submit" :loading="updating" class="w-full">
              Update Task
            </UButton>
          </form>
        </UCard>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: 'default',
})

const route = useRoute()
const api = useApi()
const loading = ref(true)
const updating = ref(false)
const task = ref<any>(null)

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

const editTask = ref({
  status: '',
  priority: '',
  due_date: '',
})

const getStatusColor = (status: string) => {
  const colors: Record<string, string> = {
    todo: 'gray',
    in_progress: 'blue',
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

const formatDateTime = (dateString: string) => {
  return new Date(dateString).toLocaleString()
}

const loadTask = async () => {
  try {
    loading.value = true
    const taskId = parseInt(route.params.id as string)
    task.value = await api.getTask(taskId)
    
    // Initialize edit form
    editTask.value = {
      status: task.value.status,
      priority: task.value.priority,
      due_date: task.value.due_date || '',
    }
  } catch (error) {
    console.error('Error loading task:', error)
  } finally {
    loading.value = false
  }
}

const updateTask = async () => {
  try {
    updating.value = true
    const taskId = parseInt(route.params.id as string)
    const updateData: any = {
      title: task.value.title,
      description: task.value.description,
      status: editTask.value.status,
      priority: editTask.value.priority,
      project_id: task.value.project.id,
    }
    
    if (editTask.value.due_date) {
      updateData.due_date = editTask.value.due_date
    }
    
    task.value = await api.updateTask(taskId, updateData)
  } catch (error) {
    console.error('Error updating task:', error)
  } finally {
    updating.value = false
  }
}

onMounted(() => {
  loadTask()
})
</script>
