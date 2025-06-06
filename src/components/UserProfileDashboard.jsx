import React, { useContext, useEffect, useState } from 'react';
import { AuthContext } from '../contexts/AuthContext';
import { fetchUserData } from '../api/userApi';
import UserInfo from './UserInfo';
import UserStats from './UserStats';
import { Link } from 'react-router-dom';

export default function UserProfileDashboard() {
  const { userId, token } = useContext(AuthContext);
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!userId || !token) {
      setError('User not authenticated');
      setLoading(false);
      return;
    }

    fetchUserData(userId, token)
      .then(data => {
        setUserData(data);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to fetch user data');
        setLoading(false);
      });
  }, [userId, token]);

  if (loading) return <div>Loading user data...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="user-profile-dashboard">
      <h1>Welcome, {userData.name}</h1>
      <UserInfo info={userData.info} />
      <UserStats stats={userData.stats} />

      <nav>
        <ul>
          <li><Link to="/settings">Settings</Link></li>
          <li><Link to="/messages">Messages</Link></li>
        </ul>
      </nav>
    </div>
  );
}
