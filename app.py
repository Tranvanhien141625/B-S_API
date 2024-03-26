import uvicorn
from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel

class Dinhgia(BaseModel):
    Phường: str
    Quận: str
    Loại_hình_nhà_ở: str
    Giấy_tờ_pháp_lý: str
    Dài: float
    Rộng: float
    Diện_tích: float
    Số_phòng_ngủ: float
    Số_tầng: float



app = FastAPI()
# Load mô hình đã lưu, và đảm bảo dấu ngoặc đóng chính xác
model = joblib.load('G:\Định giá 2\env\model.pkl')


@app.get('/')
async def index():
    return {'message': 'Định giá nhà ML API'}

@app.post('/predict')
def predict_house( data: Dinhgia):
    
    # Phường= data['Phường']

    # Data = pd.DataFrame({ "Phường": Phường, "Quận": Quận,  "Loại_hình_nhà_ở": Loại_hình_nhà_ở , "Giấy_tờ_pháp_lý": Giấy_tờ_pháp_lý, "Dài": Dài, "Rộng": Rộng,"Diện_tích": Diện_tích, "Số_phòng_ngủ": Số_phòng_ngủ, "Số_tầng": Số_tầng})
    # prediction = model.predict(Data)

    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    
    
    return {"predicted_price": prediction[0]}
  

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)