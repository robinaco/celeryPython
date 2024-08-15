ENDPOINT_DEV_EVA = "http://localhost:8080"
ENDPOINT_TEST_EVA = "https://eva.testvaosgroup.com"
ENDPOINT_PRD_EVA = "https://www.vumieva.com/"

EVA_LOGIN_URL = ENDPOINT_DEV_EVA + "/eva-system/login.jsp"
HEADERS_LOGIN = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
DATA_ACCESS_LOGIN = {"username": "Pchavez", "password": "Eva12345"}
EVA_URL_PAYMENT = ENDPOINT_DEV_EVA + "/eva-system/ws/payment/register"
HEADERS_PAYMENT = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
