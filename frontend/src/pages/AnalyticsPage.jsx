import React from 'react';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';
import { BarChart, PieChart, Activity, ArrowLeft, Database, Users, FileText, Layers, Cpu, Terminal } from 'lucide-react';
import GraphGrid from '../components/GraphGrid';
import DatasetOverview from './DatasetOverview';
import ContributionDetails from './ContributionDetails';
import DescriptiveAnalysis from './DescriptiveAnalysis';
import FeatureSelection from './FeatureSelection';
import ModelTraining from './ModelTraining';
import TechStack from './TechStack';
import './AnalyticsPage.css';

const AnalyticsPage = () => {
  const navigate = useNavigate();
  const location = useLocation();

  const navItems = [
    { id: 'dataset', label: 'Dataset Overview', icon: <Database size={20} />, path: '/analytics/dataset' },
    { id: 'descriptive', label: 'Descriptive Analysis', icon: <FileText size={20} />, path: '/analytics/descriptive' },
    { id: 'univariate', label: 'Univariate Analysis', icon: <PieChart size={20} />, path: '/analytics/univariate' },
    { id: 'bivariate', label: 'Bivariate Analysis', icon: <BarChart size={20} />, path: '/analytics/bivariate' },
    { id: 'correlation', label: 'Correlation Analysis', icon: <Activity size={20} />, path: '/analytics/correlation' },
    { id: 'feature-selection', label: 'Feature Selection', icon: <Layers size={20} />, path: '/analytics/feature-selection' },
    { id: 'model-training', label: 'Model Training', icon: <Cpu size={20} />, path: '/analytics/model-training' },
    { id: 'contribution', label: 'Contribution Details', icon: <Users size={20} />, path: '/analytics/contribution' },
    { id: 'tech-stack', label: 'Tech Stack', icon: <Terminal size={20} />, path: '/analytics/tech-stack' },
  ];

  // Default redirect to dataset
  React.useEffect(() => {
    if (location.pathname === '/analytics' || location.pathname === '/analytics/') {
      navigate('/analytics/dataset', { replace: true });
    }
  }, [location, navigate]);

  return (
    <div className="analytics-container">
      <aside className="sidebar">
        <div className="sidebar-header">
          <button className="back-btn" onClick={() => navigate('/')}>
            <ArrowLeft size={20} /> Back Home
          </button>
        </div>
        <nav className="side-nav">
          {navItems.map((item) => (
            <button
              key={item.id}
              className={`nav-item ${location.pathname.includes(item.path) ? 'active' : ''}`}
              onClick={() => navigate(item.path)}
            >
              {item.icon}
              {item.label}
            </button>
          ))}
        </nav>
      </aside>
      
      <main className="analytics-content">
        <Routes>
          <Route path="dataset" element={<DatasetOverview />} />
          <Route path="descriptive" element={<DescriptiveAnalysis />} />
          <Route path="univariate" element={<GraphGrid type="univariate" />} />
          <Route path="bivariate" element={<GraphGrid type="bivariate" />} />
          <Route path="correlation" element={<GraphGrid type="correlation" />} />
          <Route path="feature-selection" element={<FeatureSelection />} />
          <Route path="model-training" element={<ModelTraining />} />
          <Route path="contribution" element={<ContributionDetails />} />
          <Route path="tech-stack" element={<TechStack />} />
        </Routes>
      </main>
    </div>
  );
};

export default AnalyticsPage;
