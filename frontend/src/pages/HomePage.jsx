import React from 'react';
import { useNavigate } from 'react-router-dom';
import './HomePage.css';

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div className="home-container">
      <header className="hero-section">
        <h1 className="main-headline">Analytics and Visualisation of Telemetric Data from PiViTeL Edge Device</h1>
        <p className="subtitle">Advanced Behavioral Analytics Framework for insightful device monitoring and statistical modeling.</p>
        <button className="primary-btn" onClick={() => navigate('/analytics/univariate')}>
          Check Analytics
        </button>
      </header>

      <section className="github-section" style={{ textAlign: 'center', padding: '3rem 2rem' }}>
        <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
          <a
            href="https://github.com/K-Means-Technologoies-Pvt-Ltd/Behavior_Analytics_Framework_of_PiViTeL"
            target="_blank"
            rel="noopener noreferrer"
            className="github-link"
            style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.75rem',
              padding: '1rem 2rem', backgroundColor: 'var(--card-bg)', border: '1px solid var(--border)',
              borderRadius: '0.75rem', color: 'var(--text-primary)', textDecoration: 'none',
              fontSize: '1.2rem', fontWeight: 'bold', transition: 'all 0.3s ease'
            }}
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.2c3-.3 6-1.5 6-6.5a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 5 3 6.2 6 6.5a4.8 4.8 0 0 0-1 3.2v4"></path>
            </svg>
            Work Code Repository
          </a>
          <a
            href="/docs/data_visualization_report.pdf"
            target="_blank"
            rel="noopener noreferrer"
            className="github-link"
            style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.75rem',
              padding: '1rem 2rem', backgroundColor: 'var(--card-bg)', border: '1px solid var(--border)',
              borderRadius: '0.75rem', color: 'var(--text-primary)', textDecoration: 'none',
              fontSize: '1.2rem', fontWeight: 'bold', transition: 'all 0.3s ease'
            }}
          >
            Report
          </a>
          <a
            href="/docs/Project_Proposal_CSD25007&CSD25017.pdf"
            target="_blank"
            rel="noopener noreferrer"
            className="github-link"
            style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.75rem',
              padding: '1rem 2rem', backgroundColor: 'var(--card-bg)', border: '1px solid var(--border)',
              borderRadius: '0.75rem', color: 'var(--text-primary)', textDecoration: 'none',
              fontSize: '1.2rem', fontWeight: 'bold', transition: 'all 0.3s ease'
            }}
          >
            Project Proposal
          </a>
        </div>
      </section>

      <section className="workflow-section">
        <h2>System Workflow</h2>
        <div className="workflow-image-container">
          <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1000" alt="Workflow" className="workflow-img" />
          <div className="workflow-overlay">Data Ingestion ➔ Preprocessing ➔ Feature Engineering ➔ Model Inference ➔ Visualization</div>
        </div>
      </section>

      <footer className="footer">
        <div className="contributors">
          <h3>Contributors</h3>
          <div className="contributor-list">
            <div className="contributor-card">
              <div className="avatar">JB</div>
              <p>Jenish A. Borah</p>
            </div>
            <div className="contributor-card">
              <div className="avatar">SS</div>
              <p>Shruti Sarma</p>
            </div>
          </div>
        </div>
        <p className="copyright">© 2026 K-Means Technologies Pvt Ltd. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
