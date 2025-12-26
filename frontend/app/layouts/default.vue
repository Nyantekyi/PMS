<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-blue-50 to-indigo-50">
    <header class="bg-white/80 backdrop-blur-md border-b border-gray-200/50 sticky top-0 z-50 shadow-sm">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <nav class="flex items-center justify-between">
          <div class="flex items-center space-x-8">
            <NuxtLink to="/" class="flex items-center space-x-2 group">
              <div class="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-600 rounded-xl flex items-center justify-center shadow-lg group-hover:shadow-xl transition-all duration-300">
                <span class="text-white font-bold text-lg">P</span>
              </div>
              <span class="text-2xl font-bold bg-gradient-to-r from-primary-600 to-primary-700 bg-clip-text text-transparent">
                ProjectHub
              </span>
            </NuxtLink>
            <div class="hidden md:flex space-x-2">
              <UButton to="/" variant="ghost" icon="i-heroicons-home" class="transition-all duration-200">
                Dashboard
              </UButton>
              <UButton to="/projects" variant="ghost" icon="i-heroicons-folder" class="transition-all duration-200">
                Projects
              </UButton>
              <UButton to="/tasks" variant="ghost" icon="i-heroicons-clipboard-document-list" class="transition-all duration-200">
                Tasks
              </UButton>
            </div>
          </div>
          <div class="flex items-center space-x-3">
            <UButton icon="i-heroicons-bell" variant="ghost" color="gray" size="lg" />
            <UButton icon="i-heroicons-user-circle" variant="ghost" color="gray" size="lg" />
          </div>
        </nav>
      </div>
    </header>
    
    <main class="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <slot />
    </main>
    
    <footer class="mt-auto py-8 bg-white/50 backdrop-blur-sm border-t border-gray-200/50">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 text-center text-gray-600">
        <p class="text-sm">© 2025 ProjectHub. Built with Nuxt & Django</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
</script>
