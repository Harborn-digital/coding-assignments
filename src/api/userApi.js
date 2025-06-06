export async function fetchUserData(userId, token) {
  const response = await fetch(`https://api.example.com/users/${userId}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  if (!response.ok) {
    throw new Error('API error');
  }

  return await response.json();
}
