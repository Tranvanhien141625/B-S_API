from re import S
import uvicorn
from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel


#area Diện tích
# way_in: Chiều rộng ngõ
#frontage: Mặt tiền

class Dinhgia(BaseModel):
    area: float
    way_in: float
    frontage: float
    bedroom: float
    toilet: float
    floors: float
    Phường: str
    Quận: str
    Tỉnh: str
    



app = FastAPI()
# Load mô hình đã lưu, và đảm bảo dấu ngoặc đóng chính xác
model = joblib.load('C:\Users\admin\Downloads\APP_nha_o\model_nha_mat_pho_khong_ten_duong.pkl')


@app.get('/')
async def index():
    return {'message': 'Định giá nhà ML API'}

@app.post('/predict')
def predict_house( data: Dinhgia):
    
    #

    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    
    
    return {"predicted_price": prediction[0]}
  

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
