from website import create_app

# creates a running web server
app = create_app()

#only running this file will name will app.run be executed (no imported files)
if __name__ == '__main__':
    app.run(debug=True)