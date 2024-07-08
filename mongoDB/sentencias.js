// insertOne

var user2 = {
    name: 'John',
    last_name: 'Doe',
    age: 21,
    email: 'john@example.com'
}

db.users.insertOne(user2)

// insertMany

var user3 = {
    name: 'John',
    last_name: 'Goe',
    age: 22,
    email: 'johngoe@example.com'
}

var user4 = {
    name: 'Alan',
    last_name: 'Poe',
    age: 22,
    email: 'apoe@example.com'
}

db.users.insertMany([user3, user4])

db.users.find(
    {age:22},
    {last_name:true, email:true}
)

db.users.find( { age: { $lt: 22, $gte: 20} }, {  last_name: false, _id: false} )

db.users.find(
    {
        $and: [
            {age : { $lt: 22}},
            {age : { $gt: 20}},
        ]
    }
)




db.users.find(
    {
        $or: [
            {age : {$gt: 21}},
            {name : 'Alan'},
        ]
    }
)




db.books.insertMany(
    [
        {title: 'Don Quijote de la Mancha', sales: 500},
        {title: 'Historia de dos ciudades', sales: 200},
        {title: 'El se?or de los anillos', sales: 150},
        {title: 'El principito', sales: 140},
        {title: 'El hobbit', sales: 100},
        {title: 'Alicia en el pais de las maravillas', sales: 100},
        {title: 'El cédigo Da Vinci', sales: 80},
        {title: 'El alquimista', sales: 65},
    ]
)

db.users.find(
    {
        last_name: {
            $in: ['Doe','Goe']
        }
    }
)