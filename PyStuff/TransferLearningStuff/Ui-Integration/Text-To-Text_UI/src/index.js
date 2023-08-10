import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import Navbar from './Navbar';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <div>
    <Navbar/>
    <App />
    </div>
);

