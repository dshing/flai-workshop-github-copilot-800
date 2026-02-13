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

  if (loading) return <div className="container mt-4"><div className="alert alert-info">Loading workouts...</div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">💪 Workouts</h2>
      <div className="row">
        {workouts.map((workout) => (
          <div key={workout.id} className="col-md-6 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">{workout.description}</p>
                <div className="mb-3">
                  <span className="badge bg-primary me-2">{workout.category}</span>
                  <span className={`badge ${getDifficultyBadge(workout.difficulty)} me-2`}>
                    {workout.difficulty}
                  </span>
                  <span className="badge bg-info">{workout.duration} min</span>
                </div>
                <div className="d-flex justify-content-between mb-2">
                  <small>Calories: {workout.calories_estimate}</small>
                  <small>Points: {workout.points}</small>
                </div>
                <div className="mt-3">
                  <strong>Equipment:</strong>
                  <p className="small mb-2">
                    {typeof workout.equipment === 'string' 
                      ? workout.equipment 
                      : Array.isArray(workout.equipment) 
                        ? workout.equipment.join(', ') 
                        : 'None'}
                  </p>
                  <strong>Instructions:</strong>
                  <ol className="small">
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
  );
};

export default Workouts;
