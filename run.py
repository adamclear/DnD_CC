from creator import create_app, db

app = create_app()
app.app_context().push()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)