from pydantic import BaseModel

class CustomerDetails(BaseModel):
    # Customer demographics
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str

    # Customer account information
    tenure: int

    # Phone service information
    PhoneService: str
    MultipleLines: str

    # Internet service information
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str

    # Contract information
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str

    # Billing information
    MonthlyCharges: float
    TotalCharges: float