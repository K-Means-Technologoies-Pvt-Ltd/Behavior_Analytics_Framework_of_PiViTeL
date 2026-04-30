import React from 'react';
import './DescriptiveAnalysis.css';

const DescriptiveAnalysis = () => {
  const missingCategories = [
    { category: 'Completely Missing', columns: 'overlay_time, overlay_date, overlay_gps, overlay_accel_g, overlay_gyro_deg_s' },
    { category: 'High Missing', columns: 'detection_id, tracking_id, class, confidence, bbox_x, bbox_y, bbox_w, bbox_h, position, distance_m' },
    { category: 'Moderate Missing', columns: 'gps_speed_kmh, gps_course_degrees' },
    { category: 'Low Missing', columns: 'latitude, longitude, gps_altitude, gps_hdop, gps_data_age_seconds' },
  ];

  const missingSummary = [
    { name: 'overlay_time', count: 4398, percent: 100.0 },
    { name: 'overlay_date', count: 4398, percent: 100.0 },
    { name: 'overlay_gps', count: 4398, percent: 100.0 },
    { name: 'overlay_accel_g', count: 4398, percent: 100.0 },
    { name: 'overlay_gyro_deg_s', count: 4398, percent: 100.0 },
    { name: 'detection_id', count: 1098, percent: 24.97 },
    { name: 'tracking_id', count: 1098, percent: 24.97 },
    { name: 'class', count: 1098, percent: 24.97 },
    { name: 'confidence', count: 1098, percent: 24.97 },
    { name: 'bbox_x', count: 1098, percent: 24.97 },
    { name: 'bbox_y', count: 1098, percent: 24.97 },
    { name: 'bbox_w', count: 1098, percent: 24.97 },
    { name: 'bbox_h', count: 1098, percent: 24.97 },
    { name: 'position', count: 1098, percent: 24.97 },
    { name: 'distance_m', count: 1098, percent: 24.97 },
    { name: 'gps_speed_kmh', count: 485, percent: 11.03 },
    { name: 'gps_course_degrees', count: 485, percent: 11.03 },
    { name: 'latitude', count: 69, percent: 1.57 },
    { name: 'longitude', count: 69, percent: 1.57 },
    { name: 'gps_altitude', count: 69, percent: 1.57 },
    { name: 'gps_hdop', count: 69, percent: 1.57 },
    { name: 'gps_data_age_seconds', count: 69, percent: 1.57 },
  ];

  return (
    <div className="descriptive-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h2 className="section-title" style={{ marginBottom: 0 }}>Descriptive Analysis</h2>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <a href="https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL/blob/main/analytics/descriptive_analysis.py" target="_blank" rel="noopener noreferrer" className="see-code-btn">
            Descriptive Analysis Code
          </a>
          <a href="https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL/blob/main/analytics/missing_value_investigation.py" target="_blank" rel="noopener noreferrer" className="see-code-btn">
            Missing Value Code
          </a>
        </div>
      </div>
      <div className="cards-grid">
        <div className="card">
          <h3>Statistical Summary</h3>
          <p className="description">Descriptive analysis output for Central Tendency, Variability, and Extremes.</p>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '2rem', marginTop: '1rem' }}>
            <div style={{ flex: 1 }}>
              <h4 style={{ color: '#a855f7', marginBottom: '0.5rem', fontSize: '1.1rem' }}>Central Tendency</h4>
              <ul style={{ listStyle: 'none', padding: 0, color: 'var(--text-secondary)', lineHeight: 1.8 }}>
                <li><strong>Average Speed:</strong> 33.03 km/h</li>
                <li><strong>Median Speed:</strong> 34.97 km/h</li>
                <li><strong>Average Acceleration:</strong> 9.92 m/s²</li>
                <li><strong>Average Distance:</strong> 29.61 m</li>
              </ul>
            </div>
            <div style={{ flex: 1 }}>
              <h4 style={{ color: '#a855f7', marginBottom: '0.5rem', fontSize: '1.1rem' }}>Variability & Extremes</h4>
              <ul style={{ listStyle: 'none', padding: 0, color: 'var(--text-secondary)', lineHeight: 1.8 }}>
                <li><strong>Speed Std Dev:</strong> 9.31</li>
                <li><strong>Distance Std Dev:</strong> 25.41</li>
                <li><strong>Max Speed:</strong> 53.62 km/h</li>
                <li><strong>Min Speed:</strong> 2.30 km/h</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="card">
          <h3>Event Analytics</h3>
          <p className="description">Summary of observed risk events during the trip logs.</p>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '2rem', marginTop: '1rem' }}>
            <div style={{ flex: 1 }}>
              <h4 style={{ color: '#3b82f6', marginBottom: '0.5rem', fontSize: '1.1rem' }}>Event Counts</h4>
              <ul style={{ listStyle: 'none', padding: 0, color: 'var(--text-secondary)', lineHeight: 1.8 }}>
                <li><strong>Overspeed:</strong> 93</li>
                <li><strong>Sudden Acceleration:</strong> 2</li>
                <li><strong>Sudden Braking:</strong> 3</li>
                <li><strong>Close Risk:</strong> 1098</li>
              </ul>
            </div>
            <div style={{ flex: 1 }}>
              <h4 style={{ color: '#3b82f6', marginBottom: '0.5rem', fontSize: '1.1rem' }}>Event Percentages</h4>
              <ul style={{ listStyle: 'none', padding: 0, color: 'var(--text-secondary)', lineHeight: 1.8 }}>
                <li><strong>Overspeed %:</strong> 2.11%</li>
                <li><strong>Acceleration %:</strong> 0.05%</li>
                <li><strong>Braking %:</strong> 0.07%</li>
                <li><strong>Close Risk %:</strong> 24.97%</li>
              </ul>
            </div>
          </div>
        </div>

        <div className="card">
          <h3>Missing Value Categories</h3>
          <p className="description">Attributes categorized by their percentage of missing values.</p>
          <table className="analysis-table">
            <thead>
              <tr>
                <th>Category</th>
                <th>Columns</th>
              </tr>
            </thead>
            <tbody>
              {missingCategories.map((item, idx) => (
                <tr key={idx}>
                  <td><strong>{item.category}</strong></td>
                  <td>{item.columns}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="card">
          <h3>Missing Value Summary</h3>
          <p className="description">Detailed count and percentage of missing values per column.</p>
          <div className="table-responsive">
            <table className="analysis-table summary-table">
              <thead>
                <tr>
                  <th>Column Name</th>
                  <th>Missing Count</th>
                  <th>Missing Percent (%)</th>
                </tr>
              </thead>
              <tbody>
                {missingSummary.map((item, idx) => (
                  <tr key={idx}>
                    <td>{item.name}</td>
                    <td>{item.count}</td>
                    <td>
                      <span className="percent-bar" style={{ width: `${item.percent}%` }}></span>
                      <span className="percent-text">{item.percent}%</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DescriptiveAnalysis;
