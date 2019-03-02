import bottle
import ticket
import json
import chat


@bottle.route('/')
def web():
    return bottle.static_file("index1.html", root='')


@bottle.route('/map1.js')
def mapjs():
    return bottle.static_file("map1.js", root='')


@bottle.route('/ticket')
def mapdata():
    return ticket.getdata("https://data.buffalony.gov/resource/rmt8-pctg.json", "https://data.buffalony.gov/resource/itjx-a2se.json")


@bottle.route('/chat.js')
def static():
    return bottle.static_file("chat.js", root="")


@bottle.route('/chat')
def get_chat():
    return json.dumps(chat.get_chat())


@bottle.post('/send')
def do_chat():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    chat.add_message(content['message'])
    return json.dumps(chat.get_chat())


bottle.run(host="0.0.0.0", port=8080, debug=True)