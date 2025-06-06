# React code structure

Bekijk deze component. Welke verbeteringen zou je voorstellen op het gebied van structuur, herbruikbaarheid en onderhoudbaarheid? Je mag denken aan component splitting, hooks, stijlgebruik, API-laag scheiding, etc. Je hoeft het niet volledig opnieuw te schrijven, maar je mag het wel doen als dat je helpt.

```
import React, { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [name, setName] = useState('');
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setName(data.name);
      });
  }, [userId]);

  const handleSave = () => {
    setSaving(true);
    fetch(`/api/users/${userId}`, {
      method: 'POST',
      body: JSON.stringify({ name }),
      headers: { 'Content-Type': 'application/json' },
    })
      .then(() => {
        setUser((prev) => ({ ...prev, name }));
        setEditMode(false);
      })
      .finally(() => setSaving(false));
  };

  if (!user) return <p>Loading...</p>;

  return (
    <div style={{ border: '1px solid gray', padding: 20 }}>
      <h2>User Profile</h2>
      {editMode ? (
        <div>
          <input value={name} onChange={(e) => setName(e.target.value)} />
          <button onClick={handleSave} disabled={saving}>
            {saving ? 'Saving...' : 'Save'}
          </button>
        </div>
      ) : (
        <div>
          <p>Name: {user.name}</p>
          <button onClick={() => setEditMode(true)}>Edit</button>
        </div>
      )}
    </div>
  );
}

export default UserProfile;
```