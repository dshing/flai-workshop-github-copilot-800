import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Teams from './components/Teams';
import Users from './components/Users';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              🏋️ OctoFit Tracker
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">
                    Users
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div>
      <div className="hero-section text-center">
        <div className="container">
          <h1 className="display-3">Welcome to OctoFit Tracker! 🏋️‍♀️</h1>
          <p className="lead">Track your fitness journey with Marvel and DC superheroes!</p>
          <p className="mt-3">Join the ultimate fitness challenge where heroes compete for glory!</p>
        </div>
      </div>
      <div className="container">
        <div className="page-container">
          <h2 className="page-header text-center mb-4">Get Started</h2>
          <div className="row g-4">
            <div className="col-md-4">
              <div className="card text-center h-100">
                <div className="card-body d-flex flex-column">
                  <div className="mb-3">
                    <span style={{fontSize: '3rem'}}>🏆</span>
                  </div>
                  <h5 className="card-title">Leaderboard</h5>
                  <p className="card-text">See who's leading the fitness challenge and compete for the top spot!</p>
                  <div className="mt-auto">
                    <Link to="/leaderboard" className="btn btn-primary">View Rankings</Link>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card text-center h-100">
                <div className="card-body d-flex flex-column">
                  <div className="mb-3">
                    <span style={{fontSize: '3rem'}}>👥</span>
                  </div>
                  <h5 className="card-title">Teams</h5>
                  <p className="card-text">Marvel vs DC - Join a team and contribute to their victory!</p>
                  <div className="mt-auto">
                    <Link to="/teams" className="btn btn-primary">View Teams</Link>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card text-center h-100">
                <div className="card-body d-flex flex-column">
                  <div className="mb-3">
                    <span style={{fontSize: '3rem'}}>💪</span>
                  </div>
                  <h5 className="card-title">Workouts</h5>
                  <p className="card-text">Discover superhero-inspired workout routines tailored to your level!</p>
                  <div className="mt-auto">
                    <Link to="/workouts" className="btn btn-primary">Browse Workouts</Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
