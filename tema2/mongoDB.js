const {MongoClient} = require('mongodb');
const uri = "mongodb+srv://ccLab2user:00000000@cluster0.pvlrp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

let db = {
    findUserByCnp: async function (cnp, callback) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            console.log(typeof (cnp))
            err=0;
            const result = await client.db("myClass").collection("users").findOne({cnp: cnp});

            if (result) {
                console.log(`Am gasit userul: '${cnp}':`);
                console.log(result);
            } else {
                err=1
                console.log(`Nu amm gasit userul '${cnp}'`);
            }
            await client.close();
            if(err==0)
                callback(result)
            else
                callback(-1)
        } catch (e) {
            console.error(e);
            callback(-2);
        }
    },


    findNoteByCnp: async function (cnp) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const cursor = client.db("myClass").collection("note").find({elev_cnp: `${cnp}`});
            const result = await cursor.toArray();
            if (result) {
                console.log(`Au fost gasite note pentru '${cnp}':`);
                console.log(result);

            } else {
                console.log(`Nu au fost gasite note pentru '${cnp}'`);
            }
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    findAllUsers: async function (callback) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const cursor = client.db("myClass").collection("users").find();
            const result = await cursor.toArray();
            if (result) {
                console.log(`Au fost gasite note pentru :`);
                console.log(result);
                callback(result)
            } else {
                console.log(`Nu au fost gasite note pentru `);
            }
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },
    findAllMaterii: async function (calllback) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const cursor = client.db("myClass").collection("materii").find();
            const result = await cursor.toArray();
            if (result) {
                console.log(`Au fost trimise materiile:`);
                //console.log(result);


            } else {
                console.log(`Nu au fost gasite materii`);
                result=-1
            }
            await client.close();
            calllback(result);
        } catch (e) {
            console.error(e);
        }
    },

    findMaterie: async function (nume_materie) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("materii").findOne({nume_materie: nume_materie});

            if (result) {
                console.log(`Am gasit materia: '${nume_materie}':`);
                console.log(result);
            } else {
                console.log(`Nu am gasit materia '${nume_materie}'`);
            }
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    findMaterieByCnp: async function (cnp, callback) {

        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("materii").findOne({profesor_cnp: cnp});
            let err=0;
            if (result) {
                console.log(`Am gasit materia pt : '${cnp}':`);
                console.log(result);
                callback(result)
            } else {
                err=-1
                console.log(`Nu am gasit materia pt'${cnp}'`);
            }
            await client.close();
            if(err=-1)
                callback(-1)
            else
                callback(result)
        } catch (e) {
            console.error(e);
            callback(-2)
        }
    },


    createUsers: async function (newUsers) {
        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#insertMany for the insertMany() docs

        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("users").insertMany(newUsers);

            console.log(`${result.insertedCount} au fost adaugati userii cu id:`);
            console.log(result.insertedIds);
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    createMaterii: async function (newMaterii) {
        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#insertMany for the insertMany() docs

        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("materii").insertMany(newUsers);

            console.log(`${result.insertedCount} au fost adaugate materiile cu id:`);
            console.log(result.insertedIds);
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    createNote: async function (newNote, callback) {
        // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#insertMany for the insertMany() docs

        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("note").insertMany(newNote);

            console.log(`${result.insertedCount} au fost adaugate notele cu id:`);
            console.log(result.insertedIds);
            await client.close();
            callback(result)
        } catch (e) {
            console.error(e);
        }
    },

    updateNota: async function (notaOld, notaNew, callback) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("note").updateOne(notaOld, {$set: notaNew}, {upsert: true});
            console.log(`${result.matchedCount} document(s) matched the query criteria.`);

            if (result.modifiedCount > 0) {
                // console.log(`Nota a fost modificata. ID: ${result.upsertedId._id}`);
                callback(1)
            } else {
                callback(1)
                // console.log(`${result.modifiedCount} document(s) was/were updated.`);
            }
            await client.close();
        } catch (e) {
            callback(-1)
            console.error(e);
        }
    },

    updateMaterie: async function (materieOld, materieNew) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("materii").updateOne(materieOld, {$set: materieNew}, {upsert: true});
            console.log(`${result.matchedCount} document(s) matched the query criteria.`);

            if (result.upsertedCount > 0) {
                console.log(`Materia a fost modificata. ID: ${result.upsertedId._id}`);
            } else {
                console.log(`${result.modifiedCount} document(s) was/were updated.`);
            }
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    updateUser: async function (userOld, userNew) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("users").updateOne(userOld, {$set: userNew}, {upsert: true});
            console.log(`${result.matchedCount} document(s) matched the query criteria.`);

            if (result.upsertedCount > 0) {
                console.log(`Userul a fost modificata. ID: ${result.upsertedId._id}`);
            } else {
                console.log(`${result.modifiedCount} document(s) was/were updated.`);
            }
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    deleteUser: async function (user) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("users").deleteOne(user);
            console.log(`${result.deletedCount} user was/were deleted.`);
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },
    deleteMaterie: async function (materie) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("materii").deleteOne(materie);
            console.log(`${result.deletedCount} materie was/were deleted.`);
            await client.close();
        } catch (e) {
            console.error(e);
        }
    },

    deleteNota: async function (nota, callback) {
        try {
            const client = new MongoClient(uri);
            await client.connect();
            const result = await client.db("myClass").collection("note").deleteOne(nota);
            console.log(`${result.deletedCount} nota was/were deleted.`);
            await client.close();
            callback(1)
        } catch (e) {
            console.error(e);
            callback(-1)
        }
    }
}

module.exports = db;


// let userOld = [
//     {
//         nume: "Luca",
//         prenume: "Mihai",
//         key: "12345",
//         cnp: "1950101001",
//         grad: 1
//     }
// ]
// createUsers(userOld).catch(console.error)
// let user={
//     cnp:"1950101001"
// }
// deleteUser(user);
// let cnp = "2000101001"
//findUserByCnp(cnp).catch(console.error);
// findNoteByCnp(cnp).catch(console.error);
// findMaterie("matematica").catch(console.error);
// let newUsers = [
//     {
//         nume: "Gabor",
//         prenume: "Andrei",
//         key: "0",
//         cnp: "2000101002",
//         grad: 0
//     },
//     {
//         nume: "Luca",
//         prenume: "Mihai",
//         key: "12345",
//         cnp: "2000101002",
//         grad: 1
//     }
// ]
// createUsers(newUsers).catch(console.error)
// const {MongoClient} = require('mongodb');
//
// async function main(cnp){
//     const uri= "mongodb+srv://ccLab2user:00000000@cluster0.pvlrp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
//     const client = new MongoClient(uri);
//     try {
//         await client.connect();
//         await findOneListingByName(client,cnp);
//     }catch (e){
//         console.error(e);
//     }finally {
//         await  client.close();
//     }
// }
//
// async function findOneListingByName(client, cnp) {
//     // See https://mongodb.github.io/node-mongodb-native/3.6/api/Collection.html#findOne for the findOne() docs
//     const result = await client.db("myClass").collection("users").findOne({ cnp: cnp });
//
//     if (result) {
//         console.log(`Found a listing in the collection with the name '${cnp}':`);
//         console.log(result);
//     } else {
//         console.log(`No listings found with the name '${cnp}'`);
//     }
// }
//
// let cnp="2000101001"
// main(cnp).catch(console.error);
// main(cnp).catch(console.error);
// main(cnp).catch(console.error);
//

