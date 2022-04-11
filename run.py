from creator import create_app

app = create_app()
app.config['SECRET_KEY'] = 'hbtn_foundations_capstone'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creator.db'

if __name__ == '__main__':
    app.run(debug=True)