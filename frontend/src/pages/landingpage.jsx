import React from 'react';
import './landingpage.css';
import welcome from '../assets/welcome.png';
import makerereLogo from '../assets/makerere.logo.png';

const LandingPage = () => {
    return (
        <div className='landing-page'>
            <div className="logo">AITS</div>
            <img src={welcome} alt='welcome' className='welcome-image' />
            <img src={makerereLogo} alt="Makerere University Logo" className="makerere-logo" />
            <div className="welcome-text"> WELCOME TO THE ACADEMIC ISSUE TRACKING SYSTEM</div>
        </div>
    );
};

export default LandingPage;