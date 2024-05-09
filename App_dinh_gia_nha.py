from re import S
import uvicorn
from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel

class Dinhgia(BaseModel):
    Diện tích: float
    Số phòng ngủ: float
    Số phòng toilet: float
    Số tầng: float
    Giấy_tờ_pháp_lý: str
    Nội thất: str
    Đường: str
    Tỉnh: str
    Quận: str
    Phường: str

#numerical_cols = ['Diện tích', 'Số phòng ngủ', 'Số phòng toilet', 'Số tầng']
# categorical_cols = ['balcony_direction',	'house_direction',	'property_legal_document',	'furniture','Đường','Tỉnh',	'Quận',	'Phường']  # thay thế các giá trị thực tế của bạn
#categorical_cols = ['Kiểu nhà','Giấy tờ pháp lý','Nội thất','Đường','Tỉnh',	'Quận',	'Phường']  # thay thế các giá trị thực tế của bạn

app = FastAPI()
# Load mô hình đã lưu, và đảm bảo dấu ngoặc đóng chính xác
model = joblib.load('c:\Users\admin\Downloads\model_nha_ơ_nha_tot_Ha_Noi')


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
