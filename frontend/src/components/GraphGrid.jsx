import React from 'react';
import FlipCard from './FlipCard';
import './GraphGrid.css';

const univariateImages = [
  'acceleration_distribution.png', 'class_pie.png', 'close_object_risk.png',
  'confidence_histogram.png', 'gps_course_rose_plot.png', 'gps_route.png',
  'high_accleration_distribution.png', 'hour_of_day.png', 'night_driving.png',
  'overspeed_distribution.png', 'risk_by_hour.png', 'risk_pie.png',
  'speed_boxplot.png', 'speed_histogram.png', 'sudden_acceleration_distribution.png',
  'sudden_braking_distribution.png', 'trip_distance.png'
];

const bivariateImages = [
  'acceleration_vs_braking.png', 'acceleration_vs_risk.png', 'braking_vs_distance.png',
  'close_risk_hour.png', 'density_speed_distance.png', 'distance_vs_object.png',
  'event_correlation.png', 'pairplot.png', 'risk_probability_speed.png',
  'speed_vs_acc_event.png', 'speed_vs_acceleration.png', 'speed_vs_acceleration_event.png',
  'speed_vs_braking.png', 'speed_vs_class.png', 'speed_vs_close_risk.png',
  'speed_vs_distance.png', 'speed_vs_hour.png'
];

const correlationImages = [
  'correlation_heatmap.png'
];

const formatName = (filename) => {
  return filename.replace('.png', '').split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
};

const createGraphData = (images, type) => {
  return images.map((img, index) => ({
    id: `${type}-${index}`,
    title: formatName(img),
    img: `/analytics/${type}/${img}`,
    desc: `This graph visualizes ${formatName(img)} to provide insights into driving behavior.`
  }));
};

const data = {
  univariate: createGraphData(univariateImages, 'univariate'),
  bivariate: createGraphData(bivariateImages, 'bivariate'),
  correlation: createGraphData(correlationImages, 'correlation')
};

const GraphGrid = ({ type }) => {
  const graphs = data[type] || [];
  
  const titles = {
    univariate: 'Univariate Analysis',
    bivariate: 'Bivariate Analysis',
    correlation: 'Correlation Analysis'
  };

  const githubLinks = {
    univariate: 'univariate_analysis.py',
    bivariate: 'bivariate_analysis.py',
    correlation: 'correlation_analysis'
  };

  return (
    <div className="graph-grid-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <h2 className="section-title" style={{ marginBottom: 0 }}>{titles[type]}</h2>
        <a 
          href={`https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL/blob/main/analytics/${githubLinks[type]}`} 
          target="_blank" 
          rel="noopener noreferrer"
          style={{
            display: 'inline-block', padding: '0.5rem 1rem', 
            backgroundColor: 'var(--card-bg)', border: '1px solid var(--border)',
            borderRadius: '0.5rem', color: 'var(--text-primary)', textDecoration: 'none',
            fontSize: '1rem', transition: 'all 0.3s ease'
          }}
        >
          See Code
        </a>
      </div>
      <p className="section-desc">Click on any graph to flip and read its detailed statistical explanation.</p>
      
      <div className="grid">
        {graphs.map(graph => (
          <FlipCard key={graph.id} graph={graph} />
        ))}
      </div>
    </div>
  );
};

export default GraphGrid;
