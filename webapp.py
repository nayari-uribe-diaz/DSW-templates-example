from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    optradio1 = request.args ['optradio1']
    optradio2 = request.args ['optradio2']
    optradio3 = request.args ['optradio3']
    optradio4 = request.args ['optradio4']
    
    rules1 = [optradio1 == 'option1', optradio2 == 'option5' or 'option1', optradio3 == 'option2']
    rules2 = [optradio1 == 'option1', optradio2 == 'option5', optradio3 == 'option1']
    
    image = 'Daisy.jpg'
    alttext = 'daisy'
    
    if all(rules1) and optradio4 == 'option3':
        song = 'Day in The Life - The Beatles'
        
    elif all(rules1):
        song = 'Day in The Life - The Beatles'
    else: 
        if all(rules2) and optradio4 == 'option3':
            song = 'Eleanor Rigby - The Beatles'
        else:
            song = 'something else'
    return render_template('page1.html', response = song, songimage = image, imagename = alttext)
   
    '''if optradio2 == 'option5':
        genre = 'psycadelic rock'
    elif optradio2 == 'option3':
        genre = 'concept rock'
    else: 
        optradio3 = request.args ['optradio3']
        if optradio3 == 'option1':
            genre = 'rap music.'
        else:
            genre = 'pop music.'
        return render_template('page2.html', response = genre)
    return render_template('page1.html', response = genre)'''

@app.route("/p2")
def render_page2():
    optradio3 = request.args ['optradio3']
    if optradio3 == 'option1':
        genre = 'rap music.'
    else:
        genre = 'pop music.'
    return render_template('page2.html', response = genre)
    
@app.route("/p3")
def render_page3():
    
    return render_template('page3.html')
 
    
    
    
if __name__=="__main__":
    app.run(debug=False)
