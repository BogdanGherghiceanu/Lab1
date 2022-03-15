let db = require('./mongoDB')
var http = require('http')
// let cnp = "2000101001"
// db.findNoteByCnp(cnp)


// function doHomework(subject, callback){
//     console.log(`start ${subject}`)
//     callback();
// }
//
// function printHatz(){
//     console.log("hatzz")
// }
//
// doHomework("cf baby",printHatz)


function requestValidator(path, res) {

    if (path == '/favicon.ico') {
        res.end();
        return 0;
    }
    if (path == '/') {
        res.writeHead(200, {'Content-Type': 'text/json'});
        res.write('{response:200}')
        res.end();
        return 0;
    }

    let path1 = ["elev",
        "profesor",
        "materii"]

    let path2 = ["detalii",
        "note",
    ]
    let path3 = [
        "readAll",
        "add",
        "modify",
        "replace",
        "delete"]

    pathSplit = path.split('/')
    const apiNr = -1;
    if (pathSplit.length >= 2) {
        if (path1.includes(pathSplit[1])) {
            if (pathSplit[1] == "materii")
                return 1
            if (pathSplit.length >= 3) {
                if (path2.includes(pathSplit[2])) {
                    if (pathSplit[1] == "elev") {
                        if (pathSplit[2] == "detalii")
                            return 2;
                        if (pathSplit[2] == "note")
                            return 3;
                    }
                    if (pathSplit[1] == "profesor") {
                        if (pathSplit[2] == "detalii")
                            return 4;
                        if (pathSplit[2] == "note") {
                            if (pathSplit.length >= 4) {
                                if (pathSplit[3] == "readAll") {
                                    return 5;
                                }
                                if (pathSplit[3] == "add") {
                                    return 6;
                                }
                                if (pathSplit[3] == "modify") {
                                    return 7;
                                }
                                if (pathSplit[3] == "replace") {
                                    return 8;
                                }
                                if (pathSplit[3] == "delete") {
                                    return 9;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return -1;
}

function err404(res) {
    res.writeHead(404, "Resurce Not Found");
    res.end('404: Resurce Not Found')

}

function err400(res) {
    res.writeHead(400, "Bad Request");
    res.end('400: Bad Request')

}

function err500(res) {
    res.writeHead(500, "Internal Server Error");
    res.end('500: Internal Server Error')

}

function err401(res) {
    res.writeHead(401, "Unauthorized");
    res.end('401 :Unauthorized')

}

// let p=new Promise((resolve,reject)=>{
//     let result=await db.findAllMaterii()
//     resolve('succes')
// })
var server = http.createServer(function (req, res) {
    let path = req.url
    let apiNr = requestValidator(path, res);
    switch (apiNr) {
        case 0:
            console.log("Response:" + path + " 200 ")
            break;
        case 1:
            if (req.method != "GET") {
                err400(res)
            } else {
                db.findAllMaterii((result) => {
                    //console.log(result)
                    jsonFile = JSON.parse('{}')
                    for (let i = 0; i < result.length; i++) {
                        jsonFile[i] = result[i].nume_materie;
                    }


                    res.writeHead(200, {'Content-Type': 'text/json'});
                    res.write(JSON.stringify(jsonFile));
                    res.end()
                })

            }
            break;

        case 2:
            if (req.method != "GET") {
                err400(res)
            } else {
                console.log(req.headers.cnp)
                db.findUserByCnp(req.headers.cnp, (result) => {

                    if (result == -1)
                        err404(res)
                    else {
                        if (result == -2) {
                            err500(res)
                        } else {
                            if (result.grad == 0) {
                                if (req.headers.key != result.key) {
                                    err401(res)
                                } else {
                                    jsonFile = {
                                        nume: result.nume,
                                        prenume: result.prenume,
                                        cnp: result.cnp,
                                        grad: "student"
                                    }

                                    res.writeHead(200, {'Content-Type': 'text/json'});

                                    res.write(JSON.stringify(jsonFile));
                                    res.end()
                                }
                            } else {
                                err404();
                            }
                        }


                    }
                })

            }
            break;
        case 6:
            if (req.method != "POST") {
                err400(res)
            } else {
                console.log(req.headers.cnp_profesor)
                db.findUserByCnp(req.headers.cnp_profesor, (result) => {
                    console.log(result)
                    if (result == -1)
                        err404(res)
                    else {
                        if (result == -2) {
                            err500(res)
                        } else {
                            if (result.grad == 1) {
                                if (req.headers.key != result.key) {
                                    err401(res)
                                } else {
                                    db.findMaterieByCnp(req.headers.cnp_profesor, (result) => {
                                        console.log(result)
                                        let a=result.nume_materie
                                        db.createNote([{
                                            elev_cnp:req.headers.cnp_elev,
                                            nume_materie:a,
                                            nota:req.headers.nota
                                        }],()=>{})
                                        res.writeHead(200, {'Content-Type': 'text/json'});
                                        res.end(' {code:200}')


                                    })




                                }
                            } else {
                                err404();
                            }
                        }


                    }
                })

            }
            break;
        case 7:

            if(req.method=="PUT"){
            let notaOld={
                elev_cnp:req.headers.elev_cnp,
                nume_materie:req.headers.nume_materie,
                nota:req.headers.nota
            }
            let notaNew={
                nota:req.headers.nota_new
            }
            db.updateNota(notaOld,notaNew,(result)=>{
                if(result==1){
                    res.writeHead(200, {'Content-Type': 'text/json'});

                    res.end('200 :succes');
                }else{
                    err400(res);
                }
            })}
            else{
                err400(res);
            }

            break;
        case 9:

            if(req.method=="DELETE"){
                let nota={
                    elev_cnp:req.headers.elev_cnp,
                    nume_materie:req.headers.nume_materie,
                    nota:req.headers.nota
                }
                db.deleteNota(nota,(result)=>{
                    if(result==1){
                        res.writeHead(200, {'Content-Type': 'text/json'});

                        res.end('200 :succes');
                    }else{
                        err400(res);
                    }
                })}
            else{
                err400(res);
            }

            break;
        default:
            err400(res)
            break;
    }


});

const PORT = 5000
server.listen(PORT);
console.log('Serverul ruleaza la adresa: http://127.0.0.1:' + PORT);