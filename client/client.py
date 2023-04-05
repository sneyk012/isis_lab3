import urllib.request


fp = urllib.request.urlopen("http://localhost:1234/")#запрос к 'http://localhost:1234/'
encodedContent = fp.read()#'encodedContent' соответствует закодированному ответу сервера ('index.html')
decodedContent = encodedContent.decode("utf8")#'decodedContent' соответствует раскодированному ответу сервера (то, что мы хотим вывести на экран)
print(decodedContent)#вывод содержимого файла, полученного с сервера ('index.html')
fp.close()#закрытие соединения с сервером
