#Test 01/12/2020 00:00:00, 01/01/2021 00:00:00
#Alunos: Mateus Amaral, Gabriel Duarte 
#Parte 1:
import sys, dateconv, requests, bs4

#Parte 2:
stock = sys.argv[1:]

#Parte 3:
date1 = str(dateconv.convert_to_unix(input("Insira a data de inicio: ")))
date2 = str(dateconv.convert_to_unix(input("Insira a data de fim: ")))

#Parte 4:
for i in range(len(stock)):
    #Parte 4.1
    link = "https://br.financas.yahoo.com/quote/" + stock[i] + "/history?period1=" + date1 + "&period2=" + date2 + "&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
    
    #Parte 4.2
    request = requests.get(link)
    request.raise_for_status()
    
    #Parte 4.3
    structure = bs4.BeautifulSoup(request.text, "html.parser")
    tags = structure.select(r"td.Py\(10px\)")
    print(f"Dados da {stock[i]}")
    for j in range(len(tags)):                                                                                                                                                                    
        print(tags[j].select("span")[0].string)

    #Parte 4.4
    print(f"Salvando o .csv de {stock[i]}...")
    link_csv = "https://query1.finance.yahoo.com/v7/finance/download/" + stock[i] + "?period1=" + date1 + "&period2=" + date2 + "&interval=1d&events=history&includeAdjustedClose=true"
    request2 = requests.get(link_csv)
    request2.raise_for_status()
    temp_file = open(f"{stock[i]}.csv","wb")
    for chunk in request2.iter_content(1000000):
        temp_file.write(chunk)
    temp_file.close()
    print(f".csv de {stock[i]} salvo com sucesso.")