<template>
  <div>
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-gray-900">Tasks</h1>
        <p class="text-gray-600 mt-2">Manage all your tasks</p>
      </div>
    </div>

    <!-- Filters -->
    <UCard class="mb-6">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <UFormGroup label="Status">
          <USelect
            v-model="filters.status"
            :options="[{ label: 'All', value: '' }, ...taskStatusOptions]"
            option-attribute="label"
            value-attribute="value"
            @change="loadTasks"
          />
        </UFormGroup>
        
        <UFormGroup label="Priority">
          <USelect
            v-model="filters.priority"
            :options="[{ label: 'All', value: '' }, ...priorityOptions]"
            option-attribute="label"
            value-attribute="value"
            @change="loadTasks"
          />
        </UFormGroup>
        
        <UFormGroup label="Search">
          <UInput v-model="filters.search" placeholder="Search tasks..." @input="loadTasks" />
        </UFormGroup>
        
        <div class="flex items-end">
          <UButton @click="resetFilters" variant="ghost">Reset Filters</UButton>
        </div>
      </div>
    </UCard>

    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-500">Loading tasks...</p>
    </div>

    <div v-else-if="tasks.length === 0" class="text-center py-12">
      <p class="text-gray-500 mb-4">No tasks found</p>
    </div>

    <div v-else class="space-y-4">
      <UCard
        v-for="task in tasks"
        :key="task.id"
        class="cursor-pointer hover:shadow-md transition-shadow"
        @click="navigateTo(`/tasks/${task.id}`)"
      >
        <div class="flex justify-between items-start mb-3">
          <div class="flex-1">
            <h3 class="text-lg font-semibold mb-1">{{ task.title }}</h3>
            <p class="text-gray-600 text-sm mb-2">{{ task.description || 'No description' }}</p>
          </div>
          <div class="flex gap-2 ml-4">
            <UBadge :color="getStatusColor(task.status)">{{ task.status }}</UBadge>
            <UBadge :color="getPriorityColor(task.priority)">{{ task.priority }}</UBadge>
          </div>
        </div>
        
        <div class="flex items-center justify-between text-sm text-gray-500">
          <div class="flex items-center gap-4">
            <span>Project: {{ task.project?.name }}</span>
            <span>Assignee: {{ task.assignee?.username || 'Unassigned' }}</span>
          </div>
          <span>Due: {{ task.due_date ? formatDate(task.due_date) : 'No due date' }}</span>
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
const tasks = ref<any[]>([])

const filters = ref({
  status: '',
  priority: '',
  search: '',
})

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

const loadTasks = async () => {
  try {
    loading.value = true
    const filterParams: any = {}
    
    if (filters.value.status) {
      filterParams.status = filters.value.status
    }
    if (filters.value.priority) {
      filterParams.priority = filters.value.priority
    }
    if (filters.value.search) {
      filterParams.search = filters.value.search
    }
    
    const data = await api.getTasks(filterParams)
    tasks.value = data.results || data || []
  } catch (error) {
    console.error('Error loading tasks:', error)
  } finally {
    loading.value = false
  }
}

const resetFilters = () => {
  filters.value = {
    status: '',
    priority: '',
    search: '',
  }
  loadTasks()
}

onMounted(() => {
  loadTasks()
})
</script>
