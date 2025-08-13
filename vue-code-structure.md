# Vue code structure

Bekijk dit component. Welke verbeteringen zou je voorstellen op het gebied van structuur, herbruikbaarheid en onderhoudbaarheid? Denk hierbij aan concepten zoals component splitting, composables, stijlgebruik, API-laag scheiding én het gebruik van TypeScript. Je hoeft het niet volledig opnieuw te schrijven, maar je mag het wel doen als dat je helpt.

```
<script setup>
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
  userId: {
    type: Number,
    required: true,
  },
});

const user = ref(null);
const editMode = ref(false);
const name = ref('');
const saving = ref(false);

const fetchUser = () => {
  fetch(`/api/users/${props.userId}`)
    .then((res) => res.json())
    .then((data) => {
      user.value = data;
      name.value = data.name;
    });
};

const handleSave = () => {
  saving.value = true;
  fetch(`/api/users/${props.userId}`, {
    method: 'POST',
    body: JSON.stringify({ name: name.value }),
    headers: { 'Content-Type': 'application/json' },
  })
    .then(() => {
      user.value.name = name.value;
      editMode.value = false;
    })
    .finally(() => (saving.value = false));
};

onMounted(() => {
  fetchUser();
});

watch(() => props.userId, fetchUser);
</script>

<template>
  <div style="border: 1px solid gray; padding: 20px">
    <h2>User Profile</h2>
    <div v-if="editMode">
      <input v-model="name" />
      <button @click="handleSave" :disabled="saving">
        {{ saving ? 'Saving...' : 'Save' }}
      </button>
    </div>
    <div v-else>
      <p>Name: {{ user.name }}</p>
      <button @click="editMode = true">Edit</button>
    </div>
  </div>
</template>
```
