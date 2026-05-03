let name = document.getElementById('name').value
let hobbies = document.getElementById('message').value

async function send(name, hobbies) {

    const res =  await fetch('/submit', {
        method: 'POST',
        Headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            message: hobbies,
        })
    })

    const resMessage =  await res.json()
}

document.getElementById('form').addEventListener('submit', (e) =>{
    e.preventDefault()
    
    send(name, hobbies).catch(err => {
        console.log("Error:",err)
    })
})  
