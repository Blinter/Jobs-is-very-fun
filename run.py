from app import create_app

app = create_app()


if __name__ == "__main__":
    app_main = create_app()
    app_main.run('0.0.0.0', debug=True)
    # context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # context.load_cert_chain(certfile='ssl/fullchain.pem',
    # keyfile='ssl/privkey.pem')
    # app_main.run('0.0.0.0', debug=True, port=5000, ssl_context=context)
    # app_main.run('0.0.0.0', debug=True, port=5000, ssl_context=(
    #    'ssl/fullchain.pem', 'ssl/privkey.pem'))
