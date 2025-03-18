import React, { useState } from 'react';
import makererelogo from '../assets/makererelogo.png'; // Import the Makerere logo
import upload from '../assets/upload.png'; // Import the vector image
import './profilepicture.css'; // Import the corresponding CSS file

const ProfilePictureSetup = () => {
  const [currentPicture, setCurrentPicture] = useState(null);
  const [newPicture, setNewPicture] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setNewPicture(URL.createObjectURL(file));
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (newPicture) {
      setCurrentPicture(newPicture);
      setNewPicture(null);
    }
  };

  return (
    <div className="profile-picture-setup">
      <div className="title-container">
        <img src={makererelogo} alt="Makerere University Logo" className="logo" />
        <h1 className="title">Academic Issue Tracking System</h1>
      </div>
      <h2>Profile Picture Setup</h2>
      <p className="description">Let's also set your profile picture</p>

      <div className="current-picture">
        <h3>Current Picture</h3>
        {currentPicture ? (
          <img src={upload} alt="upload" className="upload" />
        ) : (
          <p>None</p>
        )}
      </div>

      <form onSubmit={handleSubmit}>
        <div className="new-picture">
          <h3>New Picture</h3>
          <input type="file" onChange={handleFileChange} accept="image/*" />
          {newPicture && (
            <img src={Vector} alt="New Profile" className="profile-image" />
          )}
        </div>

        <div className="button-group">
          <button type="button" className="button back-button">Back</button>
          <button type="submit" className="button next-button">Next</button>
        </div>
      </form>
    </div>
  );
};

export default ProfilePictureSetup;