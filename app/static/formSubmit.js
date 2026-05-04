
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
    document.getElementById('name').value = ''
    document.getElementById('message').value = ''
    
    const resMessage =  await res.json()
}

document.getElementById('submit').addEventListener('click', (e) =>{
    e.preventDefault()
    name = document.getElementById('name').value 
    message = document.getElementById('message').value
    
    send(name, message).catch(err => {
        console.log("Error:",err)
    })
})  
