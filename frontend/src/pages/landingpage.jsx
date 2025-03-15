import React from 'react';
import './landingpage.css';
import welcome from '../assets/welcome.png';

const LandingPage = () => {
    return (
        <div className='landing-page'>
            <img src={welcome} alt='welcome' className='welcome-image' />
        </div>
    );
};

export default LandingPage;