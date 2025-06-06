import React from 'react';

export default function UserStats({ stats }) {
  return (
    <section>
      <h2>User Stats</h2>
      <ul>
        <li>Posts: {stats.posts}</li>
        <li>Followers: {stats.followers}</li>
        <li>Following: {stats.following}</li>
      </ul>
    </section>
  );
}
