import http.server
import socketserver


handler = http.server.SimpleHTTPRequestHandler#переменная для обработки запросов клиента к серверу
with socketserver.TCPServer(("", 1234), handler) as httpd:
   httpd.serve_forever()#сервер будет выполняться постоянно, ожидая запросов от клиента
