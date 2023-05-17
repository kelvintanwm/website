from website import create_app

app = create_app()

# Only if we run this file and not if we import, then we will execute the line below
if __name__ == '__main__':
    app.run(debug = True)