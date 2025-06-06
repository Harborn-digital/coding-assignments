import React from 'react';

export default function UserInfo({ info }) {
  return (
    <section>
      <h2>User Information</h2>
      <p>Email: {info.email}</p>
      <p>Location: {info.location}</p>
    </section>
  );
}
