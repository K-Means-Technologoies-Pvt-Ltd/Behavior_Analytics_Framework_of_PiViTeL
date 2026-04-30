import React from 'react';
import './ModelTraining.css';

const ModelTraining = () => {
  const modelComparisons = [
    { name: 'Logistic Regression', accuracy: '99.89%', precision: '100%', recall: '75.00%', f1: '85.71%' },
    { name: 'Decision Tree', accuracy: '99.89%', precision: '100%', recall: '75.00%', f1: '85.71%' },
    { name: 'Random Forest', accuracy: '99.89%', precision: '100%', recall: '75.00%', f1: '85.71%' }
  ];

  const featureImportance = [
    { feature: 'gps_speed_kmh', importance: 0.5259 },
    { feature: 'latitude', importance: 0.1905 },
    { feature: 'bbox_y', importance: 0.1174 },
    { feature: 'detection_id', importance: 0.0887 },
    { feature: 'distance_m', importance: 0.0775 }
  ];

  return (
    <div className="model-training-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h2 className="section-title" style={{ marginBottom: 0 }}>Model Training</h2>
        <a 
          href="https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL/blob/main/analytics/model_training.py" 
          target="_blank" 
          rel="noopener noreferrer" 
          className="see-code-btn"
        >
          See Code
        </a>
      </div>

      <div className="cards-grid">
        <div className="card">
          <h3>Model Comparison</h3>
          <p className="description">
            Performance metrics across different machine learning algorithms trained on the dataset (Train: 3518, Test: 880).
          </p>
          <div className="table-responsive">
            <table className="analysis-table">
              <thead>
                <tr>
                  <th>Model Name</th>
                  <th>Accuracy</th>
                  <th>Precision</th>
                  <th>Recall</th>
                  <th>F1 Score</th>
                </tr>
              </thead>
              <tbody>
                {modelComparisons.map((item, idx) => (
                  <tr key={idx}>
                    <td><strong>{item.name}</strong></td>
                    <td><span className="metric">{item.accuracy}</span></td>
                    <td><span className="metric">{item.precision}</span></td>
                    <td><span className="metric">{item.recall}</span></td>
                    <td><span className="metric">{item.f1}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="card">
          <h3>Feature Importance (Random Forest)</h3>
          <p className="description">
            Relative importance of features contributing to the prediction of high-risk driving events.
          </p>
          <div className="table-responsive">
            <table className="analysis-table">
              <thead>
                <tr>
                  <th>Feature Name</th>
                  <th>Importance</th>
                </tr>
              </thead>
              <tbody>
                {featureImportance.map((item, idx) => (
                  <tr key={idx}>
                    <td>{item.feature}</td>
                    <td>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                        <span className="percent-bar" style={{ width: `${item.importance * 100}%`, margin: 0, backgroundColor: '#a855f7' }}></span>
                        <span className="percent-text">{(item.importance * 100).toFixed(2)}%</span>
                      </div>
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

export default ModelTraining;
