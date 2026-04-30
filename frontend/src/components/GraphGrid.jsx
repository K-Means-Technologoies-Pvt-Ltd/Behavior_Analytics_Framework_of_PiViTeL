import React from "react";
import "./GraphGrid.css";

const base = "/Behavior_Analytics_Framework_of_PiViTeL";

// Manually define image lists (clean + reliable)
const imageMap = {
  univariate: [
    "acceleration_distribution.png",
    "class_pie.png",
    "close_object_risk.png",
    "confidence_histogram.png",
    "gps_course_rose_plot.png",
    "gps_route.png",
  ],
  bivariate: [
    "acceleration_vs_braking.png",
    "acceleration_vs_risk.png",
    "braking_vs_distance.png",
    "distance_vs_object.png",
    "event_correlation.png",
    "pairplot.png",
    "risk_probability_speed.png",
    "speed_vs_acceleration.png",
    "speed_vs_braking.png",
    "speed_vs_class.png",
    "speed_vs_close_risk.png",
    "speed_vs_distance.png",
    "speed_vs_hour.png",
  ],
  correlation: [
    "correlation_heatmap.png",
  ],
};

const GraphGrid = ({ type }) => {
  const images = imageMap[type] || [];

  return (
    <div className="grid">
      {images.map((img, index) => {
        const name = img.replace(".png", "").replace(/_/g, " ");

        return (
          <div key={index} className="flip-card">
            <div className="flip-card-inner">

              {/* FRONT */}
              <div className="flip-card-front">
                <img
                  src={`${base}/analytics/${type}/${img}`}
                  alt={name}
                />
              </div>

              {/* BACK */}
              <div className="flip-card-back">
                <h3>{name}</h3>
                <p>Click to view explanation</p>
              </div>

            </div>
          </div>
        );
      })}
    </div>
  );
};

export default GraphGrid;