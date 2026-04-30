import React, { useState } from 'react';
import { motion } from 'framer-motion';
import './FlipCard.css';

const FlipCard = ({ graph }) => {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <div className="flip-card-wrapper" onClick={() => setIsFlipped(!isFlipped)}>
      <motion.div
        className="flip-card-inner"
        initial={false}
        animate={{ rotateY: isFlipped ? 180 : 0 }}
        transition={{ duration: 0.6, animationDirection: "normal" }}
        style={{ transformStyle: "preserve-3d" }}
      >
        {/* Front of card */}
        <div className="flip-card-front">
          <img src={graph.img} alt={graph.title} className="graph-thumbnail" />
          <div className="card-content">
            <h3>{graph.title}</h3>
            <p>Click to view explanation</p>
          </div>
        </div>

        {/* Back of card */}
        <div className="flip-card-back">
          <div className="back-content">
            <h3>{graph.title}</h3>
            <div className="divider"></div>
            <p>{graph.desc}</p>
            <span className="click-hint">Click to flip back</span>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default FlipCard;
