import React, { useEffect, useRef } from "react";
import QRCode from "qrcode";

const QRCodeComponent = ({ value, size }) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    QRCode.toCanvas(canvas, value, { width: size }, function (error) {
      if (error) console.error(error);
      console.log("success!");
    });
  }, [value, size]);

  return <canvas ref={canvasRef} />;
};

export default QRCodeComponent;
