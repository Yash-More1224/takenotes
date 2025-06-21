async function save_notes(){
    // runs when save button is clicked
    const title = document.getElementById("note_title").value
    const note = document.getElementById("ipbox").value

    const res = await fetch("http://127.0.0.1:8000/save-notes", { // returns a promise that resolves to a "response" obj
        method: "post", 
        headers: {"Content-Type":"application/json"}, 
        body: JSON.stringify({"title": title, "content": note}, null, 2)        
    });

    const response = await res.json() // returns a "response" obj that provided json data as body
    console.log(response.message)
}