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
    rules2 = [optradio1 == 'option1', optradio2 == 'option5' or 'option2', optradio3 == 'option1']
    rules3 = [optradio1 == 'option1', optradio2 == 'option3', optradio3 == 'option1']
    rules6 = [optradio1 == 'option1'or 'option2', optradio2 == 'option3', optradio3 == 'option2']
    rules4 = [optradio1 == 'option1' or 'option2', optradio2 == 'option3' or 'option5', optradio3 == 'option2']
    rules5 = [optradio1 == 'option2', optradio2 == 'option3' or 'option4', optradio3 == 'option2']
    
    
    if all(rules1) and optradio4 == 'option3':
        song = 'Day in The Life - The Beatles'
        image = 'static/SGTpepper.WEBP'
        alttext = 'Sgt. Pepper`s Lonely Hearts Club Band Album Cover'
    elif all(rules1) and optradio4 == 'option1': 
        song = 'Route 66 - Peggy Suave'
    elif all(rules1) and optradio4 == 'option2':  
        song = 'Tonight You Belong to Me - Lennon Sisters'
    elif all(rules1) and optradio4 == 'option4':
        song = 'The Man Who Stole The World - David Bowie'
    elif all(rules1) and optradio4 == 'option5':
        song = 'Fairy in the Night - Tik Tok'
    elif all(rules1) and optradio4 == 'option6':
        song = ''
    elif all(rules1) and optradio == 'option7':
        song = '2000-2010'
    elif all(rules1) and optradio == 'option8':
        song = 'Eleanor Rigby - The Beatles'
        image = 'static/revolver.jpg'
        alttext = 'Revolver Album Cover'
    elif all(rules1):
        song = 'Day in The Life - The Beatles'
    else: 
        if all(rules2) and optradio4 == 'option3':
            song = 'Eleanor Rigby - The Beatles'
        elif all(rules2) and optradio4 == 'option1': 
            song = 'loud chaotic, fast song. mystical like song from the 1930s'
        elif all(rules2) and optradio4 == 'option2':  
            song = 'loud slow phycadelic song from the 50s'
        elif all(rules2) and optradio4 == 'option4':
            song = 'psycadelic son from the 70s'
        elif all(rules2) and optradio4 == 'option5':
            song = 'fairy in the night by that one guy from tik tok lol'
        elif all(rules2) and optradio4 == 'option6':
            song = '1990'
        elif all(rules2) and optradio == 'option7':
            song = '2000-2010'
        elif all(rules2) and optradio == 'option8':
            song = 'Eleanor Rigby - The Beatles'
        elif all(rules2):
            song = 'Day in The Life - The Beatles'
        else:
            song = 'something else'
            '''image = 'static/SGTpepper.WEBP'
            alttext = 'daisy'''
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
