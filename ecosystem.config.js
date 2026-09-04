module.exports = {
  apps: [
    {
      name: "fastapi-service-myblogs",
      script: ".\\w-venv\\Scripts\\uvicorn.exe", 
      instances: 1, 
      exec_mode: "fork",
      // Optimized with 13 workers to utilize your 6-core Ryzen CPU
      args: "main:app --host 0.0.0.0 --port 8000 --workers 13", 
      interpreter: "none", 
    },
  ],
};
