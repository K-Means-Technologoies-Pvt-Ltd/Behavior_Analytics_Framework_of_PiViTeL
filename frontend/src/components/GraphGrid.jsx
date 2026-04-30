import React from "react";

// Base path for GitHub Pages
const base = "/Behavior_Analytics_Framework_of_PiViTeL";

// Auto-import all images from analytics folders
const imageModules = import.meta.glob(
  "/analytics/**/*.{png,jpg,jpeg,svg}",
  { eager: true }
);

const GraphGrid = ({ type }) => {
  // Filter images based on type (univariate, bivariate, etc.)
  const images = Object.entries(imageModules)
    .filter(([path]) => path.includes(`/analytics/${type}/`))
    .map(([path, module]) => ({
      path,
      src: module.default,
      name: path.split("/").pop().replace(".png", "").replace(/_/g, " "),
    }));

  return (
    <div className="grid">
      {images.map((img, index) => (
        <div key={index} className="card">
          <img src={img.src} alt={img.name} />
          <h3>{img.name}</h3>
        </div>
      ))}
    </div>
  );
};

export default GraphGrid;