<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-white border-b border-gray-200">
      <div class="container mx-auto px-4 py-4">
        <nav class="flex items-center justify-between">
          <div class="flex items-center space-x-8">
            <NuxtLink to="/" class="text-2xl font-bold text-primary-600">
              PMS
            </NuxtLink>
            <div class="flex space-x-4">
              <UButton to="/" variant="ghost">Dashboard</UButton>
              <UButton to="/projects" variant="ghost">Projects</UButton>
              <UButton to="/tasks" variant="ghost">Tasks</UButton>
            </div>
          </div>
        </nav>
      </div>
    </header>
    
    <main class="container mx-auto px-4 py-8">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
</script>
