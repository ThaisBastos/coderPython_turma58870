from plyer import notification
from datetime import datetime
import time

def alerta_falha_carregamento(nivel):
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel ==2:
        titulo = "Alerta Médio"
    elif nivel ==3:
        titulo ="Alerta Alto"
    else:
        titulo = "Alerta Desconhecido"

    mensagem = f"Falha de carregamento. Data:{data_atual}"

    notification.notify(
        title=titulo,
        message=mensagem,
        timeout=10
                        )

alerta_falha_carregamento(1)
time.sleep(5)
alerta_falha_carregamento(2)
time.sleep(5)
alerta_falha_carregamento(3)
time.sleep(5)
alerta_falha_carregamento(4)
time.sleep(5)