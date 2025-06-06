import React, { createContext, useState } from 'react';

export const AuthContext = createContext({
  userId: null,
  token: null,
});

export function AuthProvider({ children }) {
  const [userId, setUserId] = useState('12345');
  const [token, setToken] = useState('mock-token-abc123');

  // In a real app, this would come from login flow

  return (
    <AuthContext.Provider value={{ userId, token }}>
      {children}
    </AuthContext.Provider>
  );
}
