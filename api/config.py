import os
import dotenv
dotenv.load_dotenv()

PORT = os.getenv("PORT")
PathTraining= os.getenv("PathTraining")
PathTest = os.getenv("pathTest")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
pathImagen=os.getenv("pathImagen")