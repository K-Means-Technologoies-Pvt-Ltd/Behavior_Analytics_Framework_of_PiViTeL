import React from 'react';
import { Code, Database, Layout, PenTool, Cpu } from 'lucide-react';
import './TechStack.css';

const TechStack = () => {
  const stackData = [
    {
      category: 'Programming Languages',
      icon: <Code size={24} className="stack-icon blue" />,
      items: [
        { name: 'Python', desc: 'Core language for data processing, analytics, and machine learning.' },
        { name: 'JavaScript (JSX)', desc: 'Used for building the interactive web-based analytics dashboard.' },
        { name: 'HTML5 & CSS3', desc: 'Markup and styling for the responsive user interface.' }
      ]
    },
    {
      category: 'Data Engineering & Analytics',
      icon: <Database size={24} className="stack-icon purple" />,
      items: [
        { name: 'Pandas', desc: 'Data manipulation, dataset merging, missing value treatment, and feature engineering.' },
        { name: 'NumPy', desc: 'Numerical computations, arrays, and matrix operations.' },
        { name: 'Matplotlib & Seaborn', desc: 'Generating statistical visualizations, heatmaps, and correlation plots.' }
      ]
    },
    {
      category: 'Machine Learning',
      icon: <Cpu size={24} className="stack-icon green" />,
      items: [
        { name: 'Scikit-Learn', desc: 'Model training, evaluation, and feature selection (Logistic Regression, Decision Trees, Random Forest).' }
      ]
    },
    {
      category: 'Frontend Development',
      icon: <Layout size={24} className="stack-icon orange" />,
      items: [
        { name: 'React', desc: 'Component-based UI library used to build the analytics interface.' },
        { name: 'Vite', desc: 'Next-generation frontend tooling and fast development server.' },
        { name: 'React Router DOM', desc: 'Handling client-side routing across different analytics pages.' },
        { name: 'Lucide React', desc: 'Modern SVG icon library used throughout the dashboard.' }
      ]
    },
    {
      category: 'Hardware & Tools',
      icon: <PenTool size={24} className="stack-icon red" />,
      items: [
        { name: 'PiViTeL Edge Device', desc: 'Hardware system utilized for capturing raw video and IMU/GPS telemetry data.' },
        { name: 'Git & GitHub', desc: 'Version control and collaborative code hosting.' }
      ]
    }
  ];

  return (
    <div className="tech-stack-container">
      <h2 className="section-title">Project Tech Stack</h2>
      <p className="section-desc">A comprehensive overview of the languages, libraries, and tools used to build the PiViTeL Behavior Analytics Framework.</p>

      <div className="stack-grid">
        {stackData.map((section, idx) => (
          <div key={idx} className="stack-card">
            <div className="stack-header">
              {section.icon}
              <h3>{section.category}</h3>
            </div>
            <ul className="stack-list">
              {section.items.map((item, itemIdx) => (
                <li key={itemIdx}>
                  <strong>{item.name}</strong>
                  <p>{item.desc}</p>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default TechStack;
