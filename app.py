from flask import Flask,render_template
app=Flask(__name__) #creating an instance using variable
print('hello')
@app.route('/')
def test() :
    items=[7,8,9,56]
    return render_template("index.html",items=items)

@app.route('/product') # to call or hit the function when the mentioned symbol is called. @ is used for decoration
def product() :
    return render_template('index.html')



if __name__ == '__main__' : # confirming whether the page is main page or not
    app.run(debug=True) # to run the codeapp=Flask(__name__) #creating an instance using variable
