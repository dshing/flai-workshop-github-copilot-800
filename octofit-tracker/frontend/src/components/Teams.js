import React, { useState, useEffect } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      const apiUrl = process.env.REACT_APP_CODESPACE_NAME
        ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`
        : 'http://localhost:8000/api/teams/';
      
      console.log('Teams - Fetching from API URL:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Teams - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        console.log('Teams - Processed data:', teamsData);
        setTeams(teamsData);
      } catch (err) {
        console.error('Teams - Error fetching data:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="container mt-4"><div className="page-container"><div className="alert alert-info">Loading teams...</div></div></div>;
  if (error) return <div className="container mt-4"><div className="page-container"><div className="alert alert-danger">Error: {error}</div></div></div>;

  return (
    <div className="container mt-4">
      <div className="page-container">
        <h2 className="page-header">👥 Teams</h2>
        <div className="row g-4">
          {teams.map((team) => (
            <div key={team.id} className="col-md-6">
              <div className="card h-100">
                <div className="card-body">
                  <div className="d-flex justify-content-between align-items-start mb-3">
                    <h4 className="card-title mb-0">{team.name}</h4>
                  </div>
                  <p className="card-text text-muted">{team.description}</p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center mt-3">
                    <div>
                      <span className="badge bg-primary me-2">💯 {team.total_points} Points</span>
                      <span className="badge bg-secondary">👤 {team.member_count} Members</span>
                    </div>
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

export default Teams;
