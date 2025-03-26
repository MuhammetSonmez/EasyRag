import os
from fastapi import UploadFile, HTTPException
import pandas as pd

class RagService:
    def __init__(self) -> None:
        pass

    def extract_text(file: UploadFile) -> str:
        file_extension = os.path.splitext(file.filename)[-1].lower()

        if file_extension == ".csv":
            try:
                df = pd.read_csv(file.file)
                if df.empty or df.shape[1] == 0:
                    raise HTTPException(status_code=400, detail="CSV file is empty or cannot be read.")
                
                text = "\n".join(df.iloc[:, 0].astype(str)) 
                return text
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error occurred while processing CSV: {str(e)}")
        
        raise HTTPException(status_code=400, detail=f"{file_extension} format is not supported at the moment.")
