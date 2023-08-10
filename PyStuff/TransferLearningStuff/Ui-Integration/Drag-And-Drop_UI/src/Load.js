import React, { useState, useEffect } from "react";

export default function Load({ imageUrl }) {
  const [loading, setLoading] = useState(true);
  const [loadedImageUrl, setLoadedImageUrl] = useState("");

  useEffect(() => {
    if (imageUrl) {
    
      setLoading(true);
      setTimeout(() => {
        setLoadedImageUrl(imageUrl);
        setLoading(false);
      }, 1000);
    }
  }, [imageUrl]);

  return (
    <div className="drag-and-drop-box">
      {loading ? (
        <div className="loader"></div>
      ) : (
        <img src={loadedImageUrl} alt="uploaded" className="result--img"/>
      )}
    </div>
  );
}
