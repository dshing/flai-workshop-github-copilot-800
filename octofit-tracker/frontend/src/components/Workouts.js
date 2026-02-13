import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = process.env.REACT_APP_CODESPACE_NAME
        ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`
        : 'http://localhost:8000/api/workouts/';
      
      console.log('Workouts - Fetching from API URL:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        console.log('Workouts - Processed data:', workoutsData);
        setWorkouts(workoutsData);
      } catch (err) {
        console.error('Workouts - Error fetching data:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  const getDifficultyBadge = (difficulty) => {
    const badges = {
      beginner: 'bg-success',
      intermediate: 'bg-warning',
      advanced: 'bg-danger'
    };
    return badges[difficulty] || 'bg-secondary';
  };

  if (loading) return <div className="container mt-4"><div className="page-container"><div className="alert alert-info">Loading workouts...</div></div></div>;
  if (error) return <div className="container mt-4"><div className="page-container"><div className="alert alert-danger">Error: {error}</div></div></div>;

  return (
    <div className="container mt-4">
      <div className="page-container">
        <h2 className="page-header">💪 Workout Plans</h2>
        <p className="text-muted mb-4">Superhero-inspired workout routines for all levels</p>
        <div className="row g-4">
          {workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4">
              <div className="card h-100">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title">{workout.name}</h5>
                  <p className="card-text text-muted">{workout.description}</p>
                  <div className="mb-3">
                    <span className="badge bg-primary me-2">📂 {workout.category}</span>
                    <span className={`badge ${getDifficultyBadge(workout.difficulty)} me-2`}>
                      {workout.difficulty.toUpperCase()}
                    </span>
                    <span className="badge bg-info">⏱️ {workout.duration} min</span>
                  </div>
                  <hr />
                  <div className="d-flex justify-content-between mb-3">
                    <span><strong>🔥 Calories:</strong> {workout.calories_estimate}</span>
                    <span><strong>🏅 Points:</strong> {workout.points}</span>
                  </div>
                  <div className="mb-3">
                    <strong>🏋️ Equipment:</strong>
                    <p className="small mb-0 mt-1">
                      {typeof workout.equipment === 'string' 
                        ? workout.equipment 
                        : Array.isArray(workout.equipment) 
                          ? workout.equipment.join(', ') 
                          : 'None'}
                    </p>
                  </div>
                  <div className="mt-auto">
                    <strong>📝 Instructions:</strong>
                    <ol className="small mt-2 mb-0">
                      {typeof workout.instructions === 'string' 
                        ? <li>{workout.instructions}</li>
                        : Array.isArray(workout.instructions) 
                          ? workout.instructions.map((instruction, idx) => (
                              <li key={idx}>{instruction}</li>
                            ))
                          : <li>No instructions available</li>
                      }
                    </ol>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Workouts;
