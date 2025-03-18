import React from 'react';
import makererelogo from '../assets/makererelogo.png'; // Import the Makerere logo image
import knowledge from '../assets/knowledge.png'; // Import the Knowledge image
import './Dashboard.css'; // Import the corresponding CSS file

const DashboardSetup = () => {
  const handleStartSetup = () => {
    // Handle the start setup logic here
    console.log('Start Setup clicked');
  };

  return (
    <div className="container">
      <img src={makererelogo} alt="Makerere Logo" className="logo" />
      <h1 className="title">Academic Issue Tracking System</h1>
      <h2 className="welcome">Welcome!</h2>
      <p className="description">This is your Dashboard setup</p>
      <p className="description">
        Help us customize your account and preferences to get started quickly.
      </p>
      <button onClick={handleStartSetup} className="button">
        Start Setup
      </button>
      <img src={knowledge} alt="Knowledge" className="knowledge-image" />
    </div>
  );
};

export default DashboardSetup;