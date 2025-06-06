import React, { createContext, useState } from 'react';

export const AuthContext = createContext({
  userId: null,
  token: null,
});

export function AuthProvider({ children }) {
  const [userId, setUserId] = useState('12345');
  const [token, setToken] = useState(null); // TODO: Provide a valid token after user login

  return (
    <AuthContext.Provider value={{ userId, token }}>
      {children}
    </AuthContext.Provider>
  );
}
