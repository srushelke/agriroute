 AgriRoute is a RESTful API prototype built to streamline agricultural supply chain logistics — connecting farms, managing shipments, optimizing delivery routes, and handling real-time disruptions.

 This is an early-stage prototype. Features and endpoints are under active development.
 

# Features:
Farm Management: Register and manage farm profiles and their produce
Shipment Tracking: Create and monitor agricultural shipments end-to-end
Route Optimization: Plan and retrieve optimal delivery routes
Disruption Handling: Log and respond to supply chain disruptions (weather, delays, etc.)
CORS-enabled: Ready for frontend integration (React / Next.js)


# Tech Stack:
 Layer        Technology                  
 Framework    [FastAPI](https://fastapi.tiangolo.com/) 
 Language     Python 3.x                  
 Database     PostgreSQL (via `database.py`) 
 Deployment   Heroku (Procfile included)  


# Project Structure:
agriroute/
├── routers/
│   ├── farms.py          # Farm registration & management
│   ├── shipments.py      # Shipment creation & tracking
│   ├── routes.py         # Route planning & retrieval
│   └── disruptions.py    # Disruption logging & alerts
├── database.py           # DB connection & session management
├── main.py               # FastAPI app entry point
├── requirements.txt      # Python dependencies
├── Procfile              # Heroku deployment config
└── .env                  # Environment variables (not committed)




# Prerequisites:
- Python 3.9+
- pip
- A running PostgreSQL instance


# Installation:
1. Clone the repository
git clone https://github.com/srushelke/agriroute.git
cd agriroute

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables
cp .env.example .env


# Running the Server:
The API will be available at `http://localhost:8000`.
Interactive API docs (Swagger UI): `http://localhost:8000/docs`


# API Endpoints:
 Method  Endpoint               Description                  
 GET       `/`                    Health check                 
 GET/POST  `/api/farms`         List / create farms          
 GET/POST  `/api/shipments`     List / create shipments      
 GET/POST  `/api/routes`        List / compute routes        
 GET/POST  `/api/disruptions`   List / report disruptions    

> Full interactive documentation is auto-generated at `/docs` when the server is running.


 # Deployment:
This project includes a `Procfile` for Heroku deployment.

   Deploy to Heroku
  heroku create your-app-name
  heroku config:set DATABASE_URL=your_database_url
  git push heroku main


# Environment Variables:
Create a `.env` file in the root directory with the following:
DATABASE_URL=postgresql://user:password@localhost:5432/agriroute
Never commit your `.env` file. It is already listed in `.gitignore`.



 # Roadmap:
  Authentication & role-based access (farmer / distributor / admin)
  Real-time disruption notifications (WebSockets)
  Route optimization algorithm integration
  Frontend dashboard (React)
  Unit & integration tests
  Docker support

 
 # Contributing:

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

 
# License:
This project is currently unlicensed. License details will be added in a future release.


 Author:
Srushti Shelke  
GitHub: [@srushelke](https://github.com/srushelke)
