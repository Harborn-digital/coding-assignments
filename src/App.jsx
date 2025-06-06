import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import UserProfileDashboard from './components/UserProfileDashboard';
import { AuthProvider } from './contexts/AuthContext';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<UserProfileDashboard />} />
          <Route path="/settings" element={<div>Settings Page</div>} />
          <Route path="/messages" element={<div>Messages Page</div>} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
