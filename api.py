from flask import Flask, jsonify,request 
from random import choice
from experta import *
app = Flask(__name__)
@app.route('/api', methods=['GET'])
def returndata():
    d={} 
    class Light(Fact):
     """Info about the traffic light."""
     pass
    class RobotCrossStreet(KnowledgeEngine):
        @Rule(Light(color='green'))
        def green_light(self):
            answer="Walk"
            d['output']= answer
            return d
        @Rule(Light(color='red'))
        def red_light(self):
            answer="Don't walk"
            d['output']= answer
            return d
        @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
        def cautious(self, light):
            answer= "Be cautious because light is", light["color"]
            d['output']= answer
            return d

    
    imputcolor= str(request.args['color'])
    engine = RobotCrossStreet()
    engine.reset()  
    engine.declare(Light(color=imputcolor))
    engine.run()
    return d
if __name__ == "__main__":

    app.run()
   
    


