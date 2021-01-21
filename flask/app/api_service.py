from createmodel import *
from flask import request, Response

@app.route('/web', methods=['POST'])
def createWeb():
    url_name = request.json['url_name']
    web_name = request.json['web_name']
    description = request.json['description']
    new_web = web(url_name, web_name, description)
    if new_web:
        db.session.add(new_web)
        db.session.commit()
        return Response(status=201)
    else:
        return Response(status=400)

@app.route('/web', methods=['GET'])
def getWeb():
    all_web = web.query.all()
    if all_web:
        result = web_schema.dump(all_web)
        return web_schema.jsonify(result), 200
    else:
        return Response(status=404)

@app.route('/web/<id>', methods=['PUT'])
def updateWeb(id):
    Web = web.query.get(id)

    url_name = request.json['url_name']
    web_name = request.json['web_name']
    description = request.json['description']

    Web.url_name = url_name
    Web.web_name = web_name
    Web.description = description
    if Web:
        db.session.commit()
        return Response(status=201)
    else:
        return Response(status=404)

@app.route('/web/<id>', methods=['DELETE'])
def deleteWeb(id):
    Web = web.query.get(id)
    if Web:
        db.session.delete(Web)
        db.session.commit()
        return Response(status=200)
    else:
        return Response(status=404)

@app.route('/request', methods=['GET'])
def getWebStatus():
    all_request = webStatus.query.all()
    if all_request:
        result = webstatus_schema.dump(all_request)
        return webstatus_schema.jsonify(result), 200
    else:
        return Response(status=404)

@app.route('/request/<id>', methods=['GET'])
def getbyidRequest(id):
    status = webStatus.query.get(id)
    if status:
        return webstatus1_schema.jsonify(status), 200
    return Response(status=404)


if __name__=="__main__":
    app.run(debug=True)
