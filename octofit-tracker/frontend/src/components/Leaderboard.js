import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaders, setLeaders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const apiUrl = process.env.REACT_APP_CODESPACE_NAME
        ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`
        : 'http://localhost:8000/api/leaderboard/';
      
      console.log('Leaderboard - Fetching from API URL:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Leaderboard - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        console.log('Leaderboard - Processed data:', leaderboardData);
        setLeaders(leaderboardData);
      } catch (err) {
        console.error('Leaderboard - Error fetching data:', err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="container mt-4"><div className="alert alert-info">Loading leaderboard...</div></div>;
  if (error) return <div className="container mt-4"><div className="alert alert-danger">Error: {error}</div></div>;

  return (
    <div className="container mt-4">
      <h2 className="mb-4">🏆 Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Rank</th>
              <th>User</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Activities</th>
              <th>Last Activity</th>
            </tr>
          </thead>
          <tbody>
            {leaders.map((leader) => (
              <tr key={leader.id} className={leader.rank <= 3 ? 'table-warning' : ''}>
                <td>
                  <strong>
                    {leader.rank === 1 && '🥇 '}
                    {leader.rank === 2 && '🥈 '}
                    {leader.rank === 3 && '🥉 '}
                    #{leader.rank}
                  </strong>
                </td>
                <td>{leader.user_name}</td>
                <td><span className={`badge ${leader.team === 'Team Marvel' ? 'bg-danger' : 'bg-primary'}`}>{leader.team}</span></td>
                <td><strong>{leader.total_points}</strong></td>
                <td><span className="badge bg-info">{leader.activities_count}</span></td>
                <td>{leader.last_activity ? new Date(leader.last_activity).toLocaleDateString() : 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
