import React from 'react';
import './FeatureSelection.css';

const FeatureSelection = () => {
  const finalFeatures = [
    'gps_speed_kmh',
    'latitude',
    'distance_m',
    'detection_id',
    'bbox_y'
  ];

  const targetCorrelations = [
    { feature: 'gps_speed_kmh', correlation: 0.1600 },
    { feature: 'latitude', correlation: 0.1317 },
    { feature: 'video_time_seconds', correlation: 0.1151 },
    { feature: 'frame_number', correlation: 0.1149 },
    { feature: 'distance_m', correlation: -0.1048 },
    { feature: 'detection_id', correlation: -0.1179 },
    { feature: 'bbox_y', correlation: -0.1308 },
    { feature: 'longitude', correlation: -0.1418 },
    { feature: 'confidence', correlation: -0.1429 },
  ];

  return (
    <div className="feature-selection-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h2 className="section-title" style={{ marginBottom: 0 }}>Feature Selection</h2>
        <a 
          href="https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL/blob/main/analytics/feature_selection.py" 
          target="_blank" 
          rel="noopener noreferrer" 
          className="see-code-btn"
        >
          See Code
        </a>
      </div>

      <div className="cards-grid">
        <div className="card">
          <h3>Final Selected Features</h3>
          <p className="description">
            These features were selected based on their correlation with the target variable (high_risk_event) while removing multicollinear features to optimize the machine learning model.
          </p>
          <ul className="feature-list">
            {finalFeatures.map((feature, idx) => (
              <li key={idx}>
                <span className="feature-bullet"></span>
                <strong>{feature}</strong>
              </li>
            ))}
          </ul>
        </div>

        <div className="card">
          <h3>Target Correlation (&gt; 0.1)</h3>
          <p className="description">
            Features showing significant positive or negative correlation with the `high_risk_event` target variable.
          </p>
          <div className="table-responsive">
            <table className="analysis-table">
              <thead>
                <tr>
                  <th>Feature Name</th>
                  <th>Correlation Coefficient</th>
                </tr>
              </thead>
              <tbody>
                {targetCorrelations.map((item, idx) => (
                  <tr key={idx}>
                    <td>{item.feature}</td>
                    <td>
                      <span className={item.correlation > 0 ? 'pos-corr' : 'neg-corr'}>
                        {item.correlation > 0 ? '+' : ''}{item.correlation.toFixed(4)}
                      </span>
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

export default FeatureSelection;
